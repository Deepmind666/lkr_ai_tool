param(
    [Parameter(Mandatory = $true)]
    [string]$DocxPath
)

$ErrorActionPreference = "Stop"
$OutputEncoding = [Console]::OutputEncoding = [System.Text.UTF8Encoding]::new()

if (-not (Test-Path -LiteralPath $DocxPath)) {
    throw "DOCX not found: $DocxPath"
}

Add-Type -AssemblyName System.IO.Compression
Add-Type -AssemblyName System.IO.Compression.FileSystem

function Get-NodeText {
    param($Node, $Ns)
    return (($Node.SelectNodes('.//w:t', $Ns) | ForEach-Object { $_.InnerText }) -join '')
}

$zip = [System.IO.Compression.ZipFile]::OpenRead($DocxPath)
try {
    $required = @(
        '[Content_Types].xml',
        'word/document.xml',
        'word/styles.xml',
        'word/numbering.xml',
        'word/settings.xml'
    )

    foreach ($name in $required) {
        if (-not $zip.GetEntry($name)) {
            throw "Missing DOCX package entry: $name"
        }
    }

    $entry = $zip.GetEntry('word/document.xml')
    $reader = [System.IO.StreamReader]::new($entry.Open())
    $documentXml = $reader.ReadToEnd()
    $reader.Close()

    $xml = [System.Xml.XmlDocument]::new()
    $xml.PreserveWhitespace = $true
    $xml.LoadXml($documentXml)

    $ns = [System.Xml.XmlNamespaceManager]::new($xml.NameTable)
    $ns.AddNamespace('w', 'http://schemas.openxmlformats.org/wordprocessingml/2006/main')

    $bookmarks = @(
        $xml.SelectNodes('//w:bookmarkStart', $ns) |
            ForEach-Object { $_.GetAttribute('name', 'http://schemas.openxmlformats.org/wordprocessingml/2006/main') }
    )

    $refNums = @()
    foreach ($bookmark in $bookmarks) {
        if ($bookmark -match '^Ref_(\d+)$') {
            $refNums += [int]$Matches[1]
        }
    }

    $missingRefs = @()
    $maxRef = 0
    if ($refNums.Count -gt 0) {
        $maxRef = ($refNums | Measure-Object -Maximum).Maximum
        foreach ($i in 1..$maxRef) {
            if ($refNums -notcontains $i) {
                $missingRefs += $i
            }
        }
    }

    $citationLinks = @(
        $xml.SelectNodes('//w:hyperlink', $ns) |
            Where-Object {
                $_.GetAttribute('anchor', 'http://schemas.openxmlformats.org/wordprocessingml/2006/main') -match '^Ref_\d+$' -and
                (Get-NodeText $_ $ns) -match '^\[\d+\]$'
            }
    )

    $nonSuperscriptRuns = 0
    foreach ($link in $citationLinks) {
        foreach ($run in $link.SelectNodes('.//w:r', $ns)) {
            $vertAlign = $run.SelectSingleNode('./w:rPr/w:vertAlign', $ns)
            $val = if ($vertAlign) {
                $vertAlign.GetAttribute('val', 'http://schemas.openxmlformats.org/wordprocessingml/2006/main')
            } else {
                'plain'
            }
            if ($val -ne 'superscript') {
                $nonSuperscriptRuns++
            }
        }
    }

    $algorithmTables = 0
    $algorithmNonLeftParagraphs = 0
    $algorithmWord = ([string][char]0x7B97) + ([string][char]0x6CD5)
    $algorithmPattern = '^' + [regex]::Escape($algorithmWord) + '\d+\.\d+'
    foreach ($table in $xml.SelectNodes('//w:body/w:tbl', $ns)) {
        $text = Get-NodeText $table $ns
        if ($text -match $algorithmPattern) {
            $algorithmTables++
            foreach ($paragraph in $table.SelectNodes('.//w:p', $ns)) {
                $pPr = $paragraph.SelectSingleNode('./w:pPr', $ns)
                $jc = if ($pPr) { $pPr.SelectSingleNode('./w:jc', $ns) } else { $null }
                $align = if ($jc) {
                    $jc.GetAttribute('val', 'http://schemas.openxmlformats.org/wordprocessingml/2006/main')
                } else {
                    '(none)'
                }
                if ($align -ne 'left') {
                    $algorithmNonLeftParagraphs++
                }
            }
        }
    }

    [pscustomobject]@{
        docx = (Resolve-Path -LiteralPath $DocxPath).Path
        package_ok = $true
        highlight_count = $xml.SelectNodes('//w:highlight', $ns).Count
        ref_bookmarks = $refNums.Count
        max_ref = $maxRef
        missing_refs = ($missingRefs -join ',')
        citation_links = $citationLinks.Count
        non_superscript_citation_runs = $nonSuperscriptRuns
        algorithm_tables = $algorithmTables
        algorithm_non_left_paragraphs = $algorithmNonLeftParagraphs
    } | Format-List
}
finally {
    $zip.Dispose()
}

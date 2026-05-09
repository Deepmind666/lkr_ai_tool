# CodeWiki Playbook

CodeWiki is an optional repository-documentation generator. Use it when a repo
needs a durable architecture wiki, onboarding map, or module-level explanation
for another agent or teammate.

Do not use CodeWiki as the first tool for small edits. Start with `rg`, direct
file reads, GitNexus, or Repomix when the question is narrow. CodeWiki is most
useful after the repo boundary and ignore rules are already clear.

## Fit

Use CodeWiki for:

- architecture overview pages for an unfamiliar codebase;
- module and dataflow summaries that should persist across sessions;
- handoff docs for another GPT, Codex, or Claude Code session;
- comparing large subsystems after a codebase has stabilized.

Avoid CodeWiki for:

- one-file edits or small bug fixes;
- private raw drafts, datasets, experiment dumps, model weights, caches, or
  credentials;
- claims that require line-level proof without source inspection;
- every-turn usage in an active coding session.

## Privacy And Scope Rules

Before running CodeWiki, define the target repo and exclusions. Never point it
at a whole disk or a mixed workspace.

Recommended exclusions:

```text
.git/
.venv/
venv/
node_modules/
build/
dist/
__pycache__/
.cache/
*.zip
*.tar
*.tar.gz
*.zst
*.npz
*.npy
*.pt
*.pth
*.safetensors
*.onnx
*.et
*.log
moe_runs/
local_runs/
artifacts/figures/**/figures/
experiments/**/output*/
experiments/**/results*/
experiments/**/Stage1_collect/results/
```

## Suggested Workflow

Install and validate CodeWiki on the machine that will generate documentation:

```powershell
python -m pip install "git+https://github.com/FSoft-AI4Code/CodeWiki.git"
codewiki --version
codewiki config show
codewiki config validate
```

CodeWiki supports OpenAI-compatible, Anthropic, Azure OpenAI, and AWS Bedrock
providers. Do not commit API keys. CodeWiki stores settings under
`~/.codewiki/config.json`; credentials may use the OS keychain or
`~/.codewiki/credentials.json` in headless environments.

1. Check repo cleanliness and target scope:

   ```powershell
   git status -sb
   rg --files . | Select-Object -First 40
   ```

2. Build a small source-only snapshot if the repo is noisy:

   ```powershell
   repomix.cmd . --style markdown --output repomix-output.md --top-files-len 30
   ```

3. Configure source-only agent settings:

   ```powershell
   codewiki config agent --exclude ".git,.venv,venv,node_modules,build,dist,__pycache__,.cache,*.zip,*.tar,*.tar.gz,*.zst,*.npz,*.npy,*.pt,*.pth,*.safetensors,*.onnx,*.et,*.log,moe_runs,local_runs"
   codewiki config agent --doc-type architecture
   ```

4. Run CodeWiki only on the intended repo or source subset. Keep its output in a
   generated documentation folder such as `docs/codewiki/` or a project-local
   handoff folder.

   ```powershell
   codewiki generate --output docs/codewiki --verbose
   ```

5. Verify CodeWiki claims by opening the cited files directly. Treat the wiki as
   navigation and onboarding material, not as proof.

6. Do not commit generated wiki pages unless the project explicitly wants a
   frozen onboarding snapshot. If committed, include the exact command, source
   commit, model/provider, and exclusions.

## MoE/Astra-Sim Usage

For the MoE workload simulation project, CodeWiki can help explain:

- how routing traces become statistical matrices;
- how dynamic load sequences become per-rank compute and peer-wise All-to-Allv
  bytes;
- how Chakra ET files and ASTRA-sim smoke checks are generated;
- where figures, manifests, and experiment summaries are built.

It should not index raw trace arrays, generated `.npz` matrices, `.et` files,
large experiment outputs, or synced machine archives.

## Position In The Stack

- `rg`: fastest proof-oriented lookup.
- GitNexus/Serena: graph or symbol retrieval while editing.
- Repomix: portable source snapshot for agents.
- CodeWiki: slower architecture wiki and onboarding documentation.

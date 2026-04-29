# gpt-image-2 Tips

The user may say `gpt-2-image`; the current official OpenAI model page names the
image model `gpt-image-2`.

Official model page:

- https://developers.openai.com/api/docs/models/gpt-image-2

## Best Use In This Workflow

Use image generation for visual assets, not for whole editable documents.

Good uses:

- PPT hero/background images,
- object renders,
- cover or section illustrations,
- visual metaphors,
- texture or material studies,
- icons or image references that will be redrawn as editable shapes,
- style exploration before final diagramming.

Avoid:

- asking the model to render precise Chinese or English slide text,
- dense charts,
- tables,
- equations,
- final reference labels,
- whole PPT slides that should remain editable.

## Current Limitation To Remember

The official `gpt-image-2` model page states that transparent backgrounds are
not supported yet. Plan around this:

- generate assets on a solid white, black, or brand-color background;
- crop or mask inside PowerPoint/WPS;
- use a separate background removal tool if transparency is truly needed;
- for icons, prefer native SVG/icon libraries when possible.

## Prompt Pattern

Use one image for one job:

```text
Purpose: [background / object render / illustration / texture / icon concept]
Subject: [specific object or scene]
Composition: [framing, camera angle, negative space]
Style: [realistic / editorial / clean technical / flat illustration]
Color constraints: [palette or avoid list]
Output use: [PPT background with editable text over it / figure asset / cover]
Avoid: [text, labels, watermark, clutter, extra objects]
```

## PPT-Safe Image Rules

- Leave negative space where editable slide text will sit.
- Do not ask the image model to place the title in the image.
- Keep the subject large enough to crop at 16:9 and 4:3 if needed.
- Generate backgrounds and foreground objects separately when possible.
- Store the prompt beside the asset in `templates/image_prompt_record.md` format.

## Useful Workflow

1. Draft the slide as editable PPT first.
2. Decide which visual element cannot be made cleanly with shapes/icons.
3. Generate only that visual element or background.
4. Insert it into PPT.
5. Add all text, labels, arrows, and chart data as editable PPT objects.
6. Save the prompt, source image, edited image, and PPTX together.

## Quality Checks

- Can the slide still be understood if the image is removed?
- Are all important labels editable text?
- Does the image contain broken text, watermarks, or unwanted symbols?
- Is the resolution high enough for the final page size?
- Does the crop still work on the target slide ratio?


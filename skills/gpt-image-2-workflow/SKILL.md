---
name: gpt-image-2-workflow
description: Use OpenAI gpt-image-2 for document and PPT visual assets while keeping text, labels, charts, and slide structure editable.
---

# gpt-image-2 Workflow

Use this skill when generating or revising AI images for documents, slides, or
figures.

## Rule

Generate visual assets, not final editable documents. Keep titles, labels,
arrows, equations, charts, and dense text outside the image whenever possible.

## Prompt Shape

Specify:

- purpose,
- subject,
- composition,
- style,
- color constraints,
- output use,
- what to avoid.

## PPT And Document Use

- Leave negative space for editable text.
- Avoid asking the model to render exact text.
- Generate backgrounds and foreground assets separately when possible.
- Store prompt, model, date, source image, edited image, and final use path.
- Remember that the current official `gpt-image-2` page says transparent
  backgrounds are not supported yet.


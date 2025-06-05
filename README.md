# Image Captioning and Visual Question Answering

This project uses Salesforce's BLIP (Bootstrapping Language-Image Pre-training) models to generate descriptive captions for images and answer questions about them. It provides an interactive command-line interface for selecting an image, viewing a generated caption, and optionally asking a question about the image.

## Features

- **Image Captioning**: Generates captions for images using the `BlipForConditionalGeneration` model.
- **Visual Question Answering (VQA)**: Answers user questions about images using the `BlipForQuestionAnswering` model.
- Supports three predefined images (`grok1.jpg`, `grok2.jpg`, `grok3.jpg`) in the `images/` directory.
- Includes basic error handling for invalid inputs.

## Prerequisites

- **Python**: Version 3.7 or higher
- **Dependencies**:
  - `transformers`
  - `Pillow` (PIL)
  - `torch`

Install dependencies with:
```bash
pip install transformers pillow torch
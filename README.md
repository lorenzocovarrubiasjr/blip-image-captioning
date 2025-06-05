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
```

### Example Output
```bash 
🤖 Select an image to generate a caption for:
1️⃣ Image 1
2️⃣ Image 2
3️⃣ Image 3
> 1
🤖🖼️ Generated Caption:
A serene lake surrounded by mountains under a clear blue sky.
❓ Would you like to ask a question regarding this image?
Insert Y or N:
> Y
Enter your question:
What is the color of the sky?
🤖 AI's Answer: The sky is blue.
👋 Thank you, come again!
```
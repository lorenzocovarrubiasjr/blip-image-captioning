from transformers import BlipProcessor, BlipForConditionalGeneration, BlipForQuestionAnswering
from PIL import Image

processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-large")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-large")
qa_processor = BlipProcessor.from_pretrained("Salesforce/blip-vqa-base")
qa_model = BlipForQuestionAnswering.from_pretrained("Salesforce/blip-vqa-base")

while True:
    try:
        user_selection = int(input("🤖 Select an image to generate a caption for:\n1️⃣ Image 1\n2️⃣ Image 2\n3️⃣ Image 3\n"))
        image = Image.open(f"images/grok{user_selection}.jpg")
        inputs = processor(image, return_tensors="pt")

        outputs = model.generate(**inputs)
        caption = processor.decode(outputs[0], skip_special_tokens=True)
        print("🤖🖼️ Generated Caption:\n", caption)

        user_has_a_question = input("❓ Would you like to ask a question regarding this image?\nInsert Y or N:\n")
        if(user_has_a_question.capitalize() == "Y"):
            raw_image = Image.open(f"images/grok{user_selection}.jpg").convert('RGB')

            question = input("Enter your question:\n")  
            question_inputs = qa_processor(raw_image, question, return_tensors="pt")
            question_out = qa_model.generate(**question_inputs)
            answer = qa_processor.decode(question_out[0], skip_special_tokens=True)
            print(f"🤖 AI's Answer: {answer}")
        break
    except ValueError:
        print("❌ Invalid entry.")
    finally:
        print("👋 Thank you, come again!")
    



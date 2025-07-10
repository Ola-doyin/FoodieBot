# chat.py
import google.generativeai as genai

def generate_content(model, prompt_text, uploaded_files=None, language="English"):    
    if uploaded_files:
        # Convert uploaded files to Parts for multimodal prompts
        parts = [{"mime_type": file.type, "data": file.read()} for file in uploaded_files]
        content = [prompt_text] + parts
    else:
        content = prompt_text

    response = model.generate_content(
        content,
        generation_config={
            "temperature": 0.7,
            "top_p": 1,
            "top_k": 1,
            "max_output_tokens": 512,
        }
    )
    try:
        return response.text.strip().replace("\n", "<br>")
    except ValueError:
        if language == "English":
            return "Opps! 🤖 Looks like I couldn't quite cook up a response for that. Could you try rephrasing your question, please? 😊"
        elif language == "Yoruba":
            return "Ah, oya! 🤖 Ó dàbí pé n kò lè dáhùn ìyẹn. Jọ̀wọ́, ẹ tún ìbéèrè yín ṣe? Mo ti ṣetán láti ran yín lọ́wọ́! 😊"
        elif language == "Igbo":
            return "Chai! 🤖 O dị ka enweghị m ike ịza ajụjụ ahụ. Biko, gbanwee ụzọ ị jụrụ ya? Adị m njikere inyere gị aka! 😊"
        elif language == "Hausa":
            return "Kash! 🤖 Da alama ban samu damar ba da amsa ba. Don Allah, sake faɗin tambayar taka? Ina shirye don taimaka maka! 😊"
        elif language == "Pidgin":
            return "Ah-ahn! 🤖 E be like say I no fit answer dat one. Abeg, try ask am anoda way? I ready to help you! 😊"
        else:
            return "🤖 FoodieBot couldn’t generate a reply. Try rephrasing your input."

import os
import google.generativeai as genai

# Configure the API key
genai.configure(api_key="AIzaSyBguZuCbadSdk2RU8QFaqtsNBlMr1jzOGg")

#output configurations
# Create the model
# See https://ai.google.dev/api/python/google/generativeai/GenerativeModel
generation_config = {
    "temperature": 0.4,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}



model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
    system_instruction=" your name is Gen Explorer.You was build by Vyshnavi.you should keep the thankyou at the end of the message.at the end of the message ask do you have any quires?"
)

chat_session = model.start_chat(
    history=[
    ]
)

while True:
    user_input = input("Enter your message (type 'stop' to end): ")
    if user_input.lower() == "stop":
        print("Stopping the chat session.")
        break

    response = chat_session.send_message(user_input)
    print("AI Response:", response.text)

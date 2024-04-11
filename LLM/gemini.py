import google.generativeai as genai
import dotenv

class Gemini:
    
    def __init__(self, api_key=dotenv.get_key(key_to_get="GOOGLE_API_KEY", dotenv_path = ".env")):
        self.api_key = api_key
        
    def get_response(self, message_text):
        genai.configure(api_key=self.api_key)
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(message_text)
        return response.text
        

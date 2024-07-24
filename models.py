# Import necessary libraries
from dotenv import load_dotenv
import os
import google.generativeai as genai
import streamlit as st


# Load environment variables from a .env file
load_dotenv()

# Processor class for handling text generation
class Processor():
    def __init__(self, API_KEY: str = None):
        # If API_KEY is not provided, attempt to retrieve it from environment variables
        if API_KEY is None:
            API_KEY = os.getenv("API_KEY")
            assert API_KEY is not None, "Cannot Load API key"
        
        # Configure the Generative AI with the provided API key
        genai.configure(api_key=API_KEY)
        
        # Initialize the Generative Model ('gemini-pro')
        self.model = genai.GenerativeModel('gemini-1.5-pro-latest')
        self.suggestionModel = genai.GenerativeModel('gemini-pro')

    def InsightGenerator(self, prompt: str, img):
         response = self.model.generate_content([prompt,img])
         with open("response.txt", "w") as text_file:
             text_file.write(response.text)
         return response.text
        

    def ChartGenerator(self,prompt:str,Query:str)-> str:
        response =self.suggestionModel.generate_content([prompt,Query])
        with open("suggestion.txt", "w") as text_file:
            text_file.write(response.text)
        return response.text
    

        

        

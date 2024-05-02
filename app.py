from dotenv import load_dotenv
from PIL import Image
import os
import google.generativeai as genai
import streamlit as st

load_dotenv()

key=os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=key)

for model in genai.list_models():
    if 'generateContent' in model.supported_generation_methods:
        print(model.name)

model=genai.GenerativeModel('gemini-pro-vision')

def get_gemini_response(input,image,user_prompt):
    response=model.generate_content([input, image[0], user_prompt])
    return response.text

def input_image_details(uploaded_file):
    if uploaded_file is not None:
        bytes_data=uploaded_file.getvalue()

        image_parts=[
            {
                'mime_type':uploaded_file.type,
                'data':bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError('No file uploaded')

st.set_page_config(page_title='MultiLanguage Invoice Extractor')

st.header('MultiLanguage Invoice Extractor :gemini:')
input=st.text_input('Input Prompt: ', key='input')
uploaded_file=st.file_uploader('Choose an image...', type=['jpg', 'jpeg', 'png'])

if uploaded_file is not None:
    image=Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

submit=st.button('Tell me about the invoice')

input_prompt="""
You are an expert in understanding invoices. You will receive input images as invoices and 
you will have to answer questions based on the input images.
"""

if submit:
    image_data=input_image_details(uploaded_file)
    response=get_gemini_response(input_prompt, image_data, input)
    st.subheader('The Response is')
    st.write(response)
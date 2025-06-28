#import openai
import streamlit as st
import google.generativeai as genai
#from google.generativeai.types import GenerationConfig

#Auth
#openai.api_key = st.secrets(["api_key"])
genai.configure(api_key=st.secrets["gemini_api_key"])

#Title
st.title("Chef Bot")
st.header("Getting you delicious food")

Instructions = st.text_area(
    "Tell me what you want to eat and I'll help you decide! : Breakfast, lunch or dinner"
)

if len(Instructions) <100:
    if st.button("Show Options"):
        """response = openai.completions.create(
            model = "text-davinchi-003",
            prompt = "Act like my personal chef and give me delicious food suggestion based on my following prompt: "+ Instructions,
            temperature =0,
            max_tokens = 100,
            stop = ["\n"]
        )
        output = response.choices[0].text"""
        model = genai.GenerativeModel("gemini-1.5-flash")
        prompt = f"Act like my personal chef and give me delicious food suggestion based on the following prompt: {Instructions}"
        response = model.generate_content(prompt,
                generation_config=genai.types.GenerationConfig(
                temperature=0.7,
                max_output_tokens=100
            ))
        st.info(response.text)

else:
    st.warning(
        "Input tto large, Write less than 100 words and try again"
    )
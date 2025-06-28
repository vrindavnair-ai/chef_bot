import openai
import streamlit as st

#Auth
openai.api_key = st.secrets(["api_key"])

#Title
st.title("Chef Bot")
st.header("Getting you delicious food")

Instructions = st.text_area(
    "Tell me what you want to eat and I'll help you decide! : Breakfast, lunch or dinner"
)

if len(Instructions) <100:
    if st.button("Show Options"):
        response = openai.completions.create(
            model = "text-davinchi-003",
            prompt = "Act like my personal chef and give me delicious food suggestion based on my following prompt: "+ Instructions,
            temperature =0,
            max_tokens = 100,
            stop = ["\n"]
        )
        output = response.choices[0].text
        st.info(output)

else:
    st.warning(
        "Input tto large, Write less than 100 words and try again"
    )
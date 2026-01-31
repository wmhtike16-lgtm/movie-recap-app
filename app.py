import streamlit as st
import google.generativeai as genai
import os

st.set_page_config(page_title="Movie Recap App")

st.title("🎬 Movie Recap App")

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")

st.write("YouTube transcript ကို အောက်မှာ paste လုပ်ပါ")

transcript = st.text_area(
    "Transcript",
    height=300,
    placeholder="ဒီမှာ YouTube transcript ကို paste လုပ်ပါ..."
)

if st.button("Generate Movie Recap"):
    if transcript.strip() == "":
        st.warning("Transcript မထည့်ရသေးပါ")
    else:
        with st.spinner("AI က စာရေးနေပါတယ်..."):
            prompt = f"""
မင်းက professional Movie Recap narrator ဖြစ်တယ်။
အောက်က YouTube transcript ကို
မြန်မာဘာသာနဲ့
စိတ်လှုပ်ရှားဖွယ် Movie Recap style နဲ့
ဇာတ်လမ်းပြောသလို ပြန်ရေးပါ။

Transcript:
{transcript}
"""
            response = model.generate_content(prompt)

            st.subheader("🎥 Movie Recap Script (Myanmar)")
            st.write(response.text)

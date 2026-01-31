import streamlit as st
import google.generativeai as genai
import os

# 🔑 API Key (Streamlit Secrets ကနေယူ)
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

st.set_page_config(page_title="Movie Recap App")
st.title("🎬 Movie Recap App")
st.write("YouTube transcript ကို အောက်မှာ paste လုပ်ပါ")

transcript = st.text_area(
    "Transcript",
    height=300,
    placeholder="ဒီမှာ YouTube transcript ကို paste လုပ်ပါ..."
)

if st.button("Generate Recap"):
    if transcript.strip() == "":
        st.warning("Transcript မထည့်ရသေးပါ")
    else:
        with st.spinner("AI စာရေးနေပါတယ်..."):
            try:
                model = genai.GenerativeModel("gemini-1.5-pro")

                prompt = f"""
You are a professional movie recap writer.
Rewrite the following transcript into an exciting,
storytelling Burmese (Myanmar) movie recap.

Transcript:
{transcript}
"""

                response = model.generate_content(prompt)
                st.success("ပြီးပါပြီ 🎉")
                st.write(response.text)

            except Exception as e:
                st.error(f"❌ AI မှာ အမှားဖြစ်နေပါတယ်\n\n{e}")

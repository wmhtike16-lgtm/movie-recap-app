import streamlit as st
import google.generativeai as genai
import os

st.set_page_config(page_title="Movie Recap App")

st.title("🎬 Movie Recap App")

# API KEY စစ်
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("❌ GEMINI_API_KEY မတွေ့ပါ။ GitHub Secrets မှာ မထည့်ရသေးပါ။")
    st.stop()

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-pro")

transcript = st.text_area(
    "YouTube Transcript",
    height=300,
    placeholder="ဒီမှာ YouTube transcript ကို paste လုပ်ပါ..."
)

if st.button("Generate Movie Recap"):
    if transcript.strip() == "":
        st.warning("Transcript မထည့်ရသေးပါ")
    else:
        try:
            with st.spinner("AI က စာရေးနေပါတယ်..."):
                prompt = f"""
မင်းက professional Movie Recap narrator ဖြစ်တယ်။
အောက်က transcript ကို
မြန်မာဘာသာနဲ့
စိတ်လှုပ်ရှားဖွယ် Movie Recap style နဲ့
ဇာတ်လမ်းပြောသလို ပြန်ရေးပါ။

Transcript:
{transcript}
"""
                response = model.generate_content(prompt)

            st.subheader("🎥 Movie Recap Script (Myanmar)")
            st.write(response.text)

        except Exception as e:
            st.error("❌ AI မှာ အမှားဖြစ်နေပါတယ်")
            st.code(str(e))

import streamlit as st
from openai import OpenAI
from gtts import gTTS
import tempfile
import os

# OpenAI client
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

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
                prompt = f"""
You are a professional movie recap writer.
Rewrite the following transcript into an exciting,
storytelling Burmese (Myanmar) movie recap.

Transcript:
{transcript}
"""

                response = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[
                        {"role": "user", "content": prompt}
                    ]
                )

                recap_text = response.choices[0].message.content
                st.success("ပြီးပါပြီ 🎉")
                st.write(recap_text)

                # Audio
                tts = gTTS(recap_text, lang="my")
                with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
                    tts.save(fp.name)
                    st.audio(fp.name)

            except Exception as e:
                st.error(f"❌ AI မှာ အမှားဖြစ်နေပါတယ်\n\n{e}")

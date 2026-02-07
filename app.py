import streamlit as st
from gtts import gTTS
import tempfile

st.set_page_config(page_title="Movie Recap App")

st.title("🎬 Movie Recap App (Free Version)")
st.write("YouTube transcript ကို အောက်မှာ paste လုပ်ပါ")

transcript = st.text_area(
    "Transcript",
    height=300,
    placeholder="ဒီမှာ YouTube transcript ကို paste လုပ်ပါ..."
)

def simple_burmese_recap(text):
    lines = text.split(".")
    recap = "ဒီရုပ်ရှင်က စတင်တာက အေးချမ်းတဲ့အခြေအနေတစ်ခုနဲ့ပါ။\n\n"

    for i, line in enumerate(lines[:5]):
        if line.strip():
            recap += f"နောက်တစ်ခါမှာတော့ {line.strip()} ဖြစ်လာပါတယ်။\n"

    recap += "\nနောက်ဆုံးမှာတော့ ဒီအဖြစ်အပျက်တွေက ဇာတ်လမ်းကို အရမ်းစိတ်ဝင်စားဖို့ကောင်းစေပါတယ်။"
    return recap

if st.button("Generate Recap"):
    if transcript.strip() == "":
        st.warning("Transcript မထည့်ရသေးပါ")
    else:
        with st.spinner("စာပြောင်းရေးနေပါတယ်..."):
            recap_text = simple_burmese_recap(transcript)
            st.success("ပြီးပါပြီ 🎉")
            st.write(recap_text)

            # Audio
            tts = gTTS(recap_text, lang="my")
            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
                tts.save(fp.name)
                st.audio(fp.name)

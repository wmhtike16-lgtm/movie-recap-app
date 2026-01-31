import streamlit as st

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
        st.warning("စာမထည့်ရသေးပါ")
    else:
        st.success("စာရပြီးပါပြီ 🎉")

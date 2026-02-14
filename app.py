import os
from dotenv import load_dotenv
import streamlit as st
from agents import creative_agent, regulation_agent, partner_support_agent

load_dotenv()

st.set_page_config(page_title="Valentine Copilot", page_icon="💝")
st.title("💝 Valentine Copilot (Multi-Agent)")

context = st.text_area(
    "Context (edit this to personalize)",
    value=("Wife: opera singer, ADHD, creative, recently growing her YouTube.\n"
           "Me: calm, yoga background, supportive.\n"
           "Goal: gentle, joyful Valentine’s day and a heartfelt gift."),
    height=140,
)

if st.button("Generate"):
    if not os.getenv("OPENAI_API_KEY"):
        st.error("Missing OPENAI_API_KEY. Add it to .env and restart.")
        st.stop()

    with st.spinner("Creating…"):
        c = creative_agent(context)
        r = regulation_agent(context)
        p = partner_support_agent(context)

    st.subheader("🎶 Creative Agent")
    st.write(c)

    st.subheader("🌿 Regulation Agent")
    st.write(r)

    st.subheader("🤝 Partner Support Agent")
    st.write(p)

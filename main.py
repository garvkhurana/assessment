import streamlit as st
from scraper import scrape_user_activity
from agent import generate_persona
import os
import pathlib
import traceback

st.title("Reddit User Persona Generator")

with st.sidebar:
    st.header("Credentials")
    reddit_username = st.text_input("Reddit Username (without /u/):")
    groq_api_key = st.text_input("Groq API Key:", type="password")
    client_id = st.text_input("Reddit Client ID:")
    client_secret = st.text_input("Reddit Client Secret:", type="password")
    generate = st.button("Generate Persona")

if generate:
    if reddit_username and groq_api_key and client_id and client_secret:
        os.environ["REDDIT_CLIENT_ID"] = client_id
        os.environ["REDDIT_CLIENT_SECRET"] = client_secret

        with st.spinner("Scraping Reddit and generating persona..."):
            try:
                st.info("Scraping Reddit...")
                user_data = scrape_user_activity(reddit_username)

                st.info("Generating persona...")
                persona_gen, _ = generate_persona(user_data, groq_api_key)

                if hasattr(persona_gen, "__iter__") and not isinstance(persona_gen, str):
                    persona = "".join(persona_gen)
                else:
                    persona = str(persona_gen)

                st.info("Saving file...")
                output_dir = pathlib.Path("output")
                output_dir.mkdir(exist_ok=True)

                output_path = output_dir / f"{reddit_username}_persona.txt"
                st.info(f"Output path: {output_path}")

                with open(output_path, "w", encoding="utf-8") as f:
                    f.write(persona)

                st.success(f"Persona created and saved to: {output_path}")
                st.download_button(
                    label="Download Persona Text",
                    data=persona,
                    file_name=f"{reddit_username}_persona.txt",
                    mime="text/plain"
                )
                st.text_area("Persona Output", value=persona, height=400)

            except Exception as e:
                st.error("Detailed Error Trace:")
                st.code(traceback.format_exc())
    else:
        st.error("Please fill in all fields in the sidebar.")

import streamlit as st
from scraper import scrape_user_activity
from agent import generate_persona
import os

st.title("Reddit User Persona Generator")


reddit_username = st.text_input("Enter Reddit username (without /u/):")
groq_api_key = st.text_input("Enter your Groq API Key:", type="password")
client_id = st.text_input("Reddit Client ID:")
client_secret = st.text_input(" Reddit Client Secret:", type="password")


if st.button("Generate Persona"):
    if reddit_username and groq_api_key and client_id and client_secret:
        os.environ["REDDIT_CLIENT_ID"] = client_id
        os.environ["REDDIT_CLIENT_SECRET"] = client_secret

        with st.spinner("Scraping Reddit and generating persona..."):
            try:
               
                user_data = scrape_user_activity(reddit_username)

                
                persona, _ = generate_persona(user_data, groq_api_key)

               
                os.makedirs("output", exist_ok=True)
                output_path = f"output/{reddit_username}_persona.txt"
                with open(output_path, "w", encoding="utf-8") as f:
                    f.write(persona)

                st.success(f"Persona created and saved to: {output_path}")
                st.download_button("⬇Download Persona Text", data=persona, file_name=f"{reddit_username}_persona.txt")
                st.text_area("Persona Output", value=persona, height=400)

            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.error("Please fill in all fields (username, keys, and client credentials).")

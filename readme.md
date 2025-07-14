# 🧠 Reddit User Persona Generator (LLM-powered)

This project scrapes a Reddit user's public posts and comments, then uses a Groq-hosted LLM (like LLaMA 3 or Mixtral) to generate a structured **User Persona** including traits, interests, writing style, and more.

Built using **Streamlit** for the frontend, **Phidata** for LLM orchestration, and **Groq API** for blazing-fast inference.

---

## 📌 Features

- 🔍 Input any Reddit username
- 📊 Scrapes their posts + comments
- 🧠 Generates structured persona using LLM
- 💾 Outputs as downloadable `.txt` file
- 🛡️ No API keys stored on backend — secure entry via sidebar


---

## 🛠️ Tech Stack

- [Streamlit] frontend UI
- [Phidata] agentic LLM backend
- [Groq API] LLM inference
- [PRAW] Reddit API wrapper

---

## 🔑 Requirements

You’ll need:

- A **Reddit app client ID and secret**
- A **Groq API key**
- Python 3.9+

---

## 🧾 1. Get Reddit API Credentials

1. Go to [https://www.reddit.com/prefs/apps](https://www.reddit.com/prefs/apps)
2. Scroll down to **“Developed Applications”** → click **Create App**
3. Choose **“script”**
4. Fill:
   - **Name**: anything (e.g., `PersonaApp`)
   - **Redirect URI**: `http://localhost:8501`
   - Click **Create App**
5. Copy:
   - `client_id` (below your app name)
   - `client_secret`

🔐 You'll enter these in the sidebar of the app.

---

## 🔑 2. Get Groq API Key

1. Sign up at [https://console.groq.com/](https://console.groq.com/)
2. Go to [https://console.groq.com/keys](https://console.groq.com/keys)
3. Click **Create API Key**
4. Copy your key — keep it private

📌 Models available:
- `mixtral-8x7b-32768`
- `llama3-8b-8192`
- `llama3-70b-4096`

---

## 🧰 3. Installation

Clone this repo:

bash
git clone https://github.com/garvkhurana/assessment
cd assesment

Install dependencies:
pip install -r requirements.txt

🧪 4. Run the App
streamlit run app.py

You'll see the sidebar with inputs for:

Reddit username
Groq API key
Reddit client ID
Reddit client secret

Then click Generate Persona.

🐳 Optional: Run in Docker
Build the image:
docker build -t reddit-persona .

Run the container:
docker run -p 8501:8501 reddit-persona
Then open: http://localhost:8501

📁 Project Structure
├── agent.py          # LLM persona builder using phidata + Groq
├── app.py            # Streamlit app (main UI)
├── scraper.py        # Reddit post/comment scraper (PRAW)
├── requirements.txt  # All dependencies
├── dockerfile        # Docker build config
└── output/           # Saved persona files

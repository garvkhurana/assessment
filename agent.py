from phi.assistant import Assistant
from phi.model.groq import Groq

from phi.tools.python import PythonTools

def generate_persona(user_data, groq_api_key):
    llm = Groq(api_key=groq_api_key, model="mixtral-8x7b-32768")

    content = ""
    for post in user_data["posts"]:
        content += f"POST: {post['title']}\n{post['body']}\nURL: {post['url']}\n\n"
    for comment in user_data["comments"]:
        content += f"COMMENT: {comment['body']}\nLink: {comment['link']}\n\n"

    prompt = f"""
You are an expert persona analyst.
For each trait (e.g., Interests, Tone, Writing Style, Behavior):
- Name the trait.
- Give a short description.
- Cite the post/comment URL used for inference.

Reddit User Activity:
{content}

Now build the user persona.
"""

    agent = Assistant(llm=llm, tools=[PythonTools()])
    response = agent.run(prompt)
    return response, []
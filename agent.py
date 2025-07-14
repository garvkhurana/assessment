from phi.assistant import Assistant
from phi.llm.groq import Groq  
from phi.tools.python import PythonTools

def generate_persona(user_data, groq_api_key):
    try:
        llm = Groq(api_key=groq_api_key, model="llama3-70b-8192")

        if not user_data["posts"] and not user_data["comments"]:
            return "No posts or comments found for this user. Unable to generate persona.", []

        content = ""
        
        
        if user_data["posts"]:
            content += "=== POSTS ===\n"
            for i, post in enumerate(user_data["posts"][:20], 1): 
                content += f"POST {i}:\n"
                content += f"Title: {post['title']}\n"
                if post['body']:
                    content += f"Body: {post['body']}\n"
                content += f"Subreddit: {post.get('subreddit', 'N/A')}\n"
                content += f"Score: {post.get('score', 'N/A')}\n"
                content += f"URL: {post['url']}\n\n"

        
        if user_data["comments"]:
            content += "=== COMMENTS ===\n"
            for i, comment in enumerate(user_data["comments"][:30], 1):  
                content += f"COMMENT {i}:\n"
                content += f"Body: {comment['body']}\n"
                content += f"Subreddit: {comment.get('subreddit', 'N/A')}\n"
                content += f"Score: {comment.get('score', 'N/A')}\n"
                content += f"Link: {comment['link']}\n\n"

        prompt = f"""
You are an expert persona analyst. Analyze the following Reddit user activity and create a comprehensive persona.

For each trait category, provide:
- **Trait Name**: Clear category name
- **Description**: Detailed analysis (2-3 sentences)
- **Evidence**: Specific examples from posts/comments with references

Categories to analyze:
1. **Core Interests & Hobbies**
2. **Communication Style & Tone**
3. **Values & Beliefs**
4. **Behavioral Patterns**
5. **Expertise Areas**
6. **Social Interaction Style**
7. **Personality Traits**

Reddit User: {user_data['username']}

Reddit Activity Data:
{content}

Please provide a structured analysis with clear evidence backing each conclusion.
"""

        agent = Assistant(llm=llm, tools=[PythonTools()])
        response = agent.run(prompt)
        return response, []
    
    except Exception as e:
        return f"Error generating persona: {str(e)}", []
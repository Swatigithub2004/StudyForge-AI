from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os
import json

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0.3
)


def analyze_resume_ai(resume_text):

    prompt = f"""
Analyze the following resume and return ONLY raw JSON.
Do not use markdown.

Format:

{{
    "score":75,
    "summary":"short summary",
    "strengths":["item1","item2"],
    "missing_skills":["item1","item2"],
    "weaknesses":["item1","item2"]
}}

Resume:

{resume_text}
"""

    try:

        response = llm.invoke(prompt)

        clean_response = response.content
        clean_response = clean_response.replace("```json","")
        clean_response = clean_response.replace("```","")
        clean_response = clean_response.strip()

        result = json.loads(clean_response)

        return result


    except Exception as e:

        print("AI Error:", e)

        return {

    "score":0,

    "summary":"AI service unavailable right now.",

    "strengths":[],

    "missing_skills":[],

    "weaknesses":[
        "Gemini API quota exceeded"
    ]
}
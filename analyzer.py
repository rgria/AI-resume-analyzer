import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyze_resume(resume, job):

    prompt = f"""
    Compare this resume to the job description.

    Resume:
    {resume}

    Job Description:
    {job}

    Provide:
    1. Skill gaps
    2. Suggestions for improvement
    3. Resume keywords to add
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role":"user","content":prompt}]
    )

    return response.choices[0].message.content

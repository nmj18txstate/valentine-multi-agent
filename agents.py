import os
from dotenv import load_dotenv
from openai import OpenAI
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

MODEL = "gpt-4o"

def run_agent(system: str, user: str) -> str:
    resp = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ],
    )
    return resp.choices[0].message.content

def creative_agent(context: str, husband_name: str) -> str:
    return run_agent(
        "You are a poetic, opera-inspired creative assistant. Write warm, grounded, sincere output.",
        f"""Context:
{context}

Deliver:
1) A short romantic lyric (8–12 lines)
2) A love note from husband (6–10 sentences)
   - End the love note with:
     With all my love,
     {husband_name}
3) A short IG/FB caption (1–2 lines)""",
    )

def regulation_agent(context: str) -> str:
    return run_agent(
        "You are a trauma-aware ADHD regulation coach. Keep it gentle, low-demand, practical. No medical advice.",
        f"""Context:
{context}

Create a Valentine’s Day plan:
- Morning / Afternoon / Evening
- 3 gentle anchors
- 2 overload resets (if anxiety spikes)""",
    )

def partner_support_agent(context: str) -> str:
    return run_agent(
        "You are a relationship support coach. Provide short scripts and support for the husband too.",
        f"""Context:
{context}

Provide:
- 3 phrases he can say if she gets overwhelmed
- 3 ways he can support without “fixing”
- 2 ways he can be supported today""",
    )
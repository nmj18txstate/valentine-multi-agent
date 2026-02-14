# 💝 Valentine Copilot (Multi-Agent Streamlit App)
A lightweight multi-agent AI application built with **Streamlit + OpenAI**, designed to generate:
- 🎶 Romantic lyrics & heartfelt love notes  
- 🌿 Trauma-aware ADHD-friendly Valentine plans  
- 🤝 Partner support scripts and relationship guidance  

This project demonstrates a simple **multi-agent orchestration pattern** using specialized AI roles.
---
## Features
# 🎶 Creative Agent
- Generates romantic opera-inspired lyrics
- Writes a personalized love note (with dynamic name signature)
- Creates short IG/FB captions

# 🌿 Regulation Agent
- Designs a gentle Valentine’s Day plan
- Provides overload resets
- Uses trauma-aware, low-demand language

# 🤝 Partner Support Agent
- Short supportive scripts
- Non-fixing emotional support strategies
- Support ideas for the husband as well
---
# 🏗 Architecture
Streamlit UI -> App Layer (app.py) -> Specialized Agents (agents.py) -> OpenAI GPT-4o Model

Each agent has:
- A distinct system prompt
- A clear behavioral role
- Context-aware generation
---
## ⚙️ Setup
# 1. Clone the Repository
git clone https://github.com/your-username/valentine-multi-agent.git
cd valentine-multi-agent

# 2️. Create Virtual Environment
python -m venv .venv
.venv\Scripts\activate   # Windows

# 3.Install Dependencies
pip install -r requirements.txt

# 4️. Add Environment Variables
Create a .env file:
OPENAI_API_KEY=your_key_here

# 5️. Run Locally
streamlit run app.py

🌍 Deployment
This app is deployable on:
Streamlit Community Cloud
Docker (future enhancement)
Cloud platforms (AWS / GCP / Azure)

🔮 Future Roadmap
This project currently uses a simple role-based orchestration model.
Future enhancements may include:
🧠 ADK (Agent Development Kit)
Structured agent lifecycle management
Tool integration
Memory persistence
Observability & tracing

🔁 A2A (Agent-to-Agent Communication)
Agents collaborating directly
Context sharing across agents
Task delegation patterns
Multi-step reasoning workflows

🔗 MCP (Model Context Protocol)
External knowledge injection
Context streaming
Tool and data connectors
Structured system prompt governance

📦 Additional Enhancements
Persistent memory per user
PDF export of love note
Structured section rendering
Emotional tone sliders
Prompt templates

# SupportFlow AI 🤖

A Multi-Agent Customer Support Triage System built using LangGraph.

---

## 📌 Overview

SupportFlow AI is a multi-agent system designed to automate the triaging of customer support tickets.  
It processes user queries through a sequence of specialized agents to extract insights, classify issues, determine urgency, and generate appropriate responses.

---

## 🧠 System Architecture

The system consists of four agents:

1. **Intake Agent**
   - Extracts structured information from user input
   - Identifies issue summary and sentiment

2. **Classification Agent**
   - Categorizes the issue (Billing, Technical, Refund, etc.)

3. **Priority Agent**
   - Determines urgency level (Low, Medium, High, Critical)

4. **Resolution Agent**
   - Suggests next action
   - Generates a response for the customer

---

### 🔄 Workflow

```

User Input
↓
Intake Agent
↓
Classification Agent
↓
Priority Agent
↓
Resolution Agent
↓
Final Output

```

---

## 🛠️ Tools Used

- Python 3.12
- LangGraph
- LangChain
- OpenAI API
- python-dotenv

---

## 📂 Project Structure

```

supportflow-ai/
│
├── agents/                # Individual agent implementations
├── tools/                 # Tool functions (KB lookup, escalation rules)
├── main.py                # Entry point
├── nodes.py               # LangGraph node definitions
├── state.py               # Shared state across agents
├── prompts.py             # Agent prompts
├── utils.py               # Helper functions
├── demo_log.txt           # Sample execution logs
├── requirements.txt
├── .env

````

---

## ⚙️ Setup Instructions

### 🔹 Prerequisite

Ensure `uv` is installed:  
https://docs.astral.sh/uv/


### 🔹 Step 1: Clone the Repository

```bash
git clone https://github.com/arshisaxena26/Multi-Agent-Assignment.git
cd supportflow-ai
````

### 🔹 Step 2: Install Dependencies

```bash
uv sync
```
---

### 🔑 Environment Variables

Create a `.env` file in the root directory:

```
OPENAI_API_KEY=your_api_key_here
```

---

### ▶️ Run the Application

```bash
uv run python main.py
```

---

## 🧪 Example Input

```
"I was charged twice for my order and need a refund urgently."
```

---

## 📤 Example Output

```json
{
  "issue_summary": "Customer was charged twice",
  "category": "Refund Request",
  "priority": "High",
  "recommended_action": "Escalate to billing team",
  "draft_reply": "We’re sorry for the inconvenience. Your case has been prioritized..."
}
```

---

## 📊 Demo & Logs

Sample execution logs are available in `demo_log.txt`
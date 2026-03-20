from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage

from prompts import INTAKE_PROMPT
from utils import extract_json
from state import State


llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)


def run_intake_agent(state: State) -> State:
    response = llm.invoke([
        SystemMessage(content=INTAKE_PROMPT),
        HumanMessage(content=state["ticket_text"])
    ])

    data = extract_json(response.content)

    state["customer_name"] = data.get("customer_name", "Unknown")
    state["issue_summary"] = data.get("issue_summary", "")
    state["sentiment"] = data.get("sentiment", "calm")
    state["history"].append("Intake Agent extracted customer_name, issue_summary, and sentiment.")

    return state
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage

from prompts import PRIORITY_PROMPT
from utils import extract_json
from state import State


llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)


def run_priority_agent(state: State) -> State:
    input_text = f"""
Ticket text: {state["ticket_text"]}
Issue summary: {state["issue_summary"]}
Category: {state["category"]}
Sentiment: {state["sentiment"]}
"""

    response = llm.invoke([
        SystemMessage(content=PRIORITY_PROMPT),
        HumanMessage(content=input_text)
    ])

    data = extract_json(response.content)

    state["priority"] = data.get("priority", "Medium")
    state["priority_reason"] = data.get("reason", "No reason provided.")
    state["history"].append(
        f'Priority Agent set priority = {state["priority"]}. Reason: {state["priority_reason"]}'
    )

    return state
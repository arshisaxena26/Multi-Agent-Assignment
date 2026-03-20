from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage

from prompts import CLASSIFICATION_PROMPT
from utils import extract_json
from state import State


llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)


def run_classification_agent(state: State) -> State:
    input_text = f"""
Ticket text: {state["ticket_text"]}
Issue summary: {state["issue_summary"]}
Sentiment: {state["sentiment"]}
"""

    response = llm.invoke([
        SystemMessage(content=CLASSIFICATION_PROMPT),
        HumanMessage(content=input_text)
    ])

    data = extract_json(response.content)

    state["category"] = data.get("category", "General Inquiry")
    state["history"].append(f'Classification Agent set category = {state["category"]}.')

    return state
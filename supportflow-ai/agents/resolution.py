from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage

from prompts import RESOLUTION_PROMPT
from utils import extract_json
from state import State
from tools.kb_tool import lookup_kb
from tools.escalation_tool import check_escalation


llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)


def run_resolution_agent(state: State) -> State:
    kb_guidance = lookup_kb(state["category"])
    escalation_decision = check_escalation(state["category"], state["priority"])

    state["kb_guidance"] = kb_guidance
    state["escalation_decision"] = escalation_decision

    input_text = f"""
Ticket text: {state["ticket_text"]}
Issue summary: {state["issue_summary"]}
Category: {state["category"]}
Priority: {state["priority"]}
Priority reason: {state["priority_reason"]}

Knowledge base guidance:
{kb_guidance}

Escalation decision:
{escalation_decision}
"""

    response = llm.invoke([
        SystemMessage(content=RESOLUTION_PROMPT),
        HumanMessage(content=input_text)
    ])

    data = extract_json(response.content)

    state["recommended_action"] = data.get("recommended_action", escalation_decision)
    state["draft_reply"] = data.get("draft_reply", "Thank you for contacting support.")
    state["history"].append(
        "Resolution Agent generated recommended_action and draft_reply using KB and escalation tools."
    )

    return state
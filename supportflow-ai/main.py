from langgraph.graph import StateGraph, END

from state import State
from nodes import (
    intake_node,
    classification_node,
    priority_node,
    resolution_node,
)


def build_graph():
    graph = StateGraph(State)

    # Add nodes
    graph.add_node("intake", intake_node)
    graph.add_node("classification", classification_node)
    graph.add_node("priority", priority_node)
    graph.add_node("resolution", resolution_node)

    # Define flow (pipeline)
    graph.set_entry_point("intake")

    graph.add_edge("intake", "classification")
    graph.add_edge("classification", "priority")
    graph.add_edge("priority", "resolution")
    graph.add_edge("resolution", END)

    return graph.compile()


def main():
    app = build_graph()

    print("\n=== SupportFlow AI ===\n")

    ticket = input("Enter your support request:\n> ")

    # Initial state
    initial_state = {
        "ticket_text": ticket,
        "customer_name": None,
        "issue_summary": None,
        "sentiment": None,
        "category": None,
        "priority": None,
        "priority_reason": None,
        "kb_guidance": None,
        "escalation_decision": None,
        "recommended_action": None,
        "draft_reply": None,
        "history": [],
    }

    # Run the graph
    final_state = app.invoke(initial_state)

    print("\n=== Final Output ===\n")
    print(f"Customer Name: {final_state['customer_name']}")
    print(f"Issue Summary: {final_state['issue_summary']}")
    print(f"Category: {final_state['category']}")
    print(f"Priority: {final_state['priority']}")
    print(f"Recommended Action: {final_state['recommended_action']}")
    print(f"Reply:\n{final_state['draft_reply']}")

    print("\n=== Execution Trace ===")
    for step in final_state["history"]:
        print(f"- {step}")


if __name__ == "__main__":
    main()
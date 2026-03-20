from typing import TypedDict, Optional


class State(TypedDict):
    """
    Shared state across all agents in the SupportFlow AI system.
    """

    # Original user input
    ticket_text: str

    # Extracted by Intake Agent
    customer_name: Optional[str]
    issue_summary: Optional[str]
    sentiment: Optional[str]

    # Set by Classification Agent
    category: Optional[str]

    # Set by Priority Agent
    priority: Optional[str]
    priority_reason: Optional[str]

    # Set by Resolution Agent
    recommended_action: Optional[str]
    draft_reply: Optional[str]
    kb_guidance: Optional[str]
    escalation_decision: Optional[str]

    # Debug / tracking
    history: list[str]
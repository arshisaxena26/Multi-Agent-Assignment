from state import State

from agents.intake import run_intake_agent
from agents.classification import run_classification_agent
from agents.priority import run_priority_agent
from agents.resolution import run_resolution_agent


def intake_node(state: State) -> State:
    return run_intake_agent(state)


def classification_node(state: State) -> State:
    return run_classification_agent(state)


def priority_node(state: State) -> State:
    return run_priority_agent(state)


def resolution_node(state: State) -> State:
    return run_resolution_agent(state)
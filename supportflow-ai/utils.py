import json


def extract_json(content: str) -> dict:
    """
    Safely parse JSON returned by the LLM.
    """
    try:
        return json.loads(content)
    except json.JSONDecodeError:
        raise ValueError(f"Invalid JSON returned by model: {content}")
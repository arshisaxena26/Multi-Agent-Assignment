def check_escalation(category: str, priority: str) -> str:
    if priority == "Critical":
        return "Escalate immediately to senior support team"

    if priority == "High":
        if category in ["Billing", "Refund Request", "Technical Issue", "Account Access"]:
            return f"Escalate to {category} support team"
        return "Escalate to general support team"

    if priority == "Medium":
        return "Handle in standard support queue"

    return "Respond with standard reply without escalation"
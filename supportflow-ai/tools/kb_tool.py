def lookup_kb(category: str) -> str:
    kb = {
        "Billing": "Ask the customer to verify billing details and check payment confirmation. Escalate billing-related charge issues if duplicate payment is suspected.",
        "Technical Issue": "Ask for device, browser/app version, screenshot, and exact error message before escalation.",
        "Account Access": "Guide the customer through password reset and verify whether multi-factor authentication is blocking access.",
        "Refund Request": "Ask for order ID, payment method, and reason for refund. Refunds with duplicate charges should be escalated to billing.",
        "General Inquiry": "Provide a standard informational response and direct the customer to help center resources if needed.",
    }

    return kb.get(category, "No knowledge base article found for this category.")
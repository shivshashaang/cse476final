"""Your Chain-of-Thought technique goes here."""

from api import call_model_chat_completions


def answer_with_chain_of_thought(question: str) -> str:
    prompt = f"""Solve this step by step.

Question:
{question}

After thinking, reply with only the final answer.
"""
    result = call_model_chat_completions(prompt, temperature=0.0)
    return (result.get("text") or "").strip()


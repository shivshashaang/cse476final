"""Your Few-Shot Prompting technique goes here."""

from api import call_model_chat_completions


def answer_with_few_shot(question: str) -> str:
    prompt = f"""Answer the final question. Reply with only the final answer.

Example 1:
Question: What is 2 + 2?
Answer: 4

Example 2:
Question: In a race, you pass the person in second place. What place are you in?
Answer: second

Final question:
{question}
"""
    result = call_model_chat_completions(prompt, temperature=0.0)
    return (result.get("text") or "").strip()


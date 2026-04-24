"""Your Self-Consistency technique goes here."""

from collections import Counter

from api import call_model_chat_completions


def answer_with_self_consistency(question: str) -> str:
    answers = []
    for _ in range(3):
        result = call_model_chat_completions(
            question,
            system="Solve carefully. Reply with only the final answer.",
            temperature=0.7,
        )
        answers.append((result.get("text") or "").strip())

    return Counter(answers).most_common(1)[0][0]


"""Shared agent router. Teammates connect their techniques here."""

from techniques.chain_of_thought import answer_with_chain_of_thought
from techniques.few_shot import answer_with_few_shot
from techniques.self_consistency import answer_with_self_consistency


def answer_question(question: str) -> str:
    # Start simple. Later, route by domain or difficulty.
    if any(word in question.lower() for word in ["calculate", "solve", "math", "$"]):
        return answer_with_chain_of_thought(question)
    return answer_with_few_shot(question)


def answer_question_careful(question: str) -> str:
    return answer_with_self_consistency(question)


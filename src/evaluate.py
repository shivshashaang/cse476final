"""Practice-data evaluation helpers adapted from the course tutorial notebook."""

import json
import re
import time
from pathlib import Path

from api import MODEL, call_model_chat_completions
from agent import answer_question


def normalize_text(s: str) -> str:
    s = (s or "").strip().lower()
    s = re.sub(r"[^\w\s\-']", " ", s)
    s = re.sub(r"\s+", " ", s).strip()

    synonyms = {
        "unchanged": "stay the same",
        "no change": "stay the same",
        "same": "stay the same",
        "second place": "second",
        "2nd": "second",
        "first place": "first",
        "third place": "third",
    }
    return synonyms.get(s, s)


def extract_number(s: str):
    if not s:
        return None
    match = re.search(r"[-+]?\d+(\.\d+)?", s)
    return match.group(0) if match else None


def grade(expected: str, got: str, kind: str = "text") -> bool:
    if kind == "numeric":
        exp_num = extract_number(expected)
        got_num = extract_number(got)
        return (exp_num is not None) and (got_num == exp_num)
    return normalize_text(got) == normalize_text(expected)


def guess_kind(expected: str) -> str:
    return "numeric" if extract_number(expected) == normalize_text(expected) else "text"


def self_evaluate(question, prediction, expected_answer, model=MODEL):
    system = "You are a strict grader. Reply with exactly True or False. No punctuation. No explanation."
    prompt = f"""You are grading a question-answer pair.

Return exactly True if the PREDICTION would be accepted as correct for the EXPECTED_ANSWER.
Otherwise, return False.

QUESTION:
{question}

PREDICTION:
{prediction}

EXPECTED_ANSWER:
{expected_answer}

Answer with exactly: True or False
"""
    r = call_model_chat_completions(prompt, system=system, model=model, temperature=0.0)
    reply = (r.get("text") or "").strip().lower()
    if reply.startswith("true"):
        return True
    if reply.startswith("false"):
        return False
    return normalize_text(prediction) == normalize_text(expected_answer)


def evaluate_dev_data(path: Path = Path("data/dev_data.json"), limit: int = 25):
    data = json.loads(path.read_text())
    rows = []
    for item in data[:limit]:
        question = item["input"]
        expected = item["output"]
        got = answer_question(question)
        rows.append({
            "expected": expected,
            "got": got,
            "correct": grade(expected, got, guess_kind(expected)),
            "domain": item.get("domain"),
        })
        time.sleep(0.2)

    correct = sum(1 for row in rows if row["correct"])
    print(f"Score: {correct}/{len(rows)} correct")
    return rows


if __name__ == "__main__":
    evaluate_dev_data()


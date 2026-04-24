"""Run final test data and write the required answers JSON file."""

import json
from pathlib import Path

from agent import answer_question


INPUT_PATH = Path("data/test_data.json")
OUTPUT_PATH = Path("outputs/cse_476_final_project_answers.json")


def load_questions(path: Path):
    data = json.loads(path.read_text())
    if not isinstance(data, list):
        raise ValueError("Input file must contain a list of question objects.")
    return data


def build_answers(questions):
    answers = []
    for question in questions:
        answers.append({"output": answer_question(question["input"])})
    return answers


def validate_results(questions, answers):
    if len(questions) != len(answers):
        raise ValueError(f"Mismatched lengths: {len(questions)} questions vs {len(answers)} answers.")
    for idx, answer in enumerate(answers):
        if "output" not in answer:
            raise ValueError(f"Missing output field for answer index {idx}.")
        if not isinstance(answer["output"], str):
            raise TypeError(f"Answer at index {idx} has non-string output: {type(answer['output'])}")
        if len(answer["output"]) >= 5000:
            raise ValueError(f"Answer at index {idx} exceeds 5000 characters.")


def main():
    questions = load_questions(INPUT_PATH)
    answers = build_answers(questions)
    validate_results(questions, answers)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(json.dumps(answers, ensure_ascii=False, indent=2))
    print(f"Wrote {len(answers)} answers to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()


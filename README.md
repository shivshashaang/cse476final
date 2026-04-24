# CSE 476 Final Project

Runnable repo for the final project agent.

## Setup

1. Connect to ASU VPN.
2. Copy `.env.example` to `.env`.
3. Put your ASU API key in `.env`.
4. Install requirements:

```bash
pip install -r requirements.txt
```

## Files

- `src/api.py`: ASU API call code adapted from the course tutorial.
- `src/evaluate.py`: practice-data grading helpers adapted from the course tutorial.
- `src/agent.py`: one place that chooses which technique answers a question.
- `src/main.py`: runs final test questions and writes answer JSON.
- `src/techniques/`: each teammate puts technique code here.

## Your Three Techniques

- `src/techniques/few_shot.py`
- `src/techniques/chain_of_thought.py`
- `src/techniques/self_consistency.py`

Each technique should take a question string and return one final answer string.


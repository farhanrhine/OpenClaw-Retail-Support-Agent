import json
import os


BASE_DIR = os.path.dirname(__file__)
POLICY_FILE = os.path.join(BASE_DIR, "../data/policy.txt")


def load_policy():
    with open(POLICY_FILE, "r", encoding="utf-8") as f:
        return f.read()


if __name__ == "__main__":

    policy_text = load_policy()

    output = {
        "policy": policy_text
    }

    print(json.dumps(output))
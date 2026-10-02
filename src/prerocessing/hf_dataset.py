import json


DEFAULT_SYSTEM_PROMPT = (
    "You are an AI assistant for Wordpress."
    " You should help the user to answer their questions."
)


def create_dataset(question, answer):
    return {
        "messages": [
            {"role": "system", "content": DEFAULT_SYSTEM_PROMPT},
            {"role": "user", "content": question},
            {"role": "assistant", "content": answer},
        ]
    }


if __name__ == "__main__":
    df = json.loads(open("data/wordpress_faq.json", encoding="utf8").read())
    with open("data/train.jsonl", "w") as f:
        for i in range(len(df)):
            example_str = json.dumps(
                create_dataset(df[str(i)]["question"], df[str(i)]["answer"])
            )
            f.write(example_str + "\n")

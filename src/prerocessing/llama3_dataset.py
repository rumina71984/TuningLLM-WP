from datasets import Dataset
import json


df = json.loads(open("data/wordpress_faq.json", encoding="utf8").read())

TEMPLATE = """<|begin_of_text|><|start_header_id|>system<|end_header_id|>

{context}<|eot_id|><|start_header_id|>user<|end_header_id|>

{question}<|eot_id|><|start_header_id|>assistant<|end_header_id|>

{answer}<|eot_id|>"""

DEFAULT_SYSTEM_PROMPT = (
    "You are an AI assistant for Wordpress."
    " You should help the user to answer their questions."
)

data = []
for i in range(len(df)):
    data.append(
        {
            "text": TEMPLATE.format(
                context=DEFAULT_SYSTEM_PROMPT,
                question=df[str(i)]["question"],
                answer=df[str(i)]["answer"],
            )
        }
    )

my_dataset = Dataset.from_list(data)
my_dataset.push_to_hub("aminvilan2/wordpress-qa-llama3")

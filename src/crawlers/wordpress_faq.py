from bs4 import BeautifulSoup
import requests
import os
import json


# Define Function
def save_json(path, name, data):
    os.makedirs(path, exist_ok=True)
    with open(path + name, "w", encoding="utf8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

    return True


url = "https://www.wpexplorer.com/faq-wordpress/"
headers = {"User-Agent": "Mozilla/5.0"}
print("=" * 80, "Start crawling URL:", url, "=" * 60, sep="\n")

response = requests.get(url, headers=headers)
response.raise_for_status()
soup = BeautifulSoup(response.text, "html.parser")

faq_data = {}
questions = soup.find_all("h3")
print(f"Number of questions: {len(questions)}", "-" * 40, sep="\n")

for i in range(len(questions)):
    question_text = questions[i].get_text(strip=True)
    answers = []
    print(f"Questions number {i}:", question_text, "-" * 40, sep="\n")

    sibling = questions[i].find_next_sibling()
    while sibling:
        if sibling.name == "p":
            answers.append(sibling.get_text(strip=True))
        elif sibling.name == "h3":
            break
        sibling = sibling.find_next_sibling()

    if answers:
        faq_data[i] = {"question": question_text, "answer": " ".join(answers)}
    else:
        print("Answer was not found!", "=" * 40, sep="\n")

print(
    "=" * 80, "Data crawled and saved successfully.", "=" * 80, sep="\n"
) if save_json("data/", "wordpress_faq.json", faq_data) else print(
    "=" * 80, "An error occurred while saving data!", "=" * 80, sep="\n"
)

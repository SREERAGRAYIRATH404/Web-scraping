import requests
from bs4 import BeautifulSoup
word = input("Enter a word: ")
url = f"https://www.dictionary.com/browse/{word}"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
definition = soup.find("div", {"class": "css-1ghs5zt e1q3nk1v3"})
if definition:
    meaning = definition.text.strip()
    print(f"The meaning of '{word}' is: {meaning}")
else:
    print(f"No definition found for '{word}'")

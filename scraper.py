import requests
from bs4 import BeautifulSoup

# https://www.meetup.com/find/?source=GROUPS&keywords=Women%20Programmers&distance=twentyFiveMiles&location=us--ca--Emeryville

# Making a GET request
r = requests.get(
    "https://www.meetup.com/find/?source=GROUPS&keywords=Women%20Programmers&distance=twentyFiveMiles&location=us--ca--Emeryville"
)

soup = BeautifulSoup(r.content, "html.parser")
s = soup.find_all(attrs={"data-testid": "group-card-title"})
for group in s:
    print(group)
    # print(group.find_next_sibling("div"))

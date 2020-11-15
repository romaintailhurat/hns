"""
- first, authentication is needed, the page is not public
"""
import requests
import json
from bs4 import BeautifulSoup

HN_URL = "https://news.ycombinator.com/"
LOGIN_URL = "https://news.ycombinator.com/login"
UPVOTED_URL = "https://news.ycombinator.com/upvoted?id=romaintailhurat"
ID = None
PASSWORD = None

test = requests.get("https://news.ycombinator.com/")

if test.ok:
    print("Hacker news reachable")
else:
    print("Hacker news seems unreachable")
    exit()

with open("secrets.json") as sf:
    secrets = json.load(sf)
    ID = secrets["user"]
    PASSWORD = secrets["password"]

resp_login = requests.post(LOGIN_URL, data={"acct": ID, "pw": PASSWORD})

resp_302 = resp_login.history[0]
user_cookie = resp_302.cookies["user"]

req_cookies = requests.cookies.RequestsCookieJar()
req_cookies.set("user", user_cookie)


more = True
upvote_path = "upvoted?id=romaintailhurat"

stories = []

while more:
    target = f"{HN_URL}{upvote_path}"
    resp_upvoted = requests.get(target, cookies=req_cookies)
    html = BeautifulSoup(resp_upvoted.text, "html.parser")
    storylinks = html.find_all("a", class_="storylink")
    stories = stories + storylinks
    morelink = html.find_all("a", class_="morelink")
    if morelink == []:
        more = False
    else:
        upvote_path = morelink[0]["href"]

data = {}

for idx, story in enumerate(stories):
    data[idx] = {"text": story.text, "link": story["href"]}

with open("stories.json", "w") as f:
    json.dump(data, f)
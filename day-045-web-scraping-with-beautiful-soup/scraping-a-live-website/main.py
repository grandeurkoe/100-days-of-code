from bs4 import BeautifulSoup
import requests

all_articles = []
upvotes_all = []
upvote_index = 0
max_upvotes = 0
max_index = 0

# Get the contents of the ycombinator website using requests.
ycombinator_response = requests.get(url="https://news.ycombinator.com/news")
ycombinator_response.raise_for_status()
ycombinator_content = ycombinator_response.text

# Parse the ycombinator_content using BeautifulSoup.
ycombinator_soup = BeautifulSoup(ycombinator_content, "html.parser")
title = ycombinator_soup.select(selector=".titleline a")

upvotes = ycombinator_soup.select(selector=".subtext")
for upvote in upvotes:
    upvote_content = upvote.select_one(selector=".score")
    if upvote_content is None:
        upvotes_all.append(0)
    else:
        upvotes_all.append(int(upvote_content.get_text().split(" ")[0]))

# Store the title, link and upvote in a dictionary.
# Each dictionary entry is an article and every dictionary entry is stored in an all_articles array.
for title_index in range(0, len(title), +2):
    content = {
        'title': title[title_index].get_text(),
        'link': title[title_index].get("href"),
        'upvotes': upvotes_all[upvote_index]
    }
    all_articles += [content]
    upvote_index += 1

# Find the article with the most upvotes.
for article_index in range(len(all_articles)):
    if all_articles[article_index]['upvotes'] > max_upvotes:
        max_upvotes = all_articles[article_index]['upvotes']
        max_index = article_index

# Print the top article on ycombinator.
print(f"Top Article - \n"
      f"Title: {all_articles[max_index]['title']}\n"
      f"Link: {all_articles[max_index]['link']}\n"
      f"Upvotes: {all_articles[max_index]['upvotes']}")

import requests
from send_email import send_email

search_topic = "tesla"
api_key = '2910116ee77c40b0a0d87c348e893a14'
url = "https://newsapi.org/v2/everything?" \
      f"q={search_topic}&" \
      "sortBy=publishedAt&" \
      "apiKey=2910116ee77c40b0a0d87c348e893a14&" \
      "language=en"

# "from=2023-07-25&" \

# Make request to get data
request = requests.get(url)

# create a dictionary with the data
content = request.json()

# create a string email message
message = """\
Subject: Daily news scrape about tesla

From your kind self

"""

# iterate over articles and check for encoding errors, non ascii doesn't work for some reason
for index, article in enumerate(content["articles"][:20]):
    article_title = article["title"]
    article_author = article["author"]
    article_url = article["url"]
    try:
        message = message + f"""Article {index+1}:\n {article_title} 
        Written by: {article_author} \n {article_url} \n\n"""
    except AttributeError:
        print("None error")

# the error message was because some source articles or the API were
# encoding the non-unicode characters into ascii to be transferred in bytes
# therefore just need to convert all characters to utf-8 for transfer
message = message.encode("utf-8")
send_email(message=message)

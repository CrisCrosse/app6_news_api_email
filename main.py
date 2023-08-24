import requests
from send_email import send_email

api_key = '2910116ee77c40b0a0d87c348e893a14'
url = "https://newsapi.org/v2/everything?q=te" \
      "sla&from=2023-07-24&sortBy=publishedAt&ap" \
      "iKey=2910116ee77c40b0a0d87c348e893a14"

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
for index, article in enumerate(content["articles"]):
    article_title = article["title"]
    article_author = article["author"]

    try:
        message = message + f"""Article {index+1}:\n {article_title} \n Written by: {article_author} \n\n"""
    except AttributeError:
        print("None error")

# the error message was because some source articles or the API were
# encoding the non-unicode characters into ascii to be transferred in bytes
# therefore just need to convert all characters to utf-8 for transfer
message = message.encode("utf-8")
send_email(message=message)

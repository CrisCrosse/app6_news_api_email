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
for index,article in enumerate(content["articles"]):
    article_title = article["title"]
    article_author = article["author"]
    try:
        print(article_title.encode('ascii'))
        print(article_author.encode('ascii'))
        message = message + f"""Article {index+1}:\n {article_title} \n Written by: {article_author} \n"""
    except UnicodeEncodeError:
        print(f"""article {index+1} not able to be encoded and is skipped""")
    except AttributeError:
        "one of the title or authors was blank"

print(message)
send_email(message=message)



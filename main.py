import requests

api_key = '2910116ee77c40b0a0d87c348e893a14'
url = "https://newsapi.org/v2/everything?q=te" \
      "sla&from=2023-07-24&sortBy=publishedAt&ap" \
      "iKey=2910116ee77c40b0a0d87c348e893a14"

# Make request to get data
request = requests.get(url)

# create a dictionary with the data
content = request.json()

# access the title + description of each article by
# iterating through the list of articles
for article in content["articles"]:
    print(article["title"])
    print(article["source"]["Name"])


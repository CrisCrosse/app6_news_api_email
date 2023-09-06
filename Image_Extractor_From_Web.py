import requests

url = "https://upload.wikimedia.org/wikipedia/commons" \
      "/thumb/9/98/Aldrin_Apollo_11_original" \
      ".jpg/390px-Aldrin_Apollo_11_original.jpg"
response = requests.get(url)

# if response 200 then successful extraction
# into the response variable
print(response)

with open("image_extracted.jpg", "wb") as file:
    file.write(response.content)

import requests


def image_download(image_url, image_name):
    """This function takes an image url from the web and
    creates a jpg file in the local directory with the inputted name
    the url needs to be the exact url of the image
    the image_name must be compatible with naming of files"""
    response = requests.get(image_url)
    with open(f"{image_name}.jpg", "wb") as file:
        file.write(response.content)


url = "https://upload.wikimedia.org/wikipedia/commons" \
      "/thumb/9/98/Aldrin_Apollo_11_original" \
      ".jpg/390px-Aldrin_Apollo_11_original.jpg"

image_download(image_url=url, image_name="image_extracted_function")

# url = "https://upload.wikimedia.org/wikipedia/commons" \
#       "/thumb/9/98/Aldrin_Apollo_11_original" \
#       ".jpg/390px-Aldrin_Apollo_11_original.jpg"
# response = requests.get(url)
#
# # if response 200 then successful extraction
# # into the response variable
# print(response)
#
# with open("image_extracted.jpg", "wb") as file:
#     file.write(response.content)

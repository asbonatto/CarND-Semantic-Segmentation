from requests import get

url = "https://s3-us-west-1.amazonaws.com/udacity-selfdrivingcar/advanced_deep_learning/data_road.zip"

filename = "./data/data_road.zip"

with open(filename, "wb") as f:
    response  = get(url)
    f.write(response.content)

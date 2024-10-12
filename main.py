from pyairtable import Api

api = Api("patvyv6Os9vwVwrKa.c159f00a860990c58a30ab80653f20cf830c6b0c61034786f8098512c47ec1c4")

table = api.table("appTbyLknJqzqvUuV", "Menu")

response = table.all(view="Grid view")

for item in response:
    name = item.get('fields').get("Name")
    price = item.get('fields').get("Price")
    category = item.get('fields').get("Category")
    description = item.get('fields').get("Description")
    available = item.get('fields').get("Available", False)
    image = item.get('fields').get("Assets", None)[0].get("url", None)

    print(f"{name}, {price}, {category}, {description}, {available}, {image}")

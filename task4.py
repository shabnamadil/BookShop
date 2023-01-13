import requests, sys

command = sys.argv
response = requests.get(f"http://www.omdbapi.com/?t={command[2:]}&apikey=67d2565e")

response_json = response.json()
print("-"*50)
if "movie" in command:
    for key, value in response_json.items():
        if key == "Title":
            print(key, ":", value)
        elif key == "Year":
            print(key, ":", value)
        elif key == "Released":
            print(key, ":", value)
        elif key == "Genre":
            print(key, ":", value)
        elif key == "Director":
            print(key, ":", value)
print("-"*50)


import requests

API_URL = "http://localhost:5000/api"


def add_good_score():
    req = requests.put(f"{API_URL}/new", json={"name": "Good", "score": 99, "date": "0000"})
    print(f"Status code: {req.status_code}\n")


def print_scores():
    data = requests.get(f"{API_URL}/list").json()
    print(data["scores"])
    # output = "\n".join(
    #     [f"{score['name']}: {score['score']}: {score['date']}" for score in data["scores"]]
    # )
    # print(output)


def remove_good_score():
    data = {"name": "Good"}
    req = requests.delete(f"{API_URL}/list", json=data)
    print(f"Status code: {req.status_code}\n")

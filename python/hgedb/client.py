import requests

BASE_URL = "http://localhost:8000"

def ping():
    r = requests.get(f"{BASE_URL}/")
    r.raise_for_status()
    return r.json()

def test_db(password):
    r = requests.get(
        f"{BASE_URL}/test_db",
        params={"password": password},
    )
    r.raise_for_status()
    return r.json()

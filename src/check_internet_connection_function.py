import requests

def check_internet_connection():
    try:
        requests.get("https://www.google.com", timeout=5)
        print("Connected to the internet!")
        return True
    except requests.exceptions.ConnectionError:        
        print("No internet connection available.")
        return False
import requests

def client():
    token_h = "Token cde8f8c8f1f1860acf75974e76b1f4e3becea2ea"
    # credentials = {"username": "admin", "password":"q1a2z3w4s5x6"}

    # response = requests.post("http://127.0.0.1:8000/api/rest-auth/login/",
    #                         data=credentials)
    
    headers = {"Authorization": token_h}

    response=requests.get("http://127.0.0.1:8000/api/profiles/",
                            headers=headers)

    print("Status Code:", response.status_code)
    response_data = response.json()
    print(response_data)


if __name__ == "__main__":
    client()
import requests

def client():

    # data = {"username": "resttest",
    #         "email":"test@rest.com",
    #         "password1":"q1a2z3w4s5x6",
    #         "password2":"q1a2z3w4s5x6",
    #         }

    # response = requests.post("http://127.0.0.1:8000/api/rest-auth/registration/",
    #                         data=data)
    
    token_h = "Token dc32f2ae3f4822daf1ed909c439766173fa6f1e4"   
    headers = {"Authorization": token_h}

    response=requests.get("http://127.0.0.1:8000/api/profiles/",
                            headers=headers)

    print("Status Code:", response.status_code)
    response_data = response.json()
    print(response_data)


if __name__ == "__main__":
    client()
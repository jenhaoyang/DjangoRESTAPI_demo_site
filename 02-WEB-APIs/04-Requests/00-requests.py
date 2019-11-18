import requests

def main():
    payload = {"base":"USD", "symbols": "SEK"}
    response = requests.get("https://api.exchangeratesapi.io/latest", params=payload) 

    if response.status_code != 200:
        print("Status Code", response.status_code)
        raise Exception("Error")
    
    data = response.json()
    print("JSON data: ", data)

if __name__=="__main__":
    main()
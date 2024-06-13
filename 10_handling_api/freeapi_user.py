import requests # type: ignore

def fetch_data():
    response = requests.get("https://api.freeapi.app/api/v1/public/randomusers/user/random").json()
    if(response["success"] and "data" in response):
        name = response["data"]["name"]["last"]
        city  = response["data"]["location"]["city"]
        country = response["data"]["location"]["country"]
        return name,city,country
    else:
        raise Exception("Data fecting error")


def main():
    try:
        name,city,country = fetch_data()
        print(f"{name} \n {city} \n {country}")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()


import requests

def main():
    print("Input the URL:")
    url = input()
    response = requests.get(url)

    if response :
        json = response.json()
        # print(json)
        if "content" in json:
            print(json["content"])
        else:
            print("Invalid quote resource!")
    else:
        print("Invalid quote resource!")


main()
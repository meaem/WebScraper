import requests
from bs4 import BeautifulSoup


def save_to_file(content, filename):
    with open(filename,'wb') as f:
        f.write(content)



def main():
    print("Input the URL:")
    url = input()
    response = requests.get(url, headers={'Accept-Language': 'en-US,en;q=0.5'})

    if response:
        # json = response.json()
        # # print(json)
        # if "content" in json:
        #     print(json["content"])
        # else:
        #     print("Invalid quote resource!")

        # soup = BeautifulSoup(response.text)
        # title = soup.find("h1", {"data-testid": "hero-title-block__title"})
        # if title is None:
        #     print("Invalid movie page!")
        #     return
        #
        # description = soup.find("span", {"data-testid": "plot-xl"})
        #
        # print({"title": title.text, "description": description.text})

        save_to_file(response.content,'source.html')
        print("Content saved.")
    else:
        print(f"The URL returned {response.status_code}!")


main()
# number = int(input())
# bytes_number = number.to_bytes(5, byteorder='big')
# number_from_bytes = int.from_bytes(bytes_number,byteorder='big')
# print(number == number_from_bytes)  # <-- expected to be True!
# print(bytes_number )  # <-- expected to be True!
# print(number_from_bytes)  # <-- expected to be True!
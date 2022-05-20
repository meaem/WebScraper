import string

import requests
from bs4 import BeautifulSoup


def save_to_file(content, filename):
    with open(filename,'wb') as f:
        f.write(content)


def get_file_name(article_title):
    for p in string.punctuation:
        article_title = article_title.replace(p, ' ')
    article_title = article_title.strip().replace(' ','_')

    return f"{article_title}.txt"


def extract_content(url):
    response = requests.get(url, headers={'Accept-Language': 'en-US,en;q=0.5'})
    soup = BeautifulSoup(response.text)
    div = soup.find("div",{"class":"c-article-body u-clearfix"})
    if div:
        return div.get_text()
    return ""


def main():
    base_url = 'https://www.nature.com'
    params ='/nature/articles?sort=PubDate&year=2020&page=3'
    url = base_url + params
    # print("Input the URL:")
    # url = input()
    response = requests.get(url, headers={'Accept-Language': 'en-US,en;q=0.5'})

    if response:
        # json = response.json()
        # # print(json)
        # if "content" in json:
        #     print(json["content"])
        # else:
        #     print("Invalid quote resource!")

        soup = BeautifulSoup(response.text)
        title_tags = soup.find_all("article")
        for tag in title_tags:

            type = tag.find("span", {"data-test": "article.type"})
            article_link = tag.find("a", {"data-track-action":"view article"})
            print(type.text.strip())
            if type.text.strip() == 'News':
                print(base_url + article_link.get("href"))
            # print(article_link.get_text())
                if article_link:
                    print(f"title:{article_link.text}")

                    file_name = get_file_name(article_link.text)
                    content = extract_content(base_url + article_link.get("href"))
                    save_to_file(content.encode("utf-8"),file_name)
        # if title is None:
        #     print("Invalid movie page!")
        #     return
        #
        # description = soup.find("span", {"data-testid": "plot-xl"})
        #
        # print({"title": title.text, "description": description.text})


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

# https://www.nature.com/articles/d41586-020-03593-7
# https://www.nature.com/nature/articles/d41586-020-03593-7

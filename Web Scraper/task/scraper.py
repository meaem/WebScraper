import string
import os
import requests
from bs4 import BeautifulSoup


def save_to_file(content, filename):
    with open(filename, 'wb') as f:
        f.write(content)


def get_file_name(article_title):
    for p in string.punctuation:
        article_title = article_title.replace(p, ' ')
    article_title = article_title.strip().replace(' ', '_')

    return f"{article_title}.txt"


def extract_content(url):
    response = requests.get(url, headers={'Accept-Language': 'en-US,en;q=0.5'})
    soup = BeautifulSoup(response.text)
    div = soup.find("div", {"class": "c-article-body u-clearfix"})
    if div:
        return div.get_text()
    return ""


def main():
    base_url = 'https://www.nature.com'
    path_to_pages = '/nature/articles?sort=PubDate&year=2020&page='

    print(os.getcwd())
    max_page_num = int(input())
    article_type = input()
    for page_no in range(1, max_page_num + 1):
        url = f"{base_url}{path_to_pages}{page_no}"
        folder = f"Page_{page_no}"
        print(folder)
        os.mkdir(folder)
        response = requests.get(url, headers={'Accept-Language': 'en-US,en;q=0.5'})
        if response:
            soup = BeautifulSoup(response.text)
            title_tags = soup.find_all("article")
            for tag in title_tags:

                type = tag.find("span", {"data-test": "article.type"})
                article_link = tag.find("a", {"data-track-action": "view article"})
                print(type.text.strip())
                if type.text.strip() == article_type:
                    print(base_url + article_link.get("href"))
                    if article_link:
                        print(f"title:{article_link.text}")
                        file_name = os.path.join(folder, get_file_name(article_link.text))
                        content = extract_content(base_url + article_link.get("href"))
                        save_to_file(content.encode("utf-8"), file_name)

            print("Content saved.")
        else:
            print(f"The URL returned {response.status_code}!")


main()

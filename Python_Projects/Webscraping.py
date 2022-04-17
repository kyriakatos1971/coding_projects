import requests
from bs4 import BeautifulSoup as bs


def main():
    github_user = input('Input Github user: ')

    url = 'https://github.com/'+github_user

    r = requests.get(url)

    soup = bs(r.content, 'html.parser')
    profile_image = soup.find('img', {'alt':'Avatar'})['src']

    print(profile_image)


if __name__ == '__main__':
    main()








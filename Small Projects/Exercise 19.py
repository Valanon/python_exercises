'''
https://www.practicepython.org/solution/2014/10/01/19-decode-a-web-page-two-solutions.html
Using the requests and BeautifulSoup Python libraries, print to the screen the full text of the article on this website: http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture.
'''
import requests
from bs4 import BeautifulSoup

def print_to_text(base_url):
    '''
    :param base_url: URL of article to scrape
    :return: naked content to text file
    '''
    r = requests.get(base_url)
    soup = BeautifulSoup(r.text, "html.parser")
    with open("work less.txt", "w") as textfile:
        for paragraph in soup.find_all(dir="ltr"):
            textfile.write(paragraph.text.replace("<span>",""))

if __name__ == "__main__":
    #choose an article
    base_url = "http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture"
    print_to_text(base_url)
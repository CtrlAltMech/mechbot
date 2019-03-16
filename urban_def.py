"""A simple script that allows you to pull a definition off of Urban Dictionary all from the commandline"""

from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

class DefinitionScraper:

    def __init__(self, url):
        self.url = url
        self.full_link = None
        self.string_definition = None
        self.word = None

    """Appends the search term to the end of the URL and adding '+' between words"""
    def url_modifier(self, search_term):
        word_list = search_term.split()
        if len(word_list) >= 2:
            search_list = "+".join(word_list)
            self.full_link = self.url + search_list
            return self.full_link
        else:
            self.full_link = self.url + search_term
            return self.full_link

    """Creates the soup object from the URL link and finds the definition"""
    def parse_soup(self, link_to_parse):
        uClient = uReq(link_to_parse)
        page_html = uClient.read()
        uClient.close()
        page_soup = soup(page_html, "html.parser")
        def_object = page_soup.find("div", {"class":"meaning"})
        string_list = []

        for string in def_object.stripped_strings:
            string_list.append(string)

        self.string_definition = ' '.join(string_list)

        return self.string_definition

def main():

    search = input("Enter a urban word you want defined: ")

    if search == "":
        print("You did not enter anything. Bye!")
        input()
    else:
        ds = DefinitionScraper(r"http://www.urbandictionary.com/define.php?term=")
        print(ds.url_modifier(search) + "\n")
        ds.parse_soup(ds.full_link)
        print(ds.string_definition)
        input()

main()
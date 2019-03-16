#!/usr/bin/python3

### Urban dictionary scraper module ###

from bs4 import BeautifulSoup as soup
import html2text
import requests

class DefinitionScraper:

    def __init__(self, url):
        self.url = url
        self.full_link = None
        self.string_definition = None
        self.word = None
        self.converted_text = None

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
        r = requests.get(link_to_parse)
        page_html = r.text
        r.close()
        page_soup = soup(page_html, "html.parser")
        def_object = page_soup.find("div", {"class":"meaning"})
        string_list = []

        for string in def_object.stripped_strings:
            string_list.append(string)

        self.string_definition = ' '.join(string_list)
        return self.string_definition

    """Converts all that nasty encoding for you"""
    def html2text_convert(self,text):
        h = html2text.HTML2Text()
        h.ignore_links = True
        h.body_width = 0
        self.converted_text = h.handle(text)
        return self.converted_text

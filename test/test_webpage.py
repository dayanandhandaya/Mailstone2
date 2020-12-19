from bs4 import BeautifulSoup
import pytest
import pickle
import requests


class TestWebpage:
    #@pytest.fixture(autouse=True)
    def get_soup(self):
        source = requests.get("http://127.0.0.1:8000/index.html")
        soup = BeautifulSoup(source.content, 'html.parser')
        return soup

    def test_header(self):
        soup = self.get_soup()
        assert soup.find_all('header')

    def test_footer(self):
        soup = self.get_soup()
        assert soup.find_all('footer')

    def test_navigation(self):
        soup = self.get_soup()
        assert soup.find_all('nav')

    def test_navigation_content(self):
        soup = self.get_soup()
        site = soup.find('ul')
        site_nav = soup.find('nav')
        b=0
        for a in site.find_all('a'):
            if a.contents[0] == 'Home':
                b=b+1
            if a.contents[0] == 'Login/Register':
                b=b+1
            if a.contents[0] == 'Donate Blood':
                b=b+1
            if a.contents[0] == 'Host a Donation Camp':
                b=b+1
            if a.contents[0] == 'Contact US':
                b=b+1
        assert b == 5  
        assert site_nav.h1.string == 'Navigation' 

    def test_footer_content(self):
        soup=self.get_soup()
        site = soup.find('footer')
        assert site.h1.string == 'All Rights Reserved'

    def test_header_content(self):
        soup=self.get_soup()
        site = soup.find('header')
        assert site.h1.string == 'Save a LIFE today..'

    def test_article_content(self):
        soup = self.get_soup()
        site = soup.find('article')
        assert site.h1.string == 'Motivation for blood donation'
        assert site.p.contents[0]=='To give blood you neither need extra strength not extra food, and you will save a life....'





                     
    



       
      
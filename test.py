
import urllib2
from bs4 import BeautifulSoup


def main():
    quote_page = 'https://www.wunderground.com/hurricane/atlantic/2016/Post-Tropical-Cyclone-Alex'
    page = urllib2.urlopen(quote_page)

    # parse the html using beautiful soup and store in variable `soup`
    soup = BeautifulSoup(page,'html.parser')

    # Take out the <div> of name and get its value
    name_box = soup.find('h3', attrs = {'class ': 'columns'})

    name = name_box.text.strip()
    print name


if __name__ == "__main__":
    main()

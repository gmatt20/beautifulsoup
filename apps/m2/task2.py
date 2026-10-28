from bs4 import BeautifulSoup, SoupStrainer
import sys

a = SoupStrainer("a")

with open(sys.argv[1]) as htmlFile:
    soup = BeautifulSoup(htmlFile, "html.parser", parse_only=a)

with open("pretty.html", "w") as prettyFile:
    prettyFile.write(soup.prettify())

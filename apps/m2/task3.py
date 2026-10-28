from bs4 import BeautifulSoup, SoupStrainer
import sys

tags = SoupStrainer(True)

with open(sys.argv[1]) as htmlFile:
    soup = BeautifulSoup(htmlFile, "html.parser")

with open("prettyTags.html", "w") as prettyFile:
    allTags = soup.find_all(tags)
    for tag in allTags:
        prettyFile.write(tag.prettify())

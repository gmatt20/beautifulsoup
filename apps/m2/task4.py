from bs4 import BeautifulSoup, SoupStrainer
import sys

id = SoupStrainer(id=True)

with open(sys.argv[1]) as htmlFile:
    soup = BeautifulSoup(htmlFile, "html.parser", parse_only=id)

with open("ids.html", "w") as prettyFile:
    allIds = soup.find_all(id)
    for ids in allIds:
        prettyFile.write(ids.prettify())

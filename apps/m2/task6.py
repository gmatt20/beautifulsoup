from bs4 import BeautifulSoup, SoupReplacer
import sys

b_to_blockquote = SoupReplacer("b", "blockquote")

with open(sys.argv[1]) as htmlFile:
    soup = BeautifulSoup(htmlFile, "html.parser", replacer=b_to_blockquote)


with open("blockquote.html", "w") as htmlFile:
    htmlFile.write(soup.prettify())

from bs4 import BeautifulSoup, SoupReplacer
import sys


def replace_div(tag):
    if tag.name == "p":
        return {**tag.attrs, "class": "test"}
    return tag.attrs


b_to_blockquote = SoupReplacer(attrs_xformer=replace_div)

with open(sys.argv[1]) as htmlFile:
    soup = BeautifulSoup(htmlFile, "html.parser", replacer=b_to_blockquote)


with open("classChange.html", "w") as htmlFile:
    htmlFile.write(soup.prettify())

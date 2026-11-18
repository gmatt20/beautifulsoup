from bs4 import BeautifulSoup
import sys

with open(sys.argv[1]) as htmlFile:
    soup = BeautifulSoup(htmlFile, "html.parser")

for node in soup:
    print(node)

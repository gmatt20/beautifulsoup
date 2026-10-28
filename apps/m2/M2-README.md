# Milestone-2

## Part-2 - All APIS used in Milestone-1 and Milestone-2 Part-1

### Milestone-1 APIs

```Python
BeautifulSoup(htmlFile, "html.parser")
```

BeautifulSoup class is located in line 133 in beautifulsoup/bs4/**init**.py. The class takes in several parameters, most relevant is the `markup: _IncomingMarkup = "",` in line 211 and the `features: Optional[Union[str, Sequence[str]]] = None,` in line 212. The markup parameter is the file/string that contains the markup that needs to be parsed, while the features parameter is used to indicate the parser preference (HTML, XML, etc). The BeautifulSoup class also specifies a filter via `parse_only` to only filter specific elements

```Python
soup.prettify()
```

The `prettify()` function belongs to the Tag class located in line 1569 in beautifulsoup/bs4/element.py. The method implementation is located in line 2601. Prettify calls the decode() (line 2334 in beautifulsoup/bs4/element.py) function which performs the formatting.

```Python
soup.find_all()
```

The `find_all()` function belongs to the Tag class located in line 1569 in beautifulsoup/bs4/element.py. The method implementation is located in line 2715. find_all() takes in several relevant parameters such as filtering for method names, attributes, and tags in the form of string. find_all() calls the private \_find_all() function contained in the Tag class in line 1079 which performs the filtering.

```Python
a = soup.find("a")
```

The `find()` function belongs to the Tag class located in line 1569 in beautifulsoup/bs4/element.py. The method implementation is located in line 2684. find() takes in several relevant parameters such as filtering for method names, attributes, and tags in the form of string. It's different from find_all() in that it looks into the children of the specified element.

```Python
parent = a.find_parent()
```

The `find_parent()` function belongs to the Tag class located in line 1569 in beautifulsoup/bs4/element.py. The method implementation is located in line 992. find_parent() takes in several relevant parameters such as filtering for method names, and attributes but can be called directly from itself.

```Python
blockquote.name = "blockquote"
```

The name attribute belongs to the Tag class located in line 1569 in beautifulsoup/bs4/element.py.

```Python
p["class"] = "test"
```

The `cdata_list_attributes: Optional[Dict[str, Set[str]]] = None` parameter belongs to the Tag class located in line 1569 in beautifulsoup/bs4/element.py and more specifically in line 1632.

```Python
soup.css.select("html body center p tr")
```

The `css()` function belongs to the Tag class located in line 1569 in beautifulsoup/bs4/element.py. The function implementation, located in 2825, returns an interface to the CSS selector API.

### Milestone-2 Part-1 APIs

```Python
a = SoupStrainer("a")
```

SoupStrainer class is located in line 313 in beautifulsoup/bs4/filter.py. The class takes in one parameter `ElementFilter,` in line 313. The attributes of SoupStrainer includes method names, attributes, and tags in the form of string

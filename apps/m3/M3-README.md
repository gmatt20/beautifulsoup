# Milestone-3

Extending the new APIs wasn't as challenging as anticipated. Milestone-2 had more friction in that I was introducing a brand new API, which had me spend some time in analyzing the project architecture closely. However, the hard work from the prior milestone paid off, because I was able to easily extend the new API with new features as outlined in Milestone-3. Here are the technical changes:

- SoupReplacer now introduces new parameters: name_xformer, attrs_xformer and xformer.
- name_xformer will replace takes in a function or lambda function to replace tag names only.
- attrs_xformer takes in a function or lambda function to replace attributes.
- xformer is a more powerful parameter in which a function or lambda function can be passed in and can replace either names and/or attributes.
- 6 new test cases to test the new parameters

The new parameters differ from the previous parameters in milestone 2 because the new parameters are able to accept robust functions as a parameter, which allows the user to create more complicated conditions and replacements. However, this comes with a cost. attrs_xformer never needs special handling at the closing tag because `_popToTag` only matches by tag names and attributes themselves are not tag names. name_xformer is different because the parser needs to know the new tag name at the closing tag too, or it will produce a wrong tree. attrs_xformer doesn't encounter that problem because it does not need to replace closing tag names. xformer doesn't get this same closing tag handling at all, because it's an arbitrary function and there's no Tag object available at the closing tag to safely run it against.

A potential extension of SoupReplacer to make name_xformer and xformer tag handling better is to reuse the Tag object rather than constructing a new one. Whether or not the function actual needs it, the function will always have the Tag object when it needs it.

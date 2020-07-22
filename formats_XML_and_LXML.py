# XML
from xml.etree import ElementTree

tree = ElementTree.parse("example.xml")
root = tree.getroot()

print(root)
print(root.tag, root.attrib)

for element in root.iter("scores"):
    score_sum=0
    for child in element:
        score_sum+=float(child.text)
    print(score_sum)

tree.write("example_copy.xml")

# lxml
from lxml import etree
import requests

res=requests.get("https://docs.python.org/3/")
print(res.status_code)
print(res.headers["Content-Type"])

parser=etree.HTMLParser()
root=etree.fromstring(res.text, parser)

for element in root.iter("a"):
    print(element, element.attrib)

from lxml import html
from lxml.etree import tostring

def parse(text):
    tree = html.fromstring(text)
    return int(tree.xpath('//table[descendant::*[contains(text(), \'Aantal positief geteste mensen in Nederland\')]]//td[2]//h2/text()')[0])

from lxml import html
from lxml.etree import tostring

def parse(text):
    tree = html.fromstring(text)
    return int(tree.xpath('//table[descendant::*[contains(text(), \'fall av covid-19 i Sverige\')]]//tr[descendant::*[contains(text(), \'Totalt\')]]/td[2]//text()')[0])

from lxml import etree
import tempfile

def parse_xml(file):
    tmp = tempfile.NamedTemporaryFile(delete=False)
    file.save(tmp.name)
    tree = etree.parse(tmp.name)
    root = tree.getroot()
    return {child.tag: child.text for child in root}


from lxml import etree
 
def parseXML(xmlFile):
    """
    Парсинг XML
    """
    with open(xmlFile) as fobj:
        xml = fobj.read()
    
    root = etree.fromstring(xml)
    
    tree = etree.ElementTree(root)
    for e in root.iter():
        print (tree.getpath(e))

    #for appt in root.getchildren():
    #    for elem in appt.getchildren():
    #        if not elem.text:
    #            text = "None"
    #        else:
    #            text = elem.text
    #        
    #        print(etree._e .geelem.base + " => " + text)
 
 
if __name__ == "__main__":
    parseXML("d:\\logs\\SRM-4664 BPM_ML-ODS mapping\\example.xml")

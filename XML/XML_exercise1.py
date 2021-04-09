import xml.etree.ElementTree as etree

tree = etree.parse('annot.opcorpora.no_ambig.xml')
root = tree.getroot()
with open("allSentences.txt", 'w') as f:
    for text in root.iter('source'):
        f.write(text.text + "\n")

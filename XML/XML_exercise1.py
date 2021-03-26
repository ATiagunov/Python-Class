import xml.etree.ElementTree as etree

tree = etree.parse('annot.opcorpora.no_ambig.xml')
root = tree.getroot()
with open("allSentences.txt", 'w') as f:

    for child in root.findall('text'):
        paragraphs = child.find('paragraphs')
        for paragraph in paragraphs:
            sentences = paragraph.findall('sentence')
            for sentence in sentences:
                text = sentence.find('source')
                f.write(text.text + "\n")
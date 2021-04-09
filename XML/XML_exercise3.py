import xml.etree.ElementTree as ET

tree = ET.parse('annot.opcorpora.no_ambig.xml')
root = tree.getroot()

verbCounter = 0
conjCounter = 0

for token in root.iter('token'):
    word = (token.get('text'))
    if word == 'может' or word == 'Может':
        vs = token.findall('tfr')
        for v in vs:
            ls = v.find('v')
            for l in ls:
                gs = l.findall('g')
                if gs[0].attrib['v'] == 'CONJ':
                    conjCounter += 1
                elif gs[0].attrib['v'] == 'VERB':
                    verbCounter += 1


print("'может' as conj: ", conjCounter)
print("'может' as verb: ", verbCounter)

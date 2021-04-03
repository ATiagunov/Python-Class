import xml.etree.ElementTree as ET

tree = ET.parse('annot.opcorpora.no_ambig.xml')
root = tree.getroot()
with open("pluralNouns.txt", 'w') as f:
    for token in root.iter('token'):
        word = (token.get('text'))
        vs = token.findall('tfr')
        for v in vs:
            ls = v.find('v')
            for l in ls:
                gs = l.findall('g')
                if gs[0].attrib['v'] == 'NOUN' and gs[len(gs) - 2].attrib['v'] == 'plur':
                    f.write(word + "\n")


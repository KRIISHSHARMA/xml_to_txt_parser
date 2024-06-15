import xml.etree.ElementTree as ET

def xml_to_txt(xml_file, txt_file):
    # Parse the XML file
    tree = ET.parse(xml_file)
    root = tree.getroot()
    
    # Open the text file for writing
    with open('output.txt', 'w') as file:
        # Recursively process each element in the XML
        def process_element(element, level=0):
            indent = '  ' * level
            file.write(f'{indent}{element.tag}: {element.text}\n')
            for child in element:
                process_element(child, level + 1)
        
        process_element(root)
# put actual name of xml file intead fo file.txt
xml_to_txt('file.xml', 'output.txt')

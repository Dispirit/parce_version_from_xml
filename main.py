import xml.etree.ElementTree as ET
import re
import sys


def get_version(file_xml, search_version) -> str:
    root = ET.parse(file_xml).getroot()
    value_list = []
    all_elements = []
    for type_tag in root.findall('versioning/versions/version'):
        value = type_tag.text
        all_elements.append(value)
        pre_version = re.search(r'(^\d+.\d+)', value).group(0)
        if search_version == pre_version:
            value_list.append(value)
    if not value_list:
        last_element = all_elements[-1]
    else:
        last_element = value_list[-1]
    version = re.search(r'(\d+.\d+.\d+)', last_element).group(0)
    print(version)


if __name__ == '__main__':
    # xml_file = sys.argv[1]
    # manual_version = sys.argv[2]
    xml_file = 'maven-metadata.xml'
    manual_version = "1.0"
    get_version(xml_file, manual_version)

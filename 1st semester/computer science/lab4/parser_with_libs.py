import json
import xml.etree.ElementTree as ET

with open('timetable.json', 'r') as f:
    data = json.load(f)

    # Building the root element
    root = ET.Element("timetable")

    header1 = ET.SubElement(root, "subject1")
    text = data["timetable"]["subject1"]

    # convert to string
    ET.SubElement(header1, "day").text = str(data["subject1"][0])
    ET.SubElement(header1, "time").text = str(data["subject1"][1])
    ET.SubElement(header1, "week").text = str(data["subject1"][2])
    ET.SubElement(header1, "lesson").text = str(data["subject1"][3])
    ET.SubElement(header1, "teacher").text = str(data["subject1"][4])
    ET.SubElement(header1, "format").text = str(data["subject1"][5])
    ET.SubElement(header1, "place").text = str(data["subject1"][6])
    ET.SubElement(header1, "room").text = str(data["subject1"][7])


    header2 = ET.SubElement(root, "subject2")

    ET.SubElement(header2, "day").text = str(data["subject2"][0])
    ET.SubElement(header2, "time").text = str(data["subject2"][1])
    ET.SubElement(header2, "week").text = str(data["subject2"][2])
    ET.SubElement(header2, "lesson").text = str(data["subject2"][3])
    ET.SubElement(header2, "teacher").text = str(data["subject2"][4])
    ET.SubElement(header2, "format").text = str(data["subject2"][5])
    ET.SubElement(header2, "place").text = str(data["subject2"][6])
    ET.SubElement(header2, "room").text = str(data["subject2"][7])


    header3 = ET.SubElement(root, "subject3")

    ET.SubElement(header3, "day").text = str(data["subject3"][0])
    ET.SubElement(header3, "time").text = str(data["subject3"][1])
    ET.SubElement(header3, "week").text = str(data["subject3"][2])
    ET.SubElement(header3, "lesson").text = str(data["subject3"][3])
    ET.SubElement(header3, "teacher").text = str(data["subject3"][4])
    ET.SubElement(header3, "format").text = str(data["subject3"][5])
    ET.SubElement(header3, "place").text = str(data["subject3"][6])
    ET.SubElement(header3, "room").text = str(data["subject3"][7])

    # Building the tree of the xml elements using the root element
    tree = ET.ElementTree(root)
    # Writing the xml to output file
    tree.write('timetable.xml')

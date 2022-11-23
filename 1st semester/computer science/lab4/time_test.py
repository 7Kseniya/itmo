import time
from manual_parser import parse_json, create_dump_to_xml, create_xml
from parsing_with_libs import parse_json_and_dump_to_xml
from manual_parser_with_regex import parse_json_with_regex

Sourse_File = "timetable.json"
Output_File = "timetable.xml"
N_Tests = 10

if __name__ == '__main__':
    print(f'time took to execute {N_Tests} tests: ')

    start = time.time()

    for _ in range(N_Tests):
        data = parse_json(Sourse_File)
        xml_code = create_xml(data)
        dump_to_xml(Output_File, xml_code)

    print(f'manual parsing without regex: {time.time() - start}')

    start = time.time()

    for _ in range(N_Tests):
        data = parse_json_with_regex(Sourse_File)
        xml_code = create_xml(data)
        dump_to_xml(Output_File, xml_code)

    print(f'manual parsing with regex: {time.time() - start}')

    start = time.time()

    for _ in range(N_Tests):
        parse_json_and_dump_to_xml(Sourse_File, Output_File)

    print(f'manual parsing using libraries: {time.time() - start}')

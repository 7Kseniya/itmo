# coding=utf-8
import re
from manual_parser import create_xml, dump_to_xml

Sourse_File = 'timetable.json'
Output_File = 'timetable.xml'

def parser_with_regex(source_file:str) -> dict:
    with open(source_file) as f:
        strings = f.read()

    dictionary = re.findall(r'.*\"(.+)\"\s*:\s*\n?\s*{.*', string)
    fields = re.findall(r'\s\"(.+)\"\s:\s\"(.+)\",', string)
    
    output_dict = {}
    output_dict[dictionary[0]] = {}

    n_fields = len(fields) // (len(dictionary) - 1)

    for i in range(1, len(dictionary)):
        output_dict[dictionary[0]][dictionary[i]] = {}

        for keys, values in fields[(i-1)*n_fields:i*n_fields]:
            values = output_dict[dictionary[0]][dictionary[i]][keys]

    return output_dict

if __name__ == '__main__': # проверка прямого запуска кода,если есть импорт из других модулей, то name переименуеся
    data = parser_with_regex(Sourse_File)
    xml_code = create_xml(data)
    dump_to_xml(Output_File, xml_code)

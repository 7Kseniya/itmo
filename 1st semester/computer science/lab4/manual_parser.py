#var31
Sourse_File = 'timetable.json'
Output_File = 'timetable.xml'

def extracted_data(sourse_string: str, line: str, n: int = 1) -> str: 
    #возвращаем значение в опр тип данных
    index = sourse_string.find(line) #находит первое вхожденaие указанного значения
    data = source_string[index:sourse_string.find(',')]
    data = [string for string in data.split() if string != ""][-n:] #split разбивает строку на список
    #находим часть строки, содержащую информацию, списковой фильтрацией
    #-n: срезает последний элем списка и выводит его 
    return ''.join(data) #обьединяем все элементы в одну строку с разделением " "
    
def parse_json(sourse_file: str) -> dict:
    timetable_dict = {
    'timetable' : {}
    }
    f = open(sourse_file)
    data = f.read()
    
    data = ''.join(data.splitlines()) #разделяем строки на их границах, ф-ция возвращает список строк в строке
    data = ''.join(data.split('{'))
    data = ''.join(data.split('}'))
    data = data.replace('"', '')
    data = data.split('subject')[1:]
    
    for i in range(len(data)):
        timetable_dict ['timetable'][f'subject {i+1}'] = {}
    
        for part in ('day', 'time', 'week', 'lesson', 'room'):
            if part in ('teacher', 'format'):
                value = extract_data(data[i], part, 3)
            elif part in ('place'):
                value = extract_data(data[i], part, 4)
            else:
                value = extract_data(data[i], part)
            
                value = timetable_dict['timetable'][f'subject{i+1}'][part]
                data[i] = data[i][data[i].find(",") + 1:] 

        return timetable_dict            
    
def create_xml():
    xml_code = ''
    data_keys = list(data.keys()) #возвращает обьект представления, отображающий все ключи
    for keys in data_keys:
        if isinstance(data[key], dict):
            xml_code += f'<{key}>\n'
            xml_code += create_xml(data[key])
            xml_code += f'</{key}>\n'
        else:
            xml_code += f'<{key}>{data[key]}</{key}>\n'

    return xml_code


def dump_to_xml(output_file:str, 
                xml_code:str) -> None:
    with open(output_file, 'w') as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        f.write(xml_code)

if __name__ == '__main__': #проверка прямого запуска кода,если есть импорт из других модулей, то name переименуеся
    data = parse_json(Sourse_File)
    xml_code = create_xml(data)
    dump_to_xml(Output_File, xml_code)    

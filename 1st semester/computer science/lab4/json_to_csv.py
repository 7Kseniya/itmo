# coding=utf-8
import json
import csv


data = ''
if __name__ == "__main__":
    with open('timetable.json', 'r') as f:
        for line in f.read():
            data += line  # заполняем список строками из файла
    data = json.loads(data)

    with open('timetable.csv', 'w') as f:
        writer = csv.DictWriter(f, data[0].keys())  # ссылаемся на первый элемент в словаре и вызываем его значение
        writer.writeheader()
        for name in data:
            writer.writerow(name)

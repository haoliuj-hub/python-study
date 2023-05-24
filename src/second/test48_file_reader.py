"""
文件读取类
"""
import json

from second.test48_file_define import Record


class FileReader:

    def __init__(self, file_path):
        self.file_path = file_path

    def read_data(self):
        pass


class TxtReader(FileReader):

    def read_data(self) -> list[Record]:
        file = open(self.file_path, 'r', encoding='utf-8')

        result: list[Record] = []
        for line in file.readlines():
            line = line.strip()
            data_list = line.split(',')
            result.append(Record(data_list[0], data_list[1], int(data_list[2]), data_list[3]))

        file.close()
        return result


class JSONReader(FileReader):

    def read_data(self) -> list[Record]:
        file = open(self.file_path, 'r', encoding='utf-8')

        result: list[Record] = []
        for line in file.readlines():
            data_dict = json.loads(line)
            result.append(
                Record(data_dict['date'], data_dict['order_id'], int(data_dict['money']), data_dict['province']))

        file.close()
        return result


if __name__ == '__main__':
    reader = TxtReader('../../resource/2011年1月销售数据.txt')
    data = reader.read_data()
    for record in data:
        print(record)

    reader2 = JSONReader('../../resource/2011年2月销售数据JSON.txt')
    data2 = reader2.read_data()
    for record in data2:
        print(record)

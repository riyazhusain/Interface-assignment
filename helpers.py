class DataProcessing:
    """
    Helper class to read and process the file and return list it takes input file path to be processed.
    """

    @staticmethod
    def get_data(file):
        all_records = list()
        with open(file, "r") as file_object:
            file_content = file_object.read().split('!')
            clean_data = [x.strip().split('\n') for x in file_content]
            for element in clean_data:
                each_record = dict()
                for item in element:
                    item = item.strip().split(" ")
                    if len(item) == 2:
                        each_record.update({item[0]: item[1]})
                    elif len(item) > 2:
                        if item[0] == 'description':
                            b = " ".join([str(i) for i in item[1:]])
                            each_record.update({item[0]: b})
                        if item[0] == 'ip':
                            a = str(item[0] + ' ' + item[1])
                            each_record.update({a: item[2]})
                            each_record.update({'Subnet mask': item[3]})
                all_records.append(each_record)
        return all_records

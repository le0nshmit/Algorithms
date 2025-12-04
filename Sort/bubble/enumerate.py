import os

class Enumerate():
    def __init__(self):
        pass

    def get_list(self):
        files = os.listdir()

        for file in files:
            if file == 'list_result.txt':
                file_open = open(file, 'r')
                results = file_open.read()
                file_open.close()

        return results



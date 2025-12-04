import random

class Generate:
    def __init__(self):
        self.list = []
        self.lists_length = self.get_value('Enter amount of lists: ')
        self.list_length = self.get_value('Enter List Length: ')

    def get_value(self, msg):
        try:
            value = int(input(msg))
        except ValueError:
            print("An integer wasn't input!")

        return value

    def create_list(self):
        file = open('list_result.txt', 'w')
        file.write('')
        file.close()

        for _ in range(self.lists_length):
            self.list = []
            while len(self.list) < self.list_length:
                number = random.randint(1,10)
                if number not in self.list:
                    self.list.append(number)

           
        
            file = open('list_result.txt', 'a')
            file.write(f'{self.list}\n')
            file.close()


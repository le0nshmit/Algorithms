from enumerate import Enumerate
from generate import Generate
import os
import random

class Bubble:
    def __init__(self):
        self.list = []
        self.lists = Enumerate().get_list()


    def generate_lists(self):
        list_generate = Generate()
        list_generate.create_list()

    def sort(self):
        print(f'Insert: {self.list}')

        for step in range(len(self.list)-1):
            for j in range(len(self.list)-1):
                if self.list[j] > self.list[j+1]:
                    self.list[j], self.list[j+1] = self.list[j+1], self.list[j]
        
            print(f'Step {step +1}: {self.list}')

    def bubble(self):
        self.generate_lists()
        print(self.lists)
        

if __name__ == '__main__':
    poo = Bubble()
    poo.bubble()
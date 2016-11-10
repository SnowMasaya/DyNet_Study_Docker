#!/usr/bin/env python

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "."))
from os import path
APP_ROOT = path.dirname( path.abspath( __file__ ) )

class DataCount():
    """
    """

    def __init__(self, file_name, out_putfile_name):
        self.file_name = file_name
        self.out_put_file_name = out_putfile_name
        self.concept_data = {}
        self.concept_vocabuary = {}
        self.word_vocabuary = {}

    def interface_data_arrange(self):
        self.__count_vocabulary()

    def __count_vocabulary(self):
        with open(self.file_name, 'r') as f:
            data_list = f.read().split("\n")
            self.__data_arrange(data_list)

    def __data_arrange(self, data_list):
        for data in data_list:
            split_data = data.split("\t")
            if split_data[0] not in self.concept_vocabuary:
                self.concept_vocabuary.update({split_data[0]:1})
            for word in split_data[1].split(" "):
                if word not in self.word_vocabuary:
                    self.word_vocabuary.update({word:1})
        self.__output_file()

    def __output_file(self):
        with open(self.out_put_file_name, 'w') as f:
             f.write("Word Vocubaly" + str(len(self.word_vocabuary)))
             f.write("\n")
             f.write("Concept Vocubaly" + str(len(self.concept_vocabuary)))
             f.write("\n")

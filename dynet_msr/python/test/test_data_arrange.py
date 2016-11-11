#!/usr/bin/env python
#coding: utf8
import unittest
import sys
import os
from os import path
sys.path.append(os.path.join(os.path.dirname("__file__"), "./../"))
sys.path.append(os.path.join(os.path.dirname("__file__"), "."))
from data_arrange import DataArrange
from data_count import DataCount
from data_interface import DataInterface
APP_ROOT = path.dirname(path.abspath(__file__))
import filecmp


class Test_DataArrange(unittest.TestCase):
    """
    """

    def setUp(self):
        """

        """
        self.data_arrange_instance = DataArrange(APP_ROOT + "/../../data/test.txt", \
                                                 #APP_ROOT + "/../../data/data-concept-instance-relations_train.txt")
                                                 APP_ROOT + "/../../data/data-concept-instance-relations_test.txt")
        self.data_count_instance = DataCount(APP_ROOT + "/../../data/data-concept-instance-relations_train.txt", \
                                                 APP_ROOT + "/../../data/word-concept-vocabulary.txt")
        self.interface_data_arrange = DataInterface(self.data_arrange_instance)
        self.interface_data_vocabualy = DataInterface(self.data_count_instance)

    #def test_data_arrange(self):
    #    """
    #    data arrange
    #    :return:
    #    """
    #    self.interface_data_arrange.interface_data_arrange()

    def test_data_count(self):
        """
        count vocabulary
        :return:
        """
        self.interface_data_vocabualy.interface_data_arrange()

if __name__ == '__main__':
    unittest.main()

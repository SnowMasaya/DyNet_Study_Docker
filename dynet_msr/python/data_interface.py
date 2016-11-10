#!/usr/bin/env python

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "."))
from os import path
APP_ROOT = path.dirname( path.abspath( __file__ ) )


class DataInterface():

    def __init__(self, instance):
        self.instance = instance

    def interface_data_arrange(self):
        self.instance.interface_data_arrange()


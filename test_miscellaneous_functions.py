#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 31 15:53:40 2026

@author: abrahamtraore
"""

import unittest
from library import  Call_Put_processing, Architecture
import pandas as pd
import numpy as np


class TestCallPutProcessing(unittest.TestCase):
    def test_replace_missing(self):
        instance =  Call_Put_processing("address", 10)
        instance.data = pd.DataFrame(np.array([[1,2],[3,np.nan]]))
        instance.replace_missing()
        expected_value = pd.DataFrame(np.array([[1,2],[3,2]]))
        self.assertTrue(instance.data.equals(expected_value.astype(float)))


class TestArchitecture(unittest.TestCase):
    def test_model_recovery(self):
        architecture = Architecture(20)
        architecture.model_recovery()
        weights = architecture.ml_model.get_weights()
        self.assertTrue(len(weights) == 5)

if __name__ == '__main__':
    unittest.main()
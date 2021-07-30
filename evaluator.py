import numpy as np
import time
import subprocess
import sys, os
import copy


class evaluator(object):
    # Each evaluator must contain two major functions: set_params(params) and evaluate(params)
    def set_params(self, params):
        # Set the params to the desired component
        raise NotImplementedError
    
    def evaluate(self, params):
        # Execute and collect reward.
        raise NotImplementedError

    @property
    def log(self):
        return ""


class test_evaluator(object):
    # Each evaluator must contain two major functions: set_params(params) and evaluate(params)
    def __init__(self):
        self.x = 0

    def set_params(self, params):
        # Set the params to the desired component
        self.x = params[0]
    
    def evaluate(self, params):
        # Execute and collect reward.
        self.set_params(params)
        return -(self.x - 1)** 2

    @property
    def log(self):
        return "x = " + str(self.x)

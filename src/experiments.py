"""
Set of experiments

"""

import os
import sys
import subprocess
from subprocess import PIPE, Popen
import json

from utils import get_compression_factor


class AbstractExperiment:
    def __init__(self, **kwargs):
        self.output_file = kwargs.get('output_file', 'exp_out.jpg')
        self.input_file  = kwargs.get('input_file',  '../res/simple.raw')
        self.algo        = kwargs.get('algo')
        self.pred        = kwargs.get('pred', None)

    def run(self):
        self.initialize()
        cmd = f"./encoder.py --input  {self.input_file} " +\
                           f"--output {self.output_file} "+\
                           f"--algo   {self.algo} "       +\
                           f"--pred   {self.pred} "

        # print(cmd)
        FNULL = open(os.devnull, 'w')
        os.chdir(sys.path[0])
        # subprocess.call(cmd.split(),
        #                 stdout=FNULL,
        #                 stderr=subprocess.STDOUT)
        p = Popen(cmd.split(),
                  stdin=PIPE,
                  stdout=PIPE,
                  stderr=PIPE)
        self.res, _ = p.communicate()
        self.mesure()
        self.report()

    def initialize(self):
        pass

    def mesure(self):
        raise NotImplementedError()

    def report(self):
        raise NotImplementedError()


class ExpPredictive_1(AbstractExperiment):
    """
    Mesure compression ratio of the predictive algorithm on a
    simple image, without additionnal encoding
    """

    def initialize(self):
        self.algo = "predictive"

    def mesure(self):
        self.factor = get_compression_factor(
            before=self.input_file,
            after= self.output_file)

    def report(self):
        print(
            "Experiment" +\
            self.__doc__ +\
            f"using {self.algo} algorithm\n\n" +\
            f"    compression factor = {self.factor}\n")

class ExpPredictive_2(AbstractExperiment):
    """
    Mesure compression ratio of the predictive algorithm on a
    simple image, without additionnal encoding,
    with a bad prediction matrix
    """

    def initialize(self):
        self.algo='predictive'
        self.pred='bad'

    def mesure(self):
        self.factor = get_compression_factor(
            before=self.input_file,
            after= self.output_file)

    def report(self):
        print(
            "Experiment" +\
            self.__doc__ +\
            f"using {self.algo} algorithm\n\n" +\
            f"    compression factor = {self.factor}\n")


class ExpBytes_1(AbstractExperiment):
    """
    Mesure compression ratio of the byte algorithm on a
    simple image, without additionnal encoding,
    """

    def initialize(self):
        self.algo='pairs'

    def mesure(self):
        self.factor = get_compression_factor(
            before=self.input_file,
            after= self.output_file)


    def report(self):
        j = json.loads(self.res)
        factor = str(j['compression_rate'])
        print(
            "Experiment" +\
            self.__doc__ +\
            f"using {self.algo} algorithm\n\n" +\
            f"    compression factor = {factor}\n")


def run_experiments():
    ExpPredictive_1().run()
    ExpPredictive_2().run()
    ExpBytes_1().run()

run_experiments()

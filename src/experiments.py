"""
Set of experiments

"""

import subprocess

from utils import get_compression_factor


class AbstractExperiment:
    def __init__(self, **kwargs):
        self.output_file = kwargs.get('output_file', 'exp_out.jpg')
        self.input_file  = kwargs.get('input_file',  '../res/simple.raw')
        self.algo        = kwargs.get('algo')
        self.pred        = kwargs.get('pred', None)

    def run(self):
        cmd = '''
              ./encoder.py --input  {input} \
                           --output {output}\
                           --algo   {algo}
        '''.format(input= self.input_file,
                   output=self.output_file,
                   algo=  self.algo,
        )
        subprocess.call(cmd.split())

        self.mesure()
        self.report()


    def mesure(self):
        raise NotImplementedError()

    def report(self):
        raise NotImplementedError()


class ExpPredictive_1(AbstractExperiment):
    """
    Mesure compression ratio of the predictive algorithm on a
    simple image, without additionnal encoding
    """

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


def run_experiments():
    exp1 = ExpPredictive_1(
        algo='predictive'
    )
    exp1.run()


run_experiments()

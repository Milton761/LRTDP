import argparse
from util import *
from lrtdp import *

from pddlparser import PDDLParser




#R = instantiate_action(domain.operators[0], problem.objects)









V = {}
H = {}




lrtdp(problem.init, 0.0, H, V)
print(len(V))

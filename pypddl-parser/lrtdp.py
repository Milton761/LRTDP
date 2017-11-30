import argparse

from pddlparser import PDDLParser

path_domain = "pddl/triangle-tireworld/domain.ppddl"
path_problem = "pddl/triangle-tireworld/problems/p01.ppddl"

domain  = PDDLParser.parse(path_domain)
problem = PDDLParser.parse(path_problem)

print(domain)
print(problem)


def lrtdp(s, error):


	SOLVED = {}
	SOLVED[s] = False

	while SOLVED[s] == False :
		lrtdp_trial(s, error)

def lrtdp(s, error):

	#stack 
	visited = []
	
	while SOLVED[s] == False:
		visited.append(s)

		if goal.issubset(s):
			break

		a = greedy_action(s)
		update(s)

		s = pick_next_state(s,a)

	while len(visited)!=0:
		s = visited.pop()

		if check_solved[s,error]==False:
			break




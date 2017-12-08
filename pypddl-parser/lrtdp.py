import argparse
from util import *
import numpy as np
import math
from heuristics import *

from pddlparser import PDDLParser
import sys


heuristics_type = 0


def lrtdp(domain, problem, error, H, V):

	domainR = relaxProblem(domain)
	s = problem.init

	SOLVED = {}
	SOLVED[str(s)] = False
	
	while SOLVED[str(s)] == False :
		lrtdp_trial(s,domainR, domain, problem,  error,SOLVED, H, V)

def lrtdp_trial(s, domainR, domain, problem, error, SOLVED,H, V):


	s0_source = s
	visited = []
		
	while SOLVED[str(s)] == False:


	
		visited.append(s)

		if problem.goal.issubset(s):

			print("Trial end in Goal State > new trial")
			break

		#print("choose action")
		[a,P] = greedy_action(s,domainR,  domain, problem, H, V)

		

		update(s, domainR, domain , problem, H, V)

		#print(s)
		s = pick_next_state(s,a, P)



		if s == False:
			print("Trial end in Dead End > restart trial")
			s = s0_source
			

		
		if str(s) not in SOLVED.keys():
			SOLVED[str(s)] = False

	

	while len(visited)!=0:
		s = visited.pop()

		if check_solved(s, domainR, domain, problem, error, SOLVED,P,H, V)==False:
			break



def check_solved(s,domainR, domain, problem, error, SOLVED,P, H, V):
	rv = True

	openS = []
	closedS = []

	if SOLVED[str(s)] == False:
		openS.append(s)
	while len(openS)!=0:
		s = openS.pop()
		closedS.append(s)


		if residual(s, domainR, domain, problem, H, V) > error:
			rv = False

		[a,P] = greedy_action(s, domainR, domain, problem, H, V)

		SUCC = [p[2] for p in P]
		
		for s1 in SUCC:
			
			union = openS + closedS

			flag = False

			for st in union:
				if TMP[s1].issubset(st):
					flag = True
					break

			if SOLVED.get(s1,False) == False and flag == False:  
				openS.append(TMP[s1])

	if rv==True:
		for s1 in closedS:
			SOLVED[str(s1)] = True
	else:
		while len(closedS)!=0:
			s = closedS.pop()
			update(s,domainR, domain, problem, H, V)

	return rv

def greedy_action(s, domainR,  domain, problem, H, V):

	###print("--------------GREEDY ACTION--------------	")

	ACT_VALUE  = float('inf')
	ACT = None
	Pt = {}

	for a in domain.operators:



		[S,A,P] = expand_state(s, a , problem.objects)

		for s in S:
			if str(s) not in H:

				if heuristics_type=="0":
					H[str(s)] = 0
				if heuristics_type=="h_ff":

					H[str(s)] = h_ff(domainR, problem, s, problem.goal)
				
				if heuristics_type=="h_add":
					
					value = h_add(domainR, problem, s, problem.goal)
					if value==float("inf"):
					
						H[str(s)] = 0
					else:
						H[str(s)] = value


		for ins_a in A:
	
			v = qValue(s, ins_a, P, H, V )
			
			if v < ACT_VALUE:

				Pt.clear()


				ACT = ins_a
				ACT_VALUE = v
				
				for i in P:
					if str(P[i][1].precond) == str(ins_a.precond):
						Pt[i] = P[i]

						

	
	return [ACT,Pt]

def qValue(s,a, P, H, V):

	cost = 1
	suma = 0 	



	for i in P:


		suma = suma + P[i][0]*V.get(i[2], H[i[2]]	  )
		#suma = suma + P[i][0]*V.get(i[2], 1)



	return cost + suma

def update(s,domainR, domain, problem, H, V):
	[a,P] = greedy_action(s,domainR, domain, problem, H, V)


	
	V[str(s)] = qValue(s,a, P, H, V)

def pick_next_state(s,a, P):



	if len(P)==0:
		return False




	elements = [p[2] for p in P]
	probabilities = [P[p][0] for p in P]



	s1 = np.random.choice(elements, 1, p=probabilities)


	#s1 = set(s1)

	return TMP[s1[0]]

def residual(s,domainR, domain, problem, H, V):
	[a,P] = greedy_action(s,domainR, domain, problem, H, V)
	r = abs(V.get(str(s),0) - qValue(s,a, P, H, V))
	####print(r)
	return r










def main(argv):
	
	path_domain = argv[0]
	path_problem = argv[1]

	global heuristics_type 
	heuristics_type= argv[2]

	domain  = PDDLParser.parse(path_domain)
	problem = PDDLParser.parse(path_problem)

	domainR = relaxProblem(domain)

	V ={}
	H ={}

	lrtdp(domain, problem , 0.0, H, V)

if __name__ == "__main__":
	main(sys.argv[1:])


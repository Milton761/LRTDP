from copy import deepcopy
import math

def tam_instancesH(vector_param_len):

	final_tam = 1
	for tam in vector_param_len:
		final_tam = final_tam*tam
	
	return final_tam

def gen_all_combinationsH(headers_types ,objects):

	#print("init function")


	if len(headers_types) == 0:
		return []

	vector_freq = []
	instances_values = []
	index = []
	num_values = []
	keys = {}

	i=0
	for tp in headers_types:
		num_values.append(len(objects[tp]))
		index.append(0)
		keys[i] = tp
		i = i+1


		#print(tp)
	#print(num_values)
	#print(len(num_values))
	for i in range(1,len(num_values)):

		n = num_values[i]
		for j in range(i+1, len(num_values)):
			n = n*num_values[j]

		vector_freq.append(n)

		#print('here',i)

	vector_freq.append(1)

	#print(vector_freq)
	#print(index)

	full_tam = tam_instancesH(num_values)
	#print(full_tam)

	for i in range(full_tam):

		posb = [None]*len(vector_freq)

		for j in range(len(vector_freq)):
			

			posb[j] = objects[keys[j]][index[j]]

			if (i+1)%vector_freq[j] == 0:
				index[j] = (index[j]+1)%num_values[j]


		instances_values.append(posb)




	#print("end function")
	return instances_values

def instantiate_actionH(action, objects):

	number_params = len(action.params)

	var_names = [] 
	#var_names contains the name of the arg variables : ['?x', '?y', ...]
	for var in action.params:
		var_names.append(var.name)
	#print(var_names)

	headers = []

	for par in action.params:
		headers.append(par.type)

	#print(headers)

	all_values_instances = gen_all_combinationsH(headers, objects)
	

	R = []

	for i in range(len(all_values_instances)):

		temp_action = deepcopy(action)

		for index in range(len(action.params)):
			temp_action.params[index]._value = all_values_instances[i][index]
		
		R.append(temp_action)	
		#print('')


	for action in R:


		#change with a dict
		h = []
		v = []
		for i in range(len(action.params)):
			h.append(action.params[i].name)
			v.append(action.params[i].value)
		

		#print('-------------PRECONDITION---------------------')
	
		

		for i in range(len(action.precond)):

			literal =  action.precond[i]
			subs = {}
			for j in range(literal._predicate.arity):
				subs[literal._predicate.args[j]] = v[h.index(literal._predicate.args[j])]

			
			literal._predicate = literal._predicate.ground(subs)

		#	print(literal._predicate, literal.is_positive())

		#print('-------------EFFECT---------------------')

		for i in range(len(action.effects)):
			literal =  action.effects[i]
			subs = {}
			for j in range(literal._predicate.arity):
				subs[literal._predicate.args[j]] = v[h.index(literal._predicate.args[j])]

			literal._predicate = literal._predicate.ground(subs)

		#	print(literal._predicate, literal.is_positive())


	return R

def ver_precondH(precs, state):
	

	IS_VALID = True

	for p in precs:
		


		if p._predicate.name == '=':

			X = p._predicate.args[0]
			Y = p._predicate.args[1]


			if (str(X)==str(Y)) == p.is_positive():
				IS_VALID = True
			else:
				IS_VALID = False
				break

		else:

			if (str(p) in state):
				IS_VALID = True
			else:
				IS_VALID = False
				break;


	return IS_VALID

def generate_new_stateH(eff,state):

	#print(state)

	for ef in eff:


		if ef.is_positive():
			state = state.union({str(ef)})
		else:
			state = state.difference({str(ef._predicate)})

	#print(state)

	return state

def expand_stateH(state, action, objects):

	STATES = []

	ACT = []
	#state is a new posible state (an action instantiate)
	#verify if the new state is valid with the preconditions
	#if is valid update the effects and add in STATES


	#print(state)
	#print(objects)

	pos_states = instantiate_actionH(action, objects)

	for st in pos_states:

		precs =  st.precond

		if ver_precondH(precs, state) == True:

			new_s  = generate_new_stateH(st.effects, state)

			STATES.append(new_s)

			ACT.append(st)

	return [STATES,ACT]


##--------utils for EP2 --------------------------

#domain that ignore negative effects
def relaxProblemH(domain):

	relaxP = deepcopy(domain)

	for action in relaxP.operators:

		relaxEff = [effect for effect in action.effects if effect.is_positive()]
		action._effects = relaxEff

	return relaxP


def firstLevelH(var, listVar):

	level = 0
	for Var in listVar:
		if var in Var:
			return level
		level = level + 1
	return -1

#-------------------




def h_ff(domain, problem , current_state, goal_state):


		relaxP = relaxProblemH(domain)
		A = [None]
		F = []
		F.append(current_state)
		t = 0

	
		

		while goal_state.issubset(F[t]) == False:

			t = t+1

			A_t = []
			for action in relaxP.operators:

				all_pos_action = instantiate_actionH(action, problem.objects)

				

				for act in all_pos_action:
					if ver_precondH(act.precond, F[t-1]):
						A_t.append(act)
		
			A.append(A_t)
			F.append(deepcopy(F[t-1]))	
			for act in A[t]:

				F[t] = generate_new_stateH(act.effects, F[t])

			if F[t] ==	 F[t-1]:
				#print("Failure!!")
				return float('inf')

		#print([F,A])

		#Extracting a Relaxed Plan

		result = 0

		if goal_state.issubset(F[-1]) == False:
			print("Failure in Extracting a Relaxed Plan H_FF")
			return 

		list_levels = []
		for g in goal_state:
			list_levels.append(firstLevelH(g,F))



		M = max(list_levels)

		G = {}
		for t in range(M+1):

			G[t] = []


			for g in goal_state:
				if firstLevelH(g,F) == t:
					G[t].append(g)

		
		for t in range(M,0,-1):

			#print("++++++++++++++++++++++++++++++++++++++ ", t)
			#input()

			for g_t in G[t]:

				a = None
				flag = False

				for i in range(1,len(A)):
					A_t = A[i]

					#print("ACtions ", A_t)

					for act in A_t:

						effects = []

						for eff in act.effects:
							effects.append(str(eff))

						#print("Gt ",g_t)
						#print("Effects", effects)
						#input()

						if g_t in effects:
							a = act
							result = result + 1
							flag = True
							break
					if flag:
						break


				for p in a.precond:
					
					

					if p._predicate.name!="=":
						#print("Index ", G[relaxProblemH(str(p),F)])
						G[firstLevelH(str(p),F)] = list(set().union(G[firstLevelH(str(p),F)],[str(p)]))


		#print("END", result)
		#input()
		return result

def h_add(domain, problem, current_state, goal_state):

	#optimize for relax the problem just once time
	relaxP = relaxProblemH(domain)

	#s = goal_state
	H = {} 


	##init values for the DP

	for p in goal_state:

		if p in current_state:
			H[p] = 0
		else:
			H[p] = float("inf")

	##end init values

	U = deepcopy(current_state)
	#print('U', U)
	
	while True:
		
		U_before = deepcopy(U)

		#print('U_before', U_before)
		#print('H',H)
		#input()

		for action in relaxP.operators:

			#print('for action', str(action))


			all_pos_action = instantiate_actionH(action, problem.objects)

			for act in all_pos_action:



				if ver_precondH(act.precond, U):

					#print("ACTION PASS : ", str(act))

					U = generate_new_stateH(act.effects, U)

					for p in act.effects:

						#print(p)

						to_sum = []

						for q in act.precond:
							
							if q in H:
								to_sum.append(H[str(q)])
							else:
								to_sum.append(0)


						if p not in H:
							H[str(p)] = float("inf")

						H[str(p)] = min( H[str(p)], 1 +  sum( to_sum ) )

	
		if U_before == U:
			
			break



	return sum( [H.get(p,0) for p in current_state] )

	



	

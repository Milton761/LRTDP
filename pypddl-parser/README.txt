Authors:
Milton Condori
Henrique Donancio

To execute:

python3 ./lrtdp.py <domain> <problem> <heuristic>

heuristic - types:
	0
	h_ff
	h_add
example:

$>  python3 ./lrtdp.py pddl/triangle-tireworld/domain.ppddl pddl/triangle-tireworld/problems/p01.ppddl 0

$>  python3 ./lrtdp.py pddl/triangle-tireworld/domain.ppddl pddl/triangle-tireworld/problems/p01.ppddl h_ff

$>  python3 ./lrtdp.py pddl/triangle-tireworld/domain.ppddl pddl/triangle-tireworld/problems/p01.ppddl h_add
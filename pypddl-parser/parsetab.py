
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'NAME VARIABLE PROBABILITY LPAREN RPAREN HYPHEN EQUALS DEFINE_KEY DOMAIN_KEY REQUIREMENTS_KEY STRIPS_KEY EQUALITY_KEY TYPING_KEY PROBABILISTIC_EFFECTS_KEY TYPES_KEY PREDICATES_KEY ACTION_KEY PARAMETERS_KEY PRECONDITION_KEY EFFECT_KEY AND_KEY NOT_KEY PROBABILISTIC_KEY PROBLEM_KEY OBJECTS_KEY INIT_KEY GOAL_KEYpddl : domain\n            | problemdomain : LPAREN DEFINE_KEY domain_def require_def types_def predicates_def action_def_lst RPARENproblem : LPAREN DEFINE_KEY problem_def domain_def objects_def init_def goal_def RPARENdomain_def : LPAREN DOMAIN_KEY NAME RPARENproblem_def : LPAREN PROBLEM_KEY NAME RPARENobjects_def : LPAREN OBJECTS_KEY typed_constants_lst RPARENinit_def : LPAREN INIT_KEY LPAREN AND_KEY ground_predicates_lst RPAREN RPAREN\n                | LPAREN INIT_KEY ground_predicates_lst RPARENgoal_def : LPAREN GOAL_KEY LPAREN AND_KEY ground_predicates_lst RPAREN RPARENrequire_def : LPAREN REQUIREMENTS_KEY require_key_lst RPARENrequire_key_lst : require_key require_key_lst\n                       | require_keyrequire_key : STRIPS_KEY\n                   | EQUALITY_KEY\n                   | TYPING_KEY\n                   | PROBABILISTIC_EFFECTS_KEYtypes_def : LPAREN TYPES_KEY names_lst RPARENpredicates_def : LPAREN PREDICATES_KEY predicate_def_lst RPARENpredicate_def_lst : predicate_def predicate_def_lst\n                         | predicate_defpredicate_def : LPAREN NAME typed_variables_lst RPAREN\n                     | LPAREN NAME RPARENaction_def_lst : action_def action_def_lst\n                      | action_defaction_def : LPAREN ACTION_KEY NAME parameters_def action_def_body RPARENparameters_def : PARAMETERS_KEY LPAREN typed_variables_lst RPAREN\n                      | PARAMETERS_KEY LPAREN RPARENaction_def_body : precond_def effects_defprecond_def : PRECONDITION_KEY LPAREN AND_KEY literals_lst RPAREN\n                   | PRECONDITION_KEY literaleffects_def : EFFECT_KEY LPAREN AND_KEY effects_lst RPAREN\n                   | EFFECT_KEY effecteffects_lst : effect effects_lst\n                   | effecteffect : literal\n              | LPAREN PROBABILISTIC_KEY PROBABILITY literal RPARENliterals_lst : literal literals_lst\n                    | literalliteral : LPAREN NOT_KEY predicate RPAREN\n               | predicateground_predicates_lst : ground_predicate ground_predicates_lst\n                             | ground_predicatepredicate : LPAREN NAME variables_lst RPAREN\n                 | LPAREN EQUALS VARIABLE VARIABLE RPAREN\n                 | LPAREN NAME RPARENground_predicate : LPAREN NAME constants_lst RPAREN\n                        | LPAREN NAME RPARENtyped_constants_lst : constants_lst HYPHEN type typed_constants_lst\n                           | constants_lst HYPHEN typetyped_variables_lst : variables_lst HYPHEN type typed_variables_lst\n                           | variables_lst HYPHEN typeconstants_lst : constant constants_lst\n                     | constantvariables_lst : VARIABLE variables_lst\n                     | VARIABLEnames_lst : NAME names_lst\n                 | NAMEtype : NAMEconstant : NAME'
    
_lr_action_items = {'VARIABLE':([73,77,87,96,110,116,118,130,],[-59,87,87,87,87,87,130,139,]),'DEFINE_KEY':([3,],[5,]),'PROBABILISTIC_EFFECTS_KEY':([21,30,31,32,34,35,],[35,-14,35,-16,-15,-17,]),'PARAMETERS_KEY':([75,],[85,]),'REQUIREMENTS_KEY':([14,],[21,]),'ACTION_KEY':([47,],[63,]),'GOAL_KEY':([37,],[52,]),'EFFECT_KEY':([94,105,106,126,135,136,138,143,],[104,-31,-41,-46,-40,-44,-30,-45,]),'NAME':([11,12,24,27,40,41,43,55,58,63,65,69,71,73,74,97,107,114,124,129,133,],[17,18,41,43,41,-60,43,71,73,75,77,71,41,-59,41,73,116,116,116,116,116,]),'EQUALITY_KEY':([21,30,31,32,34,35,],[34,-14,34,-16,-15,-17,]),'LPAREN':([0,5,6,8,10,13,15,20,22,25,26,28,38,45,48,50,52,53,56,60,66,70,72,76,79,81,85,89,91,95,99,101,102,104,106,113,115,117,121,126,127,131,134,135,136,143,144,],[3,7,9,14,16,19,23,29,37,-6,-5,47,55,47,65,-11,67,69,-7,-18,65,-9,69,-19,69,-48,96,-23,-47,107,-22,-8,-26,114,-41,-36,124,129,133,-46,129,133,129,-40,-44,-45,-37,]),'HYPHEN':([40,41,42,57,86,87,98,],[-54,-60,58,-53,97,-56,-55,]),'EQUALS':([107,114,124,129,133,],[118,118,118,118,118,]),'$end':([1,2,4,51,62,],[0,-1,-2,-4,-3,]),'PREDICATES_KEY':([29,],[48,]),'PROBLEM_KEY':([7,],[11,]),'OBJECTS_KEY':([16,],[24,]),'STRIPS_KEY':([21,30,31,32,34,35,],[30,-14,30,-16,-15,-17,]),'RPAREN':([17,18,30,31,32,33,34,35,36,39,40,41,43,44,45,46,49,53,54,57,59,61,64,66,68,71,73,74,77,78,80,81,82,83,87,88,89,90,91,92,93,96,98,99,100,102,103,106,108,110,111,112,113,116,120,123,125,126,127,128,131,132,135,136,137,139,140,141,142,143,144,],[25,26,-14,-13,-16,50,-15,-17,51,56,-54,-60,-58,60,-25,62,-12,-43,70,-53,-57,-24,76,-21,-42,81,-59,-50,89,-20,91,-48,92,-49,-56,99,-23,100,-47,101,102,109,-55,-22,111,-26,-29,-41,119,-52,-10,-33,-36,126,-51,135,136,-46,-39,138,-35,141,-40,-44,-38,143,-34,-32,144,-45,-37,]),'TYPES_KEY':([19,],[27,]),'DOMAIN_KEY':([7,9,],[12,12,]),'AND_KEY':([55,67,107,114,],[72,79,117,121,]),'NOT_KEY':([107,114,129,133,],[115,115,115,115,]),'INIT_KEY':([23,],[38,]),'PROBABILITY':([122,],[134,]),'PROBABILISTIC_KEY':([114,133,],[122,122,]),'TYPING_KEY':([21,30,31,32,34,35,],[32,-14,32,-16,-15,-17,]),'PRECONDITION_KEY':([84,109,119,],[95,-28,-27,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'literal':([95,104,117,121,127,131,134,],[105,113,127,113,127,113,142,]),'objects_def':([10,],[15,]),'problem':([0,],[4,]),'goal_def':([22,],[36,]),'require_def':([8,],[13,]),'predicate':([95,104,115,117,121,127,131,134,],[106,106,123,106,106,106,106,106,]),'predicates_def':([20,],[28,]),'variables_lst':([77,87,96,110,116,],[86,98,86,86,125,]),'action_def':([28,45,],[45,45,]),'type':([58,97,],[74,110,]),'predicate_def':([48,66,],[66,66,]),'action_def_body':([84,],[93,]),'effects_def':([94,],[103,]),'init_def':([15,],[22,]),'predicate_def_lst':([48,66,],[64,78,]),'constants_lst':([24,40,71,74,],[42,57,80,42,]),'domain_def':([5,6,],[8,10,]),'effect':([104,121,131,],[112,131,131,]),'typed_constants_lst':([24,74,],[39,83,]),'constant':([24,40,71,74,],[40,40,40,40,]),'typed_variables_lst':([77,96,110,],[88,108,120,]),'literals_lst':([117,127,],[128,137,]),'require_key_lst':([21,31,],[33,49,]),'problem_def':([5,],[6,]),'ground_predicates_lst':([38,53,72,79,],[54,68,82,90,]),'require_key':([21,31,],[31,31,]),'pddl':([0,],[1,]),'types_def':([13,],[20,]),'ground_predicate':([38,53,72,79,],[53,53,53,53,]),'effects_lst':([121,131,],[132,140,]),'action_def_lst':([28,45,],[46,61,]),'parameters_def':([75,],[84,]),'domain':([0,],[2,]),'precond_def':([84,],[94,]),'names_lst':([27,43,],[44,59,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> pddl","S'",1,None,None,None),
  ('pddl -> domain','pddl',1,'p_pddl','pddlparser.py',128),
  ('pddl -> problem','pddl',1,'p_pddl','pddlparser.py',129),
  ('domain -> LPAREN DEFINE_KEY domain_def require_def types_def predicates_def action_def_lst RPAREN','domain',8,'p_domain','pddlparser.py',134),
  ('problem -> LPAREN DEFINE_KEY problem_def domain_def objects_def init_def goal_def RPAREN','problem',8,'p_problem','pddlparser.py',139),
  ('domain_def -> LPAREN DOMAIN_KEY NAME RPAREN','domain_def',4,'p_domain_def','pddlparser.py',144),
  ('problem_def -> LPAREN PROBLEM_KEY NAME RPAREN','problem_def',4,'p_problem_def','pddlparser.py',149),
  ('objects_def -> LPAREN OBJECTS_KEY typed_constants_lst RPAREN','objects_def',4,'p_objects_def','pddlparser.py',154),
  ('init_def -> LPAREN INIT_KEY LPAREN AND_KEY ground_predicates_lst RPAREN RPAREN','init_def',7,'p_init_def','pddlparser.py',159),
  ('init_def -> LPAREN INIT_KEY ground_predicates_lst RPAREN','init_def',4,'p_init_def','pddlparser.py',160),
  ('goal_def -> LPAREN GOAL_KEY LPAREN AND_KEY ground_predicates_lst RPAREN RPAREN','goal_def',7,'p_goal_def','pddlparser.py',168),
  ('require_def -> LPAREN REQUIREMENTS_KEY require_key_lst RPAREN','require_def',4,'p_require_def','pddlparser.py',173),
  ('require_key_lst -> require_key require_key_lst','require_key_lst',2,'p_require_key_lst','pddlparser.py',178),
  ('require_key_lst -> require_key','require_key_lst',1,'p_require_key_lst','pddlparser.py',179),
  ('require_key -> STRIPS_KEY','require_key',1,'p_require_key','pddlparser.py',187),
  ('require_key -> EQUALITY_KEY','require_key',1,'p_require_key','pddlparser.py',188),
  ('require_key -> TYPING_KEY','require_key',1,'p_require_key','pddlparser.py',189),
  ('require_key -> PROBABILISTIC_EFFECTS_KEY','require_key',1,'p_require_key','pddlparser.py',190),
  ('types_def -> LPAREN TYPES_KEY names_lst RPAREN','types_def',4,'p_types_def','pddlparser.py',195),
  ('predicates_def -> LPAREN PREDICATES_KEY predicate_def_lst RPAREN','predicates_def',4,'p_predicates_def','pddlparser.py',200),
  ('predicate_def_lst -> predicate_def predicate_def_lst','predicate_def_lst',2,'p_predicate_def_lst','pddlparser.py',205),
  ('predicate_def_lst -> predicate_def','predicate_def_lst',1,'p_predicate_def_lst','pddlparser.py',206),
  ('predicate_def -> LPAREN NAME typed_variables_lst RPAREN','predicate_def',4,'p_predicate_def','pddlparser.py',214),
  ('predicate_def -> LPAREN NAME RPAREN','predicate_def',3,'p_predicate_def','pddlparser.py',215),
  ('action_def_lst -> action_def action_def_lst','action_def_lst',2,'p_action_def_lst','pddlparser.py',223),
  ('action_def_lst -> action_def','action_def_lst',1,'p_action_def_lst','pddlparser.py',224),
  ('action_def -> LPAREN ACTION_KEY NAME parameters_def action_def_body RPAREN','action_def',6,'p_action_def','pddlparser.py',232),
  ('parameters_def -> PARAMETERS_KEY LPAREN typed_variables_lst RPAREN','parameters_def',4,'p_parameters_def','pddlparser.py',237),
  ('parameters_def -> PARAMETERS_KEY LPAREN RPAREN','parameters_def',3,'p_parameters_def','pddlparser.py',238),
  ('action_def_body -> precond_def effects_def','action_def_body',2,'p_action_def_body','pddlparser.py',246),
  ('precond_def -> PRECONDITION_KEY LPAREN AND_KEY literals_lst RPAREN','precond_def',5,'p_precond_def','pddlparser.py',251),
  ('precond_def -> PRECONDITION_KEY literal','precond_def',2,'p_precond_def','pddlparser.py',252),
  ('effects_def -> EFFECT_KEY LPAREN AND_KEY effects_lst RPAREN','effects_def',5,'p_effects_def','pddlparser.py',260),
  ('effects_def -> EFFECT_KEY effect','effects_def',2,'p_effects_def','pddlparser.py',261),
  ('effects_lst -> effect effects_lst','effects_lst',2,'p_effects_lst','pddlparser.py',269),
  ('effects_lst -> effect','effects_lst',1,'p_effects_lst','pddlparser.py',270),
  ('effect -> literal','effect',1,'p_effect','pddlparser.py',278),
  ('effect -> LPAREN PROBABILISTIC_KEY PROBABILITY literal RPAREN','effect',5,'p_effect','pddlparser.py',279),
  ('literals_lst -> literal literals_lst','literals_lst',2,'p_literals_lst','pddlparser.py',287),
  ('literals_lst -> literal','literals_lst',1,'p_literals_lst','pddlparser.py',288),
  ('literal -> LPAREN NOT_KEY predicate RPAREN','literal',4,'p_literal','pddlparser.py',296),
  ('literal -> predicate','literal',1,'p_literal','pddlparser.py',297),
  ('ground_predicates_lst -> ground_predicate ground_predicates_lst','ground_predicates_lst',2,'p_ground_predicates_lst','pddlparser.py',305),
  ('ground_predicates_lst -> ground_predicate','ground_predicates_lst',1,'p_ground_predicates_lst','pddlparser.py',306),
  ('predicate -> LPAREN NAME variables_lst RPAREN','predicate',4,'p_predicate','pddlparser.py',314),
  ('predicate -> LPAREN EQUALS VARIABLE VARIABLE RPAREN','predicate',5,'p_predicate','pddlparser.py',315),
  ('predicate -> LPAREN NAME RPAREN','predicate',3,'p_predicate','pddlparser.py',316),
  ('ground_predicate -> LPAREN NAME constants_lst RPAREN','ground_predicate',4,'p_ground_predicate','pddlparser.py',326),
  ('ground_predicate -> LPAREN NAME RPAREN','ground_predicate',3,'p_ground_predicate','pddlparser.py',327),
  ('typed_constants_lst -> constants_lst HYPHEN type typed_constants_lst','typed_constants_lst',4,'p_typed_constants_lst','pddlparser.py',335),
  ('typed_constants_lst -> constants_lst HYPHEN type','typed_constants_lst',3,'p_typed_constants_lst','pddlparser.py',336),
  ('typed_variables_lst -> variables_lst HYPHEN type typed_variables_lst','typed_variables_lst',4,'p_typed_variables_lst','pddlparser.py',344),
  ('typed_variables_lst -> variables_lst HYPHEN type','typed_variables_lst',3,'p_typed_variables_lst','pddlparser.py',345),
  ('constants_lst -> constant constants_lst','constants_lst',2,'p_constants_lst','pddlparser.py',353),
  ('constants_lst -> constant','constants_lst',1,'p_constants_lst','pddlparser.py',354),
  ('variables_lst -> VARIABLE variables_lst','variables_lst',2,'p_variables_lst','pddlparser.py',362),
  ('variables_lst -> VARIABLE','variables_lst',1,'p_variables_lst','pddlparser.py',363),
  ('names_lst -> NAME names_lst','names_lst',2,'p_names_lst','pddlparser.py',371),
  ('names_lst -> NAME','names_lst',1,'p_names_lst','pddlparser.py',372),
  ('type -> NAME','type',1,'p_type','pddlparser.py',382),
  ('constant -> NAME','constant',1,'p_constant','pddlparser.py',387),
]

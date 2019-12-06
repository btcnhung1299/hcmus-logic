import itertools

from fact import Fact
from unify import unify
from substitution import Substitution

def subst(facts_1, facts_2):           # Generalized Modus Ponens
   if len(facts_1) != len(facts_2):
      return False

   facts_1.sort()
   facts_2.sort()
   for f1, f2 in zip(facts_1, facts_2):
      if f1.get_op() != f2.get_op():
         return False

   print('here')
   print('facts_1', *facts_1)
   print('facts_2', *facts_2) 
   return unify(facts_1, facts_2, Substitution())

def forward_chaining(kb, alpha):
   facts = set(kb.facts)
   rules = kb.rules

   for i in range(1):
      new_facts = set()

      for rule in rules:
         num_facts = rule.num_conditions()
         print('! Consider rule:', rule)

         for comb_facts in list(itertools.combinations(facts, num_facts)):
            existed_facts = [fact for fact in comb_facts]
            theta = subst(rule.lhs, existed_facts)
            if not theta:
               continue
            print('yeahhh')
            print(theta)         

"""
            theta = Fact.gmp(rule.lhs(), existed_facts)
            if not theta:
               continue
            theta = Substitute(mappings=theta)
            new_fact = theta.substitute(rule.rhs())


         theta = unify(rule, alpha, Substitute):
         if not theta:
            continue

         new_conclusion = theta.substitute(rule.conclusion)
         if new_conclusion not in new_facts:
            new_facts.add(new_conclusion)
            phi = unify(new_conclusion, alpha)
            if not phi:
               return phi

      facts.union(new_facts) 
"""

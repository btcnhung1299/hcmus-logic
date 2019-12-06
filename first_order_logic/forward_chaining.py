from unify import unify
from substitution import Substitution

def forward_chaining(kb, alpha):
   facts = set(kb.facts)
   rules = kb.rules   

   print('----------- Facts: ----------------')
   print(*facts, sep='\n')
   print('----------- Rules: ----------------')
   print(*rules, sep='\n')
"""
   while True:
      new_facts = set()
      for rule in rules:
         theta = Substitute()
         theta.mappings = unify(rule, alpha, theta.mappings):
         new_conclusion = theta.substitute(rule.conclusion)

         if new_conclusion not in new_facts:
            new_facts.add(new_conclusion)
            phi = unify(new_conclusion, alpha)
            if not phi:
               return phi

      facts.union(new_facts)        
""" 

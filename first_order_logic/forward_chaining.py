import itertools

from fact import Fact
from unify import unify
from substitution import Substitution

def subst(facts_1, facts_2):           # Generalized Modus Ponens
   if len(facts_1) != len(facts_2):
      return False

   for f1, f2 in zip(facts_1, facts_2):
      if f1.get_op() != f2.get_op():
         return False

   return unify(facts_1, facts_2, Substitution())

def forward_chaining(kb, alpha):
   res = set()
   # Pre-check if current facts are enough to answer
   for fact in kb.facts:
      phi = unify(fact, alpha, Substitution())
      if phi:
         if phi.empty():
            res.add('true')
            return res
         res.add(phi)

   last_generated_facts = kb.facts.copy()

   while True:
      new_facts = set()
 
      # Optimize: Incremental forward chaining
      # At iteration t, check a rule only if its premises includes at least
      # a conjunct pi that unified with the fact pi' newly inferred at iteration t - 1
      for rule in kb.rules:
         if not rule.may_triggered(last_generated_facts):
            continue

         num_premises = rule.get_num_premises()
         # Get facts that relevant to the current rule
         potential_facts = kb.get_potential_facts(rule)

         # Check if rule contains premises with the same predicate
         if not rule.dup_predicate:        
            potential_premises = itertools.combinations(sorted(potential_facts), num_premises)
         else:
            # Assumption on order of premises may failed on something like grandparent rule with two parent relations
            potential_premises = itertools.permutations(potential_facts, num_premises)

         for tuple_premises in potential_premises:
            premises = [premise for premise in tuple_premises]
            theta = subst(rule.premises, premises)
            if not theta:
               continue
                        
            new_fact = rule.conclusion.copy()
            theta.substitute(new_fact)
            
            if new_fact not in new_facts and new_fact not in kb.facts:
               new_facts.add(new_fact)
               phi = unify(new_fact, alpha, Substitution())
               if phi:
                  if phi.empty():
                     kb.facts.update(new_facts)
                     res.add('true')
                     return res
                  res.add(phi)

      last_generated_facts = new_facts
      if not new_facts:
         if not res:
            res.add('false')
         return res
      kb.facts.update(new_facts)

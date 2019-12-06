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

   return unify(facts_1, facts_2, Substitution())

def forward_chaining(kb, alpha):
   facts = set(kb.facts)
   rules = kb.rules

   while True:
      new_facts = set()

      for rule in rules:
         num_facts = rule.num_conditions()

         for comb_facts in list(itertools.combinations(facts, num_facts)):
            existed_facts = [fact for fact in comb_facts]
            theta = subst(rule.lhs, existed_facts)
            if not theta:
               continue

            new_fact = rule.rhs.copy()
            theta.substitute(new_fact)

            if new_fact not in new_facts:
               new_facts.add(new_fact)
               phi = unify(new_fact, alpha, Substitution())
               if phi:
                  return phi

      facts.update(new_facts)


import itertools

from fact import Fact
from unify import unify
from substitution import Substitution

def subst(facts_1, facts_2):           # Generalized Modus Ponens
   # Suppose that facts_1 and facts_2 are sorted ascendingly
   if len(facts_1) != len(facts_2):
      return False

   for f1, f2 in zip(facts_1, facts_2):
      if f1.get_op() != f2.get_op():
         return False

   return unify(facts_1, facts_2, Substitution())

def forward_chaining(kb, alpha):
   # Pre-check if current facts are enough to answer
   for fact in kb.facts:
      phi = unify(fact, alpha, Substitution())
      if phi:
         yield phi

   last_generated_facts = kb.facts.copy()

   while True:
      new_facts = set()
      kb.facts = set(kb.facts)
 
      # Incremental: At iteration t, check a rule only if its premises includes
      # a conjunct pi that unified with the fact pi' newly inferred at iteration t - 1
      for rule in kb.rules:
         if not rule.may_triggered(last_generated_facts):
            continue

         # Find all pattern matching
         num_premises = rule.get_num_premises()
         for comb_facts in itertools.combinations(sorted(kb.facts), num_premises):
            existed_facts = [fact for fact in comb_facts]
            theta = subst(rule.premises, existed_facts)
            if not theta:
               continue
                        
            new_fact = rule.conclusion.copy()
            theta.substitute(new_fact)
            
            if new_fact not in new_facts:
               new_facts.add(new_fact)
               phi = unify(new_fact, alpha, Substitution())
               if phi:
                  kb.facts.update(new_facts)
                  yield phi

      last_generated_facts = new_facts.difference(kb.facts)
      if not last_generated_facts:
         return False
      kb.facts.update(last_generated_facts)

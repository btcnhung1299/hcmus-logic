from unify import unify

def forward_chaining(kb, alpha):
   facts = set(kb.facts)
   rules = kb.rules   

   while True:
      new_facts = set()
      for rule in rules:
         for theta in unify(rule, alpha):
            new_conclusion = substitute(theta, rule.conclusion)
     
   

      if not new_facts:
         return False

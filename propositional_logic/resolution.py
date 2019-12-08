import itertools

from clause import Clause

def resolution(kb, alpha):
   steps = []
   entail = False
   alpha.negate()
   clauses = set(kb.clauses)
   clauses.add(alpha) 

   while True:
      new_clauses = set()

      for (ci, cj) in itertools.combinations(sorted(clauses), 2):
         resolvents, contradict = Clause.resolve(ci, cj)
         new_clauses.update(resolvents)
         entail |= contradict

      generated_clauses = sorted(new_clauses.difference(clauses))
      steps.append(generated_clauses)
      clauses.update(new_clauses)

      if entail:
         return True, steps
      if not generated_clauses:
         return False, steps

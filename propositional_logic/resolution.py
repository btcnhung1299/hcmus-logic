import itertools

from clause import Clause

def resolution(kb, alpha):
   steps = []
   alpha.negate()
   clauses = set(kb.clauses)
   clauses.add(alpha) 

   while True:
      new_clauses = set()

      for (ci, cj) in itertools.combinations(sorted(clauses), 2):
         resolvents, contradict = Clause.resolve(ci, cj)
         new_clauses.update(resolvents)

         if contradict:
            generated_clauses = sorted(new_clauses.difference(clauses))
            steps.append(generated_clauses)
            return True, steps

      generated_clauses = sorted(new_clauses.difference(clauses))
      steps.append(generated_clauses)
      
      if len(generated_clauses) == 0:
         return False, steps

      clauses.update(new_clauses)

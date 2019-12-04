import itertools

from clause import Clause

def resolution(kb, alpha):
   list_new_clauses = []
   alpha.negate()
   clauses = set(kb.clauses)
   clauses.add(alpha) 

   while True:
      new_clauses = set()

      for (ci, cj) in itertools.combinations(clauses, 2):
         resolvents, contradict = Clause.resolve(ci, cj)
         if contradict:
            list_new_clauses.append(new_clauses.difference(clauses))
            return True, list_new_clauses
         new_clauses.update(resolvents)

      list_new_clauses.append(new_clauses.difference(clauses))
      if new_clauses.issubset(clauses):
         return False, list_new_clauses
      clauses.update(new_clauses)


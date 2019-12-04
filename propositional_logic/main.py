from knowledge_base import KnowledgeBase
from clause import Clause
from resolution import resolution

kb = KnowledgeBase()
inp_file = '../test/02.txt'

with open(inp_file, 'r') as f:
   alpha = Clause.parse_clause(f.readline())
   num_clauses = f.readline()
   clauses = f.readlines()
   KnowledgeBase.declare(kb, clauses)
f.close()

print('----------------- KNOWLEDGE BASE -----------------')
print('Number of clauses in KB:', len(kb.clauses))
for clause in kb.clauses:
   print('# {}'.format(clause))


print('----------------- RESOLUTION -----------------')
entail, new_clauses = resolution(kb, alpha)

outp_file = '../test/02.out'

with open(outp_file, 'w') as f:
   for clauses in new_clauses:
      f.write('{}\n'.format(len(clauses)))
      for clause in clauses:
         f.write('{}\n'.format(clause))
   f.write('{}'.format('YES' if entail else 'NO'))

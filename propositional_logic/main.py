from knowledge_base import KnowledgeBase
from clause import Clause
from resolution import resolution

# Edit input and output file here
test_case = input().strip()
inp_file = 'test/' + test_case + '.txt'
outp_file = 'test/' + test_case + '_out.txt'

kb = KnowledgeBase()
with open(inp_file, 'r') as f:
   alpha = Clause.parse_clause(f.readline())
   num_clauses = f.readline()
   clauses = f.readlines()
   KnowledgeBase.declare(kb, clauses)
f.close()

print('Done reading from', inp_file)

entail, new_clauses = resolution(kb, alpha)

with open(outp_file, 'w') as f:
   for clauses in new_clauses:
      f.write('{}\n'.format(len(clauses)))
      for clause in clauses:
         f.write('{}\n'.format(clause))
   f.write('{}'.format('YES' if entail else 'NO'))

print('Done writing to', outp_file)

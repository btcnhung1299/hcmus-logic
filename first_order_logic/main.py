from knowledge_base import KnowledgeBase
from fact import Fact

test_number = '02'
inp_file = 'test/' + test_number + '/profound_knowledge.pl'
query_file = 'test/' + test_number + '/query.pl'
outp_file = 'test/' + test_number + '/answers.pl'

kb = KnowledgeBase()
with open(inp_file, 'r') as f_in:
   list_sentences = f_in.readlines()
   KnowledgeBase.declare(kb, list_sentences)
print('Done initialize knowledge base from {}.'.format(inp_file))

with open(query_file, 'r') as f_query:
   with open(outp_file, 'w') as f_out:
      for query_str in f_query.readlines():
         alpha = Fact.parse_fact(query_str)
         alpha_str = str(alpha) + '.\n'
         print(alpha_str)
         substs = set(kb.query(alpha))
         substs_str = ' ;\n'.join([str(subst) for subst in substs]) + '.\n\n'        
         print(substs_str)
         f_out.write(alpha_str)
         f_out.write(substs_str)

print('Results of queries from {} are written to {}.'.format(query_file, outp_file))

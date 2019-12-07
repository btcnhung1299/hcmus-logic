from knowledge_base import KnowledgeBase
from fact import Fact

inp_file = 'test/02/profound_knowledge.pl'
query_file = 'test/02/query.pl'
outp_file = 'test/02/answers.pl'

kb = KnowledgeBase()
with open(inp_file, 'r') as f_in:
   list_sentences = f_in.readlines()
   KnowledgeBase.declare(kb, list_sentences)
print('Done initialize knowledge base from {}.'.format(inp_file))

with open(query_file, 'r') as f_query:
   with open(outp_file, 'w') as f_out:
      for query_str in f_query.readlines():
         alpha = Fact.parse_fact(query_str)
         substs = set(kb.query(alpha))

         alpha_str = str(alpha) + '.\n'
         substs_str = ' ;\n'.join([str(subst) for subst in substs]) + '.\n'        
         f_out.write(alpha_str)
         f_out.write(substs_str)

print('Results of queries from {} are written to {}.'.format(query_file, outp_file))

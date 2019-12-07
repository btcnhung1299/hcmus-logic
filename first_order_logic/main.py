from knowledge_base import KnowledgeBase

inp_file = 'test/02/profound_knowledge.pl'
query_file = 'test/02/query.pl'
outp_file = 'test/02/answers.pl'

kb = KnowledgeBase()
with open(inp_file, 'r') as f:
   list_sentences = f.readlines()
   KnowledgeBase.declare(kb, list_sentences)

with open(query_file, 'r') as f:
   for query_str in f.readlines():
      substs = set(kb.query(query_str))
      print(*substs, sep=' ;\n', end='.\n')

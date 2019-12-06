from knowledge_base import KnowledgeBase

inp_file = 'test/royal_family_tree.pl'
query_file = 'test/query.pl'
outp_file = 'test/answers.pl'

kb = KnowledgeBase()
with open(inp_file, 'r') as f:
   list_sentences = f.readlines()
   KnowledgeBase.declare(kb, list_sentences)

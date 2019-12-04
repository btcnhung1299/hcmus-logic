from knowledge_base import KnowledgeBase

kb = KnowledgeBase()
KnowledgeBase.ask(kb, '../test/01.txt')
print('Number of clauses in KB:', len(kb.clauses))

from knowledge_base import KnowledgeBase

kb = KnowledgeBase()
KnowledgeBase.declare(kb, '../test/01.txt')
print('Knowledge base contains:')
print('- Number of facts:', len(kb.facts))
print('- Number of rules:', len(kb.rules))

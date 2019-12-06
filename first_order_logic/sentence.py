class Sentence:
   def __init__(self):
      pass

   @staticmethod
   def categorize(sent_str):
      sent_str = sent_str.strip()
      if not sent_str:
         return 'blank'
      if sent_str.startswith('/*') and sent_str.endswith('*/'):
         return 'comment'
      if ':-' in sent_str:
         return 'rule'
      return 'fact' 

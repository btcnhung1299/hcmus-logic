class Sentence:

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

   @staticmethod
   def next(inp_str):
      idx = 0
      next_str = inp_str[idx].strip()
      if next_str.startswith('/*'):          # Comments
         while not next_str.endswith('*/'):
            idx += 1
            next_str += inp_str[idx].strip()
      elif next_str:                         # Queries
         while not next_str.endswith('.'):
            idx += 1
            next_str += inp_str[idx].strip()

      return next_str, inp_str[idx + 1:]

def permitido(s):
 if not s:
return False
return len(s) == len(set(s)
import re 
regex = re.compile(r'')
def permitido(s):
  if s.strip() ==  : return False
  return regex.search(s) == None
  print(permitido('banana'))
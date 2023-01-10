#11.1
import re
with open( "C:\words.txt" , encoding="utf-8") as fin:
    content = fin.read()

#print(re.split((r"[\s.()-?]+"),content))
words3=re.split((r"[\s.()-?/]+"),content)
#print(re.split((r"[\s.()-?]+"),content))
import pandas as pd
words4 = pd.Series(words3).value_counts()
words5 = dict(words4)
print(words5)
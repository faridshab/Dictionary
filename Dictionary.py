def AddArray(n: int, i: int, j: int, WordsDictionary, Dictionary):
    Row, Column = WordsDictionary.shape

    if Column <= 7:
        WordsDictionary[i].append(Dictionary[j, 2])
    elif WordsDictionary[i, n] == "":
        WordsDictionary[i, n] = Dictionary[j, 2]
    else:
        AddArray(n + 1, i, j, WordsDictionary, Dictionary)

    return 0


import pandas as pd
import numpy as np
csv1= pd.read_csv(r"d:\temp\dictionary\cefrj-vocabulary-profile-1.5.csv")
csv2= pd.read_csv(r"d:\temp\dictionary\english Dictionary.csv")
Words=np.array(csv1)
Dictionary= np.array(csv2)
WordsDictionary=np.array(csv1)


for i in range(7799):
    Word=Words[i,1]
    Words[i,1] = Word.capitalize()


for i in range(100):
    for j in range(100):
        if Words[i,1] == Dictionary[j,0]:
            AddArray(7,i,j,WordsDictionary, Dictionary)
            
            
            

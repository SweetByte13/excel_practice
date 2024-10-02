import pandas as pd;
import math;

df = pd.read_csv('OOCake.csv')

for row in range(len(df)):
    
    firstItemInRow = df.values[row][0]
    fourthItemInRow = df.values[row][3]
    
    if (str(firstItemInRow) == 'nan'):
        continue
    elif(fourthItemInRow == int(0.000)):
        continue
    elif( fourthItemInRow == 'nan'):
        continue
    else:
        if(str(fourthItemInRow) == 'nan'):
            print(str(row) + ': ' + str(firstItemInRow))
        else:
            print(str(row) + ': ' + str(firstItemInRow) + ' ' + str(fourthItemInRow))

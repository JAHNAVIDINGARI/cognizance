import pandas as pd
ser = pd.Series(['amrita', 'school', 'of', 'engineering', 'chennai' , 'campus'])
j=ser.str.capitalize()
for i in j:
    print(i,end=' ')
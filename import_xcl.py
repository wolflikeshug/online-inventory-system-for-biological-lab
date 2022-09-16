'''
How we want to import data in

import from excel

currently for Freezer template ## Will need to make if statement to see if LN2 or -80C freezer

for first 6 lines we want to take the second value on the line e.g i[1]

1 line = box_id # Want to add this box_id variable to first the box table then 
second we want to add it to every sample under box id

2 line = box type # Want to add to box table

3 line = box notes = add to box table

4 freezer_id into box table

5 shelf into box table

6 owner into box table

7 we skip this row - (header row)

8 - excel.length we take this column by column and add them to the vials table by colnum. 
Will also need to do an if statement on the second col (Sample type) so we add it to the specific type table

'''

import pandas as pd 

df = pd.read_excel('Book1.xlsx')

df 




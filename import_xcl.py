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


database fixes = type of box and also what freezer its in to be discussed

do i need to add to sample table ?

cant open up website due to there being no connections between users....

'''

from biological_samples_database.model.sample import Vial
from biological_samples_database.model.storage import Box 
from biological_samples_database.database import create_new_session, engine

import openpyxl

from sqlalchemy.orm import sessionmaker
 
dataframe = openpyxl.load_workbook("Book1.xlsx")
dataframe1 = dataframe.active

sess = sessionmaker()
sess.configure(bind=engine)



box_table = []
for row in range(0, 6):
    for col in dataframe1.iter_cols(2, 2):
        #print(col[row].value)
        box_table.append(col[row].value)

#print(box_table)

box = Box()

box.label = box_table[2]
box.freezer_id = box_table[3]
box.owner = box_table[5]
box.id = box_table[0]
box_sess = sess()
box_sess.add(box)
box_sess.commit()
        

def add_vials():
    vial_table = []
    
    
    for row in range(8, 18): #need to change to max.row. currently just doing the 10 first rows
        next = []
        Sess = sess()
        vials = Vial()
        for col in dataframe1.iter_cols(1, dataframe1.max_column):
            #print(col[row].value)
            next.append(col[row].value)
        vial_table.append(next)
        #new_tab = []
        #new_tab.append(next[0])

        vials.position = next[0]
        vials.box_id = box_table[0]
        vials.lab_id = next[3]
        vials.sample_date = next[5]
        vials.volume_ml = next[13]
        vials.user_id = next[15]
        vials.notes = next[16]

        Sess.add(vials)
        Sess.commit()
    #print(vial_table)
    return vial_table

'''
Plan for adding by sample type is to make a if statement from the vial_table where it does a
for loop through each row in the table and selects the correct column similar to above 

'''

def cell_line():
    return 0

def mosquito():
    return 0

def pbmc():
    return 0

def plasma():
    return 0

def serum():
    return 0

def virus_culture():
    return 0

def virus_isolation():
    return 0


all_data = add_vials()

for i in all_data:
    if i[1] == "cell line":
        cell_line()
    elif i[1] == "Mosquito":
        mosquito()
    elif i[1] == "PBMC":
        pbmc()
    elif i[1] == "plasma":
        plasma()
    elif i[1] == "serum":
        serum()
    elif i[1] == "virus culture":
        virus_culture()
    elif i[1] == "virus isolation":
        virus_isolation()
    
    


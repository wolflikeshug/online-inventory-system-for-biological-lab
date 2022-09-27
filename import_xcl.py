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

need to finish off extra sample types and make some changes to fit the model 

Then finally will make some more sample excel sheets we can import for testing. more excel sheets

Make button to import into. 

do i need to add to sample table ?

'''

from biological_samples_database.model.sample import Vial, VirusIsolation
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

# ADDD FREEZER OBJECT ASWELL
box = Box()

box.label = box_table[2]
box.freezer_id = box_table[3]
box.owner = box_table[5]
box.id = box_table[0]
box.box_type = box_table[1]
box_sess = sess()
box_sess.add(box)
box_sess.commit()
        
''' OLD ONE
def add_vials():
    vial_table = []
    
    
    for row in range(8, dataframe1.max_row): #need to change to max.row. currently just doing the 10 first rows
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

def virus_isolation(data_row):
    Sess = sess()
    new_entry = VirusIsolation()
    new_entry.pathwest_id = data_row[2]
    new_entry.batch_number = data_row[7]
    new_entry.passage_number = data_row[8]
    new_entry.growth_media = data_row[10]
    Sess.add(new_entry)
    Sess.commit()

def add_vials():
    
    for row in range(8, dataframe1.max_row):
        next = []
        for col in dataframe1.iter_cols(1, dataframe1.max_column):
            next.append(col[row].value)
    
        if next[1] == "cell line":
            cell_line()
        elif next[1] == "Mosquito":
            mosquito()
        elif next[1] == "PBMC":
            pbmc()
        elif next[1] == "plasma":
            plasma()
        elif next[1] == "serum":
            serum()
        elif next[1] == "virus culture":
            virus_culture()
        elif next[1] == "Virus Isolation":
            virus_isolation(next)


add_vials()


    


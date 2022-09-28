'''
database fixes = type of box and also what freezer its in to be discussed

need to finish off extra sample types and make some changes to fit the model 

Then finally will make some more sample excel sheets we can import for testing. more excel sheets

Make button to import into. 

do i need to add to sample table ?

'''

from biological_samples_database.model.sample import Antigen, CellLine, Mosquito, Other, Pbmc, Peptide, Plasma, Rna, Serum, Supernatant, Vial, VirusCulture, VirusIsolation
from biological_samples_database.model.storage import Box, BoxType, Freezer, Shelf 
from biological_samples_database.database import create_new_session, engine

import openpyxl

from sqlalchemy.orm import sessionmaker
 
dataframe = openpyxl.load_workbook("Book1.xlsx")
dataframe1 = dataframe.active

sess = sessionmaker()
sess.configure(bind=engine)

dataframe1

box_table = []
for row in range(0, 6):
    for col in dataframe1.iter_cols(2, 2):
        box_table.append(col[row].value)

def new_freezer():
    box_sess = sess()
    q = box_sess.query(Freezer).all()
    p = box_sess.query(Freezer).count()
    counter = 0
    for i in q:
        counter +=1
        if(i.name == box_table[3]): #if statement off name not ID atm
            return i.id
        elif (p <= counter):
            NewFreezer = Freezer()
            NewFreezer.name = box_table[3]
            NewFreezer.freezer_type = i.freezer_type #sets to the freezer type before
            NewFreezer.room_id = i.room_id #sets to the same room as before
            newsess = sess()
            newsess.add(NewFreezer)
            newsess.commit()
            obj = box_sess.query(Freezer).filter(Freezer.name == box_table[3])
            for j in obj:
                return j.id

def box_type():
    new_sess = sess()
    obj = new_sess.query(BoxType).all()
    for type1 in obj:
        
        if (type1.name == "9x9"):
            nineBynine = type1.id
        elif(type1.name == "10x10"):
            tenByten = type1.id
        elif(type1.name == "Wax Box (Standard)"):
            WBS = type1.id
        elif(type1.name == "Wax Box (5ml)"):
            WB5ml = type1.id
        elif(type1.name == "Wax Box (Large)"):
            WBL = type1.id
    print(nineBynine)
    print(tenByten)
    print(WBS)
    print(WB5ml)
    print(WBL)
    if(box_table[1] == "Wax Box standard"):
        return WBS
    elif(box_table[1] == "Wax Box (5ml)"): #ToDo fix these up when needed
        return WB5ml

def shelf_box(freezer_id):
    shelf_sess = sess()
    obj = shelf_sess.query(Shelf).filter(Shelf.freezer_id == freezer_id)
    count1 = shelf_sess.query(Shelf).filter(Shelf.freezer_id == freezer_id).count()
    counter = 0

    if count1 == 0:
        shelf = Shelf()
        shelf.freezer_id = freezer_id
        shelf.name = box_table[4]
        new_session = sess()
        new_session.add(shelf)
        new_session.commit()
        obj1 = shelf_sess.query(Shelf).filter(Shelf.name == box_table[4])
        for j in obj1:
            return j.id
    
    else:
        counter += 1
        for shelf1 in obj:
            print("here")
            counter +=1
            print(shelf1.name)
            if(shelf1.name == box_table[4]):
                return shelf1.id
            elif(count1 <= counter):
                print("here")
                shelf = Shelf()
                shelf.freezer_id = freezer_id
                shelf.name = box_table[4]
                new_session = sess()
                new_session.add(shelf)
                new_session.commit()
                obj1 = shelf_sess.query(Shelf).filter(Shelf.name == box_table[4])
                for j in obj1:
                    print(j.name)
                    return j.id


def box():
    box_sess = sess()
    box = Box()
    box.label = box_table[0]
    box.owner = box_table[5]
    box.box_type = box_type()
    freezer_id = new_freezer()
    box.freezer_id = freezer_id
    box.shelf_id = shelf_box(freezer_id)
    box_sess.add(box)
    box_sess.commit()

def antigen(data_row):
    Sess = sess()
    new_entry = Antigen()
    new_entry.pathwest_id = data_row[2]
    new_entry.lab_id = data_row[3]
    new_entry.batch_number = data_row[7]
    new_entry.passage_number = data_row[8]
    new_entry.lot_number = data_row[12]
    Sess.add(new_entry)
    Sess.commit()

def cell_line(data_row):
    Sess = sess()
    new_entry = CellLine()
    new_entry.lab_id = data_row[3]
    new_entry.cell_type = data_row[4]
    new_entry.passage_number = data_row[8]
    new_entry.cell_count = data_row[9]
    new_entry.growth_media = data_row[10]
    new_entry.vial_source = data_row[11]
    new_entry.lot_number = data_row[12]
    Sess.add(new_entry)
    Sess.commit()

def mosquito(data_row):
    Sess = sess()
    new_entry = Mosquito()
    new_entry.lab_id = data_row[3]
    Sess.add(new_entry)
    Sess.commit()

def pbmc(data_row):
    Sess = sess()
    new_entry = Pbmc()
    new_entry.lab_id = data_row[3]
    new_entry.visit_number = data_row[6]
    new_entry.cell_count = data_row[9]
    new_entry.patient_code = data_row[14]
    Sess.add(new_entry)
    Sess.commit()

def peptide(data_row):
    Sess = sess()
    new_entry = Peptide()
    new_entry.lab_id = data_row[3]
    new_entry.cell_type = data_row[4]
    new_entry.batch_number = data_row[7]
    new_entry.vial_source = data_row[11]
    new_entry.lot_number = data_row[12]
    Sess.add(new_entry)
    Sess.commit()

def plasma(data_row):
    Sess = sess()
    new_entry = Plasma()
    new_entry.lab_id = data_row[3]
    new_entry.visit_number = data_row[6]
    Sess.add(new_entry)
    Sess.commit()

def rna(data_row):
    Sess = sess()
    new_entry = Rna()
    new_entry.pathwest_id = data_row[2]
    new_entry.lab_id = data_row[3]
    new_entry.batch_number = data_row[7]
    new_entry.lot_number = data_row[12]
    Sess.add(new_entry)
    Sess.commit()

def serum(data_row):
    Sess = sess()
    new_entry = Serum()
    new_entry.pathwest_id = data_row[2]
    new_entry.lab_id = data_row[3]
    Sess.add(new_entry)
    Sess.commit()

def supernatant(data_row):
    Sess = sess()
    new_entry = Supernatant()
    new_entry.lab_id = data_row[3]
    Sess.add(new_entry)
    Sess.commit()

def virus_culture(data_row):
    Sess = sess()
    new_entry = VirusCulture()
    new_entry.pathwest_id = data_row[2]
    new_entry.lab_id = data_row[3]
    new_entry.batch_number = data_row[7]
    new_entry.passage_number = data_row[8]
    new_entry.growth_media = data_row[10]
    Sess.add(new_entry)
    Sess.commit()

def virus_isolation(data_row):
    Sess = sess()
    new_entry = VirusIsolation()
    new_entry.box_id = box_id
    new_entry.position = data_row[0]
    new_entry.pathwest_id = data_row[2]
    new_entry.lab_id = data_row[3]
    new_entry.sample_date = data_row[5]
    new_entry.batch_number = data_row[7]
    new_entry.passage_number = data_row[8]
    new_entry.growth_media = data_row[10]
    new_entry.volume_ml = data_row[13]
    #ToDo linkn initials and user id up 
    new_entry.notes = data_row[16]
    Sess.add(new_entry)
    Sess.commit()

def other(data_row):
    Sess = sess()
    new_entry = Other()
    new_entry.lab_id = data_row[3]
    Sess.add(new_entry)
    Sess.commit()

def add_vials():
    
    for row in range(7, dataframe1.max_row):
        next = []
        for col in dataframe1.iter_cols(1, dataframe1.max_column):
            next.append(col[row].value)
        if next[1] == "Virus Isolation":
            virus_isolation(next)
    '''
        if next[1] == "cell line":
            #cell_line(next)
            continue
        elif next[1] == "Mosquito":
            #mosquito(next)
            continue
        elif next[1] == "PBMC":
            pbmc()
        elif next[1] == "plasma":
            plasma()
        elif next[1] == "serum":
            serum()
        elif next[1] == "virus culture":
            virus_culture()
    '''


box()
box_sess = sess()
obj = box_sess.query(Box).filter(Box.label == box_table[0])
for k in obj:
    box_id = k.id

add_vials()


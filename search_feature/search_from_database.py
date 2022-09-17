from traceback import print_tb
from data_model import Serum, VirusIsolation, VirusCulture, Plasma, CellLine, Pbmc, Mosquito, Antigen, RNA, Peptide, Supernatant, Other
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

database_dir = "biological_samples.sqlite"

# create engine
engine = create_engine( "sqlite:///"+database_dir )
# base modle
Base = declarative_base(engine)

# create session
Session = sessionmaker( bind=engine )
session = Session()

# set up cases for different sample types
class query_case(object):
    def __init__(self, input_key):
        self.sample_type = input_key[0]
        self.pw_id = input_key[1]
        self.id = input_key[2]
        self.type = input_key[3]
        self.date = input_key[4]
        self.visit_number = input_key[5]
        self.batch_number = input_key[6]
        self.passage_number = input_key[7]
        self.total_count = input_key[8]
        self.media = input_key[9]
        self.source = input_key[10]
        self.lot_number = input_key[11]
        self.volume = input_key[12]
        self.patient_code = input_key[13]
        self.initials = input_key[14]
        self.other = input_key[15]

    def query_Serum (self):
        query_result = session.query( Serum ).filter( Serum.pw_id.like("%"+self.pw_id+"%") )\
                                .filter( Serum.id.like( "%"+self.id+"%") )\
                                .filter( Serum.date.like( "%"+self.date+"%" ) )\
                                .filter( Serum.initials.like( "%"+self.initials+"%" ) )\
                                .filter( Serum.other.like("%"+self.other+"%") ).all()
        
        if isinstance(self.volume, int):
            for row in query_result:
                if row.volume != self.volume:
                    query_result.remove(row)
        
        return query_result

    def query_VirusIsolation (self):
        query_result = session.query( VirusIsolation ).filter( VirusIsolation.pw_id.like("%"+self.pw_id+"%") )\
                                                    .filter( VirusIsolation.id.like("%"+self.id+"%") )\
                                                    .filter( VirusIsolation.date.like("%"+self.date+"%") )\
                                                    .filter( VirusIsolation.media.like("%"+self.media+"%") )\
                                                    .filter( VirusIsolation.initials.like("%"+self.initials+"%") )\
                                                    .filter( VirusIsolation.other.like("%"+self.other+"%") ).all()

        if isinstance(self.batch_number, int):
            for row in query_result:
                if row.batch_number != self.batch_number:
                    query_result.remove(row)
        if isinstance(self.passage_number, int):
            for row in query_result:
                if row.passage_number != self.passage_number:
                    query_result.remove(row)
        if isinstance(self.volume, int):
            for row in query_result:
                if row.volume != self.volume:
                    query_result.remove(row)
        
        return query_result

    def query_VirusCulture (self):
        query_result = session.query( VirusCulture ).filter( VirusCulture.pw_id.like("%"+self.pw_id+"%") )\
                                                    .filter( VirusCulture.id.like("%"+self.id+"%") )\
                                                    .filter( VirusCulture.date.like("%"+self.date+"%") )\
                                                    .filter( VirusCulture.media.like("%"+self.media+"%") )\
                                                    .filter( VirusCulture.initials.like("%"+self.initials+"%") )\
                                                    .filter( VirusCulture.other.like("%"+self.other+"%") ).all()
        
        if isinstance(self.batch_number, int):
            for row in query_result:
                if row.batch_number != self.batch_number:
                    query_result.remove(row)
        if isinstance(self.passage_number, int):
            for row in query_result:
                if row.passage_number != self.passage_number:
                    query_result.remove(row)
        if isinstance(self.volume, int):
            for row in query_result:
                if row.volume != self.volume:
                    query_result.remove(row)
        
        return query_result

    def query_Plasma (self):
        query_result = session.query( Plasma ).filter( Plasma.id.like("%"+self.id+"%") )\
                                            .filter( Plasma.date.like("%"+self.date+"%") )\
                                            .filter( Plasma.initials.like("%"+self.initials+"%") )\
                                            .filter( Plasma.other.like("%"+self.other+"%") ).all()

        if isinstance(self.visit_number, int):
            for row in query_result:
                if row.visit_number != self.visit_number:
                    query_result.remove(row)
        if self.volume != 0:
            for row in query_result:
                if row.volume != self.volume:
                    query_result.remove(row)
        
        return query_result

    def query_PBMC (self):
        query_result = session.query( Pbmc ).filter( Pbmc.id.like("%"+self.id+"%") )\
                                            .filter( Pbmc.date.like("%"+self.date+"%") )\
                                            .filter( Pbmc.patient_code.like("%"+self.patient_code+"%") )\
                                            .filter( Pbmc.initials.like("%"+self.initials+"%") )\
                                            .filter( Pbmc.other.like("%"+self.other+"%") ).all()

        if isinstance(self.visit_number, int):
            for row in query_result:
                if row.visit_number != self.visit_number:
                    query_result.remove(row)
        if isinstance(self.volume, int):
            for row in query_result:
                if row.volume != self.volume:
                    query_result.remove(row)
        
        return query_result

    def query_CellLine (self):
        query_result = session.query( CellLine ).filter( CellLine.id.like("%"+self.id+"%") )\
                                                .filter( CellLine.type.like("%"+self.type+"%") )\
                                                .filter( CellLine.date.like("%"+self.date+"%") )\
                                                .filter( CellLine.media.like("%"+self.media+"%") )\
                                                .filter( CellLine.source.like("%"+self.source+"%") )\
                                                .filter( CellLine.lot_number.like("%"+self.lot_number+"%") )\
                                                .filter( CellLine.initials.like("%"+self.initials+"%") )\
                                                .filter( CellLine.other.like("%"+self.other+"%") ).all()

        if isinstance(self.passage_number, int):
            for row in query_result:
                if row.passage_number != self.passage_number:
                    query_result.remove(row)
        if isinstance(self.total_count, int):
            for row in query_result:
                if row.total_count != self.total_count:
                    query_result.remove(row)
        if isinstance(self.volume, int):
            for row in query_result:
                if row.volume != self.volume:
                    query_result.remove(row)
        
        return query_result

    def query_Mosquito (self):
        query_result = session.query( Mosquito ).filter( Mosquito.id.like("%"+self.id+"%") )\
                                                .filter( Mosquito.date.like("%"+self.date+"%") )\
                                                .filter( Mosquito.initials.like("%"+self.initials+"%") )\
                                                .filter( Mosquito.other.like("%"+self.other+"%") ).all()

        if isinstance(self.volume, int):
            for row in query_result:
                if row.volume != self.volume:
                    query_result.remove(row)
        
        return query_result

    def query_Antigen (self):
        query_result = session.query( Antigen ).filter( Antigen.pw_id.like("%"+self.pw_id+"%") )\
                                                .filter( Antigen.id.like("%"+self.id+"%") )\
                                                .filter( Antigen.date.like("%"+self.date+"%") )\
                                                .filter( Antigen.initials.like("%"+self.initials+"%") )\
                                                .filter( Antigen.other.like("%"+self.other+"%") ).all()

        if isinstance(self.batch_number, int):
            for row in query_result:
                if row.batch_number != self.batch_number:
                    query_result.remove(row)
        if isinstance(self.volume, int):
            for row in query_result:
                if row.volume != self.volume:
                    query_result.remove(row)
        
        return query_result

    def query_RNA (self):
        query_result = session.query( RNA ).filter( RNA.pw_id.like("%"+self.pw_id+"%") )\
                                            .filter( RNA.id.like("%"+self.id+"%") )\
                                            .filter( RNA.date.like("%"+self.date+"%") )\
                                            .filter( RNA.lot_number.like("%"+self.lot_number+"%") )\
                                            .filter( RNA.initials.like("%"+self.initials+"%") )\
                                            .filter( RNA.other.like("%"+self.other+"%") ).all()

        if isinstance(self.batch_number, int):
            for row in query_result:
                if row.batch_number != self.batch_number:
                    query_result.remove(row)

        return query_result

    def query_Peptide (self):
        query_result = session.query( Peptide ).filter( Peptide.id.like("%"+self.id+"%") )\
                                                .filter( Peptide.date.like("%"+self.date+"%") )\
                                                .filter( Peptide.source.like("%"+self.source+"%") )\
                                                .filter( Peptide.lot_number.like("%"+self.lot_number+"%") )\
                                                .filter( Peptide.initials.like("%"+self.initials+"%") )\
                                                .filter( Peptide.other.like("%"+self.other+"%") ).all()

        if isinstance(self.batch_number, int):
            for row in query_result:
                if row.batch_number != self.batch_number:
                    query_result.remove(row)
        if isinstance(self.volume, int):
            for row in query_result:
                if row.volume != self.volume:
                    query_result.remove(row)
        
        return query_result

    def query_Supernatant (self):
        query_result = session.query( Supernatant ).filter( Supernatant.id.like("%"+self.id+"%") )\
                                                    .filter( Supernatant.date.like("%"+self.date+"%") )\
                                                    .filter( Supernatant.initials.like("%"+self.initials+"%") )\
                                                    .filter( Supernatant.other.like("%"+self.other+"%") ).all()

        if isinstance(self.volume, int):
            for row in query_result:
                if row.volume != self.volume:
                    query_result.remove(row)
        
        return query_result

    def query_Other (self):
        query_result = session.query( Other ).filter( Other.id.like("%"+self.id+"%") )\
                                            .filter( Other.date.like("%"+self.date+"%") )\
                                            .filter( Other.initials.like("%"+self.initials+"%") )\
                                            .filter( Other.other.like("%"+self.other+"%") ).all()

        if isinstance(self.volume, int):
            for row in query_result:
                if row.volume != self.volume:
                    query_result.remove(row)
        
        return query_result


# query the matched data from database
# search_key is in form of [sample_type, pw_id, id, type, date, visit_number, batch_number, passage_number, total_count, media, source, lot_number, volume, patient_code, initials, other]
# search_key should be in form of [str, str, str, str, date, int, int, int, int, str, str, str, int, str, str, str]
# keep the slot None if the element is not not been inputed anything, the function expect a list of 16 elements
def query_data_from_database( input_key ):
    for key in range(0, len(input_key)):
        if input_key[key] is None:
            input_key[key] = ""

    # query the matched data from database
    sample_type_list = ["Serum", "Virus Isolation", "Virus Culture", "Plasma", "PBMC", "Cell Line", "Mosquito", "Antigen", "RNA", "Peptide", "Supernatant", "Other"]
    guess_list = [True, True, True, True, True, True, True, True, True, True, True, True]
    case = query_case( input_key )
    result = []

    if input_key[0] in sample_type_list:
        if sample_type_list.index(input_key[0]) == 0:
            result = case.query_Serum()
        elif sample_type_list.index(input_key[0]) == 1:
            result = case.query_VirusIsolation()
        elif sample_type_list.index(input_key[0]) == 2:
            result = case.query_VirusCulture()
        elif sample_type_list.index(input_key[0]) == 3:
            result = case.query_Plasma()
        elif sample_type_list.index(input_key[0]) == 4:
            result = case.query_PBMC()
        elif sample_type_list.index(input_key[0]) == 5:
            result = case.query_CellLine()
        elif sample_type_list.index(input_key[0]) == 6:
            result = case.query_Mosquito()
        elif sample_type_list.index(input_key[0]) == 7:
            result = case.query_Antigen()
        elif sample_type_list.index(input_key[0]) == 8:
            result = case.query_RNA()
        elif sample_type_list.index(input_key[0]) == 9:
            result = case.query_Peptide()
        elif sample_type_list.index(input_key[0]) == 10:
            result = case.query_Supernatant()
        elif sample_type_list.index(input_key[0]) == 11:
            result = case.query_Other()
    
    elif input_key[0] == "":
        print("missing smaple type, start guessing")
        # if sample type is not been determined, search all the data that matches the description
        if input_key[1] != "":
            guess_list[3] = False
            guess_list[4] = False
            guess_list[5] = False
            guess_list[6] = False
            guess_list[9] = False
            guess_list[10] = False
            guess_list[11] = False
        
        if input_key[3] != "":
            guess_list[0] = False
            guess_list[1] = False
            guess_list[2] = False
            guess_list[3] = False
            guess_list[4] = False
            guess_list[6] = False
            guess_list[7] = False
            guess_list[8] = False
            guess_list[10] = False
            guess_list[11] = False

        if input_key[5] != "":
            guess_list[0] = False
            guess_list[1] = False
            guess_list[2] = False
            guess_list[5] = False
            guess_list[6] = False
            guess_list[7] = False
            guess_list[8] = False
            guess_list[9] = False
            guess_list[10] = False
            guess_list[11] = False
        
        if input_key[6] != "":
            guess_list[0] = False
            guess_list[3] = False
            guess_list[4] = False
            guess_list[5] = False
            guess_list[6] = False
            guess_list[8] = False
            guess_list[10] = False
            guess_list[11] = False

        if input_key[7] != "":
            guess_list[0] = False
            guess_list[3] = False
            guess_list[4] = False
            guess_list[6] = False
            guess_list[7] = False
            guess_list[8] = False
            guess_list[9] = False
            guess_list[10] = False
            guess_list[11] = False

        if input_key[8] != "":
            guess_list[0] = False
            guess_list[1] = False
            guess_list[2] = False
            guess_list[3] = False
            guess_list[6] = False
            guess_list[7] = False
            guess_list[8] = False
            guess_list[9] = False
            guess_list[10] = False
            guess_list[11] = False

        if input_key[9] != "":
            guess_list[0] = False
            guess_list[3] = False
            guess_list[4] = False
            guess_list[6] = False
            guess_list[7] = False
            guess_list[8] = False
            guess_list[9] = False
            guess_list[10] = False
            guess_list[11] = False
        
        if input_key[10] != "":
            guess_list[0] = False
            guess_list[1] = False
            guess_list[2] = False
            guess_list[3] = False
            guess_list[4] = False
            guess_list[6] = False
            guess_list[7] = False
            guess_list[8] = False
            guess_list[10] = False
            guess_list[11] = False

        if input_key[11] != "":
            guess_list[0] = False
            guess_list[1] = False
            guess_list[2] = False
            guess_list[3] = False
            guess_list[4] = False
            guess_list[6] = False
            guess_list[8] = False
            guess_list[10] = False
            guess_list[11] = False
        
        if input_key[13] != "":
            guess_list[0] = False
            guess_list[1] = False
            guess_list[2] = False
            guess_list[3] = False
            guess_list[5] = False
            guess_list[6] = False
            guess_list[7] = False
            guess_list[8] = False
            guess_list[9] = False
            guess_list[10] = False
            guess_list[11] = False
        
        # sample_type_list = ["Serum", "Virus Isolation", "Virus Culture", "Plasma", "PBMC", "Cell Line", "Mosquito", "Antigen", "RNA", "Peptide", "Supernatant", "Other"]
        if guess_list[0] == True:
            result.append(case.query_Serum())
        if guess_list[1] == True:
            result.append(case.query_VirusIsolation())
        if guess_list[2] == True:
            result.append(case.query_VirusCulture())
        if guess_list[3] == True:
            result.append(case.query_Plasma())
        if guess_list[4] == True:
            result.append(case.query_PBMC())
        if guess_list[5] == True:
            result.append(case.query_CellLine())
        if guess_list[6] == True:
            result.append(case.query_Mosquito())
        if guess_list[7] == True:
            result.append(case.query_Antigen())
        if guess_list[8] == True:
            result.append(case.query_RNA())
        if guess_list[9] == True:
            result.append(case.query_Peptide())
        if guess_list[10] == True:
            result.append(case.query_Supernatant())
        if guess_list[11] == True:
            result.append(case.query_Other())
        
    return result


# search_key is in form of [sample_type, pw_id, id, type, date, visit_number, batch_number, passage_number, total_count, media, source, lot_number, volume, patient_code, initials, other]
# search_key should be in form of [str, str, str, str, date, int, int, int, int, str, str, str, int, str, str, str]
key_key = [None, "Hello", None, None, None, None, None, None, None, None, None, None, None, None, None, None]
print_result = query_data_from_database(key_key)
print(len(print_result))
print(print_result)
for item2 in print_result:  
    for item in item2:
        print(item.pw_id, item.id, item.date, item.initials, item.other)

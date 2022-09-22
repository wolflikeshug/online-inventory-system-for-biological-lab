from ..model.sample import Serum, VirusIsolation, VirusCulture, Plasma,\
     CellLine, Pbmc, Mosquito, Antigen, RNA, Peptide, Supernatant, Other
from ..database import create_new_session


session = create_new_session()

# set up cases for different sample types
class query_case(object):
    def __init__(self, input_key):
        self.sample_type = input_key[0]
        self.pathwest_id = input_key[1]
        self.id = input_key[2]
        self.cell_type = input_key[3]
        self.start_date = input_key[4][0]
        self.end_date = input_key[4][1]
        self.visit_number = input_key[5]
        self.batch_number = input_key[6]
        self.passage_number = input_key[7]
        self.cell_count = input_key[8]
        self.growth_media = input_key[9]
        self.vial_source = input_key[10]
        self.lot_number = input_key[11]
        self.volume_ml = input_key[12]
        self.patient_code = input_key[13]
        self.initials = input_key[14]
        self.other = input_key[15]

    def query_Serum (self):
        query_result = session.query( Serum ).filter( Serum.pathwest_id.like("%"+self.pathwest_id+"%") )\
                                .filter( Serum.id.like( "%"+self.id+"%") )\
                                .filter( Serum.initials.like( "%"+self.initials+"%" ) )\
                                .filter( Serum.other.like("%"+self.other+"%") ).all()
        
        duplicate = query_result.copy()
        if self.start_date != "" and self.end_date != "":
            for row in duplicate:
                if row.sample_date < self.start_date or row.sample_date > self.end_date:
                    query_result.remove(row)
        if isinstance(self.volume_ml, int):
            for row in duplicate:
                if row.volume_ml != self.volume_ml:
                    query_result.remove(row)
        
        return query_result

    def query_VirusIsolation (self):
        query_result = session.query( VirusIsolation ).filter( VirusIsolation.pathwest_id.like("%"+self.pathwest_id+"%") )\
                                                    .filter( VirusIsolation.id.like("%"+self.id+"%") )\
                                                    .filter( VirusIsolation.growth_media.like("%"+self.growth_media+"%") )\
                                                    .filter( VirusIsolation.initials.like("%"+self.initials+"%") )\
                                                    .filter( VirusIsolation.other.like("%"+self.other+"%") ).all()
        
        duplicate = query_result.copy()
        if self.start_date != "" and self.end_date != "":
            for row in duplicate:
                if row.sample_date < self.start_date or row.sample_date > self.end_date:
                    query_result.remove(row)
        if isinstance(self.batch_number, int):
            for row in duplicate:
                if row.batch_number != self.batch_number:
                    query_result.remove(row)
        if isinstance(self.passage_number, int):
            for row in duplicate:
                if row.passage_number != self.passage_number:
                    query_result.remove(row)
        if isinstance(self.volume_ml, int):
            for row in duplicate:
                if row.volume_ml != self.volume_ml:
                    query_result.remove(row)
        
        return query_result

    def query_VirusCulture (self):
        query_result = session.query( VirusCulture ).filter( VirusCulture.pathwest_id.like("%"+self.pathwest_id+"%") )\
                                                    .filter( VirusCulture.id.like("%"+self.id+"%") )\
                                                    .filter( VirusCulture.growth_media.like("%"+self.growth_media+"%") )\
                                                    .filter( VirusCulture.initials.like("%"+self.initials+"%") )\
                                                    .filter( VirusCulture.other.like("%"+self.other+"%") ).all()
        
        duplicate = query_result.copy()
        if self.start_date != "" and self.end_date != "":
            for row in duplicate:
                if row.sample_date < self.start_date or row.sample_date > self.end_date:
                    query_result.remove(row)
        if isinstance(self.batch_number, int):
            for row in duplicate:
                if row.batch_number != self.batch_number:
                    query_result.remove(row)
        if isinstance(self.passage_number, int):
            for row in duplicate:
                if row.passage_number != self.passage_number:
                    query_result.remove(row)
        if isinstance(self.volume_ml, int):
            for row in duplicate:
                if row.volume_ml != self.volume_ml:
                    query_result.remove(row)
        
        return query_result

    def query_Plasma (self):
        query_result = session.query( Plasma ).filter( Plasma.id.like("%"+self.id+"%") )\
                                            .filter( Plasma.initials.like("%"+self.initials+"%") )\
                                            .filter( Plasma.other.like("%"+self.other+"%") ).all()

        duplicate = query_result.copy()
        if self.start_date != "" and self.end_date != "":
            for row in duplicate:
                if row.sample_date < self.start_date or row.sample_date > self.end_date:
                    query_result.remove(row)
        if isinstance(self.visit_number, int):
            for row in duplicate:
                if row.visit_number != self.visit_number:
                    query_result.remove(row)
        if isinstance(self.volume_ml, int):
            for row in duplicate:
                if row.volume_ml != self.volume_ml:
                    query_result.remove(row)
        
        return query_result

    def query_PBMC (self):
        query_result = session.query( Pbmc ).filter( Pbmc.id.like("%"+self.id+"%") )\
                                            .filter( Pbmc.patient_code.like("%"+self.patient_code+"%") )\
                                            .filter( Pbmc.initials.like("%"+self.initials+"%") )\
                                            .filter( Pbmc.other.like("%"+self.other+"%") ).all()

        duplicate = query_result.copy()
        if self.start_date != "" and self.end_date != "":
            for row in duplicate:
                if row.sample_date < self.start_date or row.sample_date > self.end_date:
                    query_result.remove(row)
        if isinstance(self.visit_number, int):
            for row in duplicate:
                if row.visit_number != self.visit_number:
                    query_result.remove(row)
        if isinstance(self.volume_ml, int):
            for row in duplicate:
                if row.volume_ml != self.volume_ml:
                    query_result.remove(row)
        
        return query_result

    def query_CellLine (self):
        query_result = session.query( CellLine ).filter( CellLine.id.like("%"+self.id+"%") )\
                                                .filter( CellLine.cell_type.like("%"+self.cell_type+"%") )\
                                                .filter( CellLine.growth_media.like("%"+self.growth_media+"%") )\
                                                .filter( CellLine.vial_source.like("%"+self.vial_source+"%") )\
                                                .filter( CellLine.lot_number.like("%"+self.lot_number+"%") )\
                                                .filter( CellLine.initials.like("%"+self.initials+"%") )\
                                                .filter( CellLine.other.like("%"+self.other+"%") ).all()
     
        duplicate = query_result.copy()
        if self.start_date != "" and self.end_date != "":
            for row in duplicate:
                if row.sample_date < self.start_date or row.sample_date > self.end_date:
                    query_result.remove(row)
        if isinstance(self.visit_number, int):
            for row in duplicate:
                if row.visit_number != self.visit_number:
                    query_result.remove(row)
        if isinstance(self.cell_count, int):
            for row in duplicate:
                if row.cell_count != self.cell_count:
                    query_result.remove(row)
        if isinstance(self.volume_ml, int):
            for row in duplicate:
                if row.volume_ml != self.volume_ml:
                    query_result.remove(row)

        return query_result

    def query_Mosquito (self):
        query_result = session.query( Mosquito ).filter( Mosquito.id.like("%"+self.id+"%") )\
                                                .filter( Mosquito.initials.like("%"+self.initials+"%") )\
                                                .filter( Mosquito.other.like("%"+self.other+"%") ).all()

        duplicate = query_result.copy()
        if self.start_date != "" and self.end_date != "":
            for row in duplicate:
                if row.sample_date < self.start_date or row.sample_date > self.end_date:
                    query_result.remove(row)
        if isinstance(self.volume_ml, int):
            for row in duplicate:
                if row.volume_ml != self.volume_ml:
                    query_result.remove(row)

        return query_result

    def query_Antigen (self):
        query_result = session.query( Antigen ).filter( Antigen.pathwest_id.like("%"+self.pathwest_id+"%") )\
                                                .filter( Antigen.id.like("%"+self.id+"%") )\
                                                .filter( Antigen.initials.like("%"+self.initials+"%") )\
                                                .filter( Antigen.other.like("%"+self.other+"%") ).all()

        duplicate = query_result.copy()
        if self.start_date != "" and self.end_date != "":
            for row in duplicate:
                if row.sample_date < self.start_date or row.sample_date > self.end_date:
                    query_result.remove(row)
        if isinstance(self.batch_number, int):
            for row in duplicate:
                if row.batch_number != self.batch_number:
                    query_result.remove(row)
        if isinstance(self.volume_ml, int):
            for row in duplicate:
                if row.volume_ml != self.volume_ml:
                    query_result.remove(row)

        return query_result

    def query_RNA (self):
        query_result = session.query( RNA ).filter( RNA.pathwest_id.like("%"+self.pathwest_id+"%") )\
                                            .filter( RNA.id.like("%"+self.id+"%") )\
                                            .filter( RNA.lot_number.like("%"+self.lot_number+"%") )\
                                            .filter( RNA.initials.like("%"+self.initials+"%") )\
                                            .filter( RNA.other.like("%"+self.other+"%") ).all()

        duplicate = query_result.copy()
        if self.start_date != "" and self.end_date != "":
            for row in duplicate:
                if row.sample_date < self.start_date or row.sample_date > self.end_date:
                    query_result.remove(row)
        if isinstance(self.volume_ml, int):
            for row in duplicate:
                if row.volume_ml != self.volume_ml:
                    query_result.remove(row)

        return query_result

    def query_Peptide (self):
        query_result = session.query( Peptide ).filter( Peptide.id.like("%"+self.id+"%") )\
                                                .filter( Peptide.vial_source.like("%"+self.vial_source+"%") )\
                                                .filter( Peptide.lot_number.like("%"+self.lot_number+"%") )\
                                                .filter( Peptide.initials.like("%"+self.initials+"%") )\
                                                .filter( Peptide.other.like("%"+self.other+"%") ).all()

        duplicate = query_result.copy()
        if self.start_date != "" and self.end_date != "":
            for row in duplicate:
                if row.sample_date < self.start_date or row.sample_date > self.end_date:
                    query_result.remove(row)
        if isinstance(self.batch_number, int):
            for row in duplicate:
                if row.batch_number != self.batch_number:
                    query_result.remove(row)
        if isinstance(self.volume_ml, int):
            for row in duplicate:
                if row.volume_ml != self.volume_ml:
                    query_result.remove(row)

        return query_result

    def query_Supernatant (self):
        query_result = session.query( Supernatant ).filter( Supernatant.id.like("%"+self.id+"%") )\
                                                    .filter( Supernatant.initials.like("%"+self.initials+"%") )\
                                                    .filter( Supernatant.other.like("%"+self.other+"%") ).all()

        duplicate = query_result.copy()
        if self.start_date != "" and self.end_date != "":
            for row in duplicate:
                if row.sample_date < self.start_date or row.sample_date > self.end_date:
                    query_result.remove(row)
        if isinstance(self.volume_ml, int):
            for row in duplicate:
                if row.volume_ml != self.volume_ml:
                    query_result.remove(row)

        return query_result

    def query_Other (self):
        query_result = session.query( Other ).filter( Other.id.like("%"+self.id+"%") )\
                                            .filter( Other.initials.like("%"+self.initials+"%") )\
                                            .filter( Other.other.like("%"+self.other+"%") ).all()

        duplicate = query_result.copy()
        if self.start_date != "" and self.end_date != "":
            for row in duplicate:
                if row.sample_date < self.start_date or row.sample_date > self.end_date:
                    query_result.remove(row)
        if isinstance(self.volume_ml, int):
            for row in duplicate:
                if row.volume_ml != self.volume_ml:
                    query_result.remove(row)
        
        return query_result

# query the matched data from database
# search_key is in form of [sample_type, pathwest_id, id, cell_type, date, visit_number, batch_number, passage_number, cell_count, growth_media, source, lot_number, volume, patient_code, initials, other]
# search_key should be in form of [[str(list the selected sample_type want to search)]], str, str, str, [start_date, end_date], int, int, int, int, str, str, str, float, str, str, str]
# note: if user going to provide date value, must provide start_date and end_date at the same time, otherwise, it will be ignored, 
# if user going to provide the excate date, then start_date and end_date should be the same date like [2020-01-01, 2020-01-01]
# filled the slot with None if the element is not not been inputed anything, the function expect a list of 16 elements
# if user did not select the sample_type, keep the first element as a empty list like []
def query_data_from_database( input_key ):
    for key in range(1, len(input_key)):
        if input_key[key] is None:
            input_key[key] = ""
        if key == 4:
            for day in range(0, len(input_key[key])):
                if input_key[key][day] is None:
                    input_key[key][day] = ""

    # query the matched data from database
    sample_type_list = ["Serum", "Virus Isolation", "Virus Culture", "Plasma", "PBMC", "Cell Line", "Mosquito", "Antigen", "RNA", "Peptide", "Supernatant", "Other"]
    request_list = [False, False, False, False, False, False, False, False, False, False, False, False]
    guess_list = [True, True, True, True, True, True, True, True, True, True, True, True]
    req_guess = True               # if the user selected the sample type, then req_guess be True, otherwise it will be false
    case = query_case( input_key )
    result = [[]]
    quest_list = [case.query_Serum(), case.query_VirusIsolation(), case.query_VirusCulture(), case.query_Plasma(), case.query_PBMC(), case.query_CellLine(), case.query_Mosquito(), case.query_Antigen(), case.query_RNA(), case.query_Peptide(), case.query_Supernatant(), case.query_Other()]


    if input_key[0] != []:
        req_guess = True
        for sample_type in input_key[0]:
            if sample_type in sample_type_list:
                request_list[sample_type_list.index(sample_type)] = True
 
    else:
        req_guess = False
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


    if req_guess:
        for req in range(0, len(request_list)):
            if request_list[req]:
                result.append(quest_list[req])
                result[0].append(sample_type_list[req])
            
    else:    
        for req in range(0, len(guess_list)):
            if guess_list[req]:
                result.append(quest_list[req])
                result[0].append(sample_type_list[req])

    # the resturn will in form of [[sample types that matches the description], [queried data], [queried data], ...]
    return result

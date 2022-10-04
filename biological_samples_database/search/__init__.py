"""

Search

All API information related to search samples

"""
# Standard
from datetime import datetime

# Flask
from flask import Blueprint, redirect, render_template, request

# Flask WTF
from wtforms import IntegerField, StringField
from flask_wtf import FlaskForm
from wtforms import (
    BooleanField,
    DateField,
    FloatField,
    IntegerField,
    StringField
)

from ..model.search import Search_Result

from .search_from_database import query_data_from_database

SEARCH = Blueprint(
    'search_output',
    __name__,
    template_folder='templates'
)

from ..forms import SearchForm

search_input = [[], None, None, None, [None, None], None, None, None, None, None, None, None, None, None, None, None]

@SEARCH.route('/', methods=['GET'])
def read_all():
    '''
    form = SearchForm()

    if request.form.get('Serum_sele'):
        search_input[0].append('Serum')
    if request.form.get('Virus_Isolation_sele'):
        search_input[0].append('Virus Isolation')
    if request.form.get('Virus_Culture_sele'):
        search_input[0].append('Virus Culture')
    if request.form.get('Plasma_sele'):
        search_input[0].append('Plasma')
    if request.form.get('PBMC_sele'):
        search_input[0].append('PBMC')
    if request.form.get('Cell_Line_sele'):
        search_input[0].append('Cell Line')
    if request.form.get('Mosquito_sele'):
        search_input[0].append('Mosquito')
    if request.form.get('Antigen_sele'):
        search_input[0].append('Antigen')
    if request.form.get('Rna_sele'):
        search_input[0].append('Rna')
    if request.form.get('Peptide_sele'):
        search_input[0].append('Peptide')
    if request.form.get('Supernatant_sele'):
        search_input[0].append('Supernatant')
    if request.form.get('Other_sele'):
        search_input[0].append('Other')
    
    search_input[1] = request.form.get('pw_id')
    search_input[2] = request.form.get('id')
    search_input[3] = request.form.get('cell_type')
    if request.form.get('need_date'):
        search_input[4][0] = request.form.get('start_date')
        search_input[4][1] = request.form.get('end_date')
    search_input[5] = request.form.get('visit_number')
    search_input[6] = request.form.get('batch_number')
    search_input[7] = request.form.get('passage_number')
    search_input[8] = request.form.get('cell_count')
    search_input[9] = request.form.get('growth_media')
    search_input[10] = request.form.get('vial_source')
    search_input[11] = request.form.get('lot_number')
    search_input[12] = request.form.get('volume_ml')
    search_input[13] = request.form.get('patient_code')
    search_input[14] = request.form.get('user_id')
    search_input[15] = request.form.get('notes')
    
    search_raw_output = query_data_from_database(search_input)
    search_output = []
    for i in range(1, len(search_raw_output)):
        for n in range(0, len(search_raw_output[i])):
            if search_raw_output[0][i-1] == "Serum":
                search_output.append(Search_Result(sample_type = search_raw_output[0][i-1], 
                                                    lab_id = search_raw_output[i][n].lab_id,
                                                    box_id = search_raw_output[i][n].box_id,
                                                    position = search_raw_output[i][n].position,
                                                    pathwest_id = search_raw_output[i][n].pathwest_id, 
                                                    id = search_raw_output[i][n].id, 
                                                    sample_date = str(search_raw_output[i][n].sample_date), 
                                                    volume_ml = str(search_raw_output[i][n].volume_ml), 
                                                    user_id = search_raw_output[i][n].user_id, 
                                                    notes = search_raw_output[i][n].notes))
            elif search_raw_output[0][i-1] == "Virus Isolation":
                search_output.append(Search_Result(sample_type = search_raw_output[0][i-1], 
                                                    lab_id = search_raw_output[i][n].lab_id,
                                                    box_id = search_raw_output[i][n].box_id,
                                                    position = search_raw_output[i][n].position,
                                                    pathwest_id = search_raw_output[i][n].pathwest_id, 
                                                    id = search_raw_output[i][n].id,
                                                    sample_date = str(search_raw_output[i][n].sample_date), 
                                                    batch_number = str(search_raw_output[i][n].batch_number), 
                                                    passage_number = str(search_raw_output[i][n].passage_number), 
                                                    growth_media = search_raw_output[i][n].growth_media, 
                                                    volume_ml = str(search_raw_output[i][n].volume_ml), 
                                                    user_id = search_raw_output[i][n].user_id, 
                                                    notes = search_raw_output[i][n].notes))
            elif search_raw_output[0][i-1] == "Virus Culture":
                search_output.append(Search_Result(sample_type = search_raw_output[0][i-1], 
                                                    lab_id = search_raw_output[i][n].lab_id,
                                                    box_id = search_raw_output[i][n].box_id,
                                                    position = search_raw_output[i][n].position,
                                                    pathwest_id = search_raw_output[i][n].pathwest_id, 
                                                    id = search_raw_output[i][n].id, 
                                                    sample_date = str(search_raw_output[i][n].sample_date), 
                                                    batch_number = str(search_raw_output[i][n].batch_number), 
                                                    passage_number = str(search_raw_output[i][n].passage_number), 
                                                    growth_media = search_raw_output[i][n].growth_media, 
                                                    volume_ml = str(search_raw_output[i][n].volume_ml), 
                                                    user_id = search_raw_output[i][n].user_id, 
                                                    notes = search_raw_output[i][n].notes))
            elif search_raw_output[0][i-1] == "Plasma":
                search_output.append(Search_Result(sample_type = search_raw_output[0][i-1], 
                                                    lab_id = search_raw_output[i][n].lab_id,
                                                    box_id = search_raw_output[i][n].box_id,
                                                    position = search_raw_output[i][n].position,
                                                    id = search_raw_output[i][n].id, 
                                                    sample_date = str(search_raw_output[i][n].sample_date), 
                                                    visit_number = str(search_raw_output[i][n].visit_number), 
                                                    volume_ml = str(search_raw_output[i][n].volume_ml), 
                                                    user_id = search_raw_output[i][n].user_id, 
                                                    notes = search_raw_output[i][n].notes))
            elif search_raw_output[0][i-1] == "PBMC":
                search_output.append(Search_Result(sample_type = search_raw_output[0][i-1], 
                                                    lab_id = search_raw_output[i][n].lab_id,
                                                    box_id = search_raw_output[i][n].box_id,
                                                    position = search_raw_output[i][n].position,
                                                    id = search_raw_output[i][n].id, 
                                                    sample_date = str(search_raw_output[i][n].sample_date), 
                                                    visit_number = str(search_raw_output[i][n].visit_number), 
                                                    volume_ml = str(search_raw_output[i][n].volume_ml), 
                                                    patient_code = search_raw_output[i][n].patient_code, 
                                                    user_id = search_raw_output[i][n].user_id, 
                                                    notes = search_raw_output[i][n].notes))
            elif search_raw_output[0][i-1] == "Cell Line":
                search_output.append(Search_Result(sample_type = search_raw_output[0][i-1], 
                                                    lab_id = search_raw_output[i][n].lab_id,
                                                    box_id = search_raw_output[i][n].box_id,
                                                    position = search_raw_output[i][n].position,
                                                    id = search_raw_output[i][n].id, 
                                                    cell_type = search_raw_output[i][n].cell_type, 
                                                    sample_date = str(search_raw_output[i][n].sample_date), 
                                                    passage_number = str(search_raw_output[i][n].passage_number), 
                                                    cell_count = str(search_raw_output[i][n].cell_count), 
                                                    growth_media = search_raw_output[i][n].growth_media, 
                                                    lot_number = search_raw_output[i][n].lot_number, 
                                                    volume_ml = str(search_raw_output[i][n].volume_ml), 
                                                    user_id = search_raw_output[i][n].user_id, 
                                                    notes = search_raw_output[i][n].notes))
            elif search_raw_output[0][i-1] == "Mosquito":
                search_output.append(Search_Result(sample_type = search_raw_output[0][i-1], 
                                                    lab_id = search_raw_output[i][n].lab_id,
                                                    box_id = search_raw_output[i][n].box_id,
                                                    position = search_raw_output[i][n].position,
                                                    id = search_raw_output[i][n].id, 
                                                    sample_date = str(search_raw_output[i][n].sample_date), 
                                                    volume_ml = str(search_raw_output[i][n].volume_ml), 
                                                    user_id = search_raw_output[i][n].user_id, 
                                                    notes = search_raw_output[i][n].notes))
            elif search_raw_output[0][i-1] == "Antigen":
                search_output.append(Search_Result(sample_type = search_raw_output[0][i-1], 
                                                    lab_id = search_raw_output[i][n].lab_id,
                                                    box_id = search_raw_output[i][n].box_id,
                                                    position = search_raw_output[i][n].position,
                                                    pathwest_id = search_raw_output[i][n].pathwest_id, 
                                                    id = search_raw_output[i][n].id, 
                                                    sample_date = str(search_raw_output[i][n].sample_date), 
                                                    batch_number = str(search_raw_output[i][n].batch_number), 
                                                    lot_number = search_raw_output[i][n].lot_number, 
                                                    volume_ml = str(search_raw_output[i][n].volume_ml), 
                                                    user_id = search_raw_output[i][n].user_id, 
                                                    notes = search_raw_output[i][n].notes))
            elif search_raw_output[0][i-1] == "Rna":
                search_output.append(Search_Result(sample_type = search_raw_output[0][i-1],
                                                    lab_id = search_raw_output[i][n].lab_id,
                                                    box_id = search_raw_output[i][n].box_id,
                                                    position = search_raw_output[i][n].position, 
                                                    pathwest_id = search_raw_output[i][n].pathwest_id, 
                                                    id = search_raw_output[i][n].id, 
                                                    sample_date = str(search_raw_output[i][n].sample_date), 
                                                    batch_number = str(search_raw_output[i][n].batch_number), 
                                                    lot_number = search_raw_output[i][n].lot_number, 
                                                    volume_ml = str(search_raw_output[i][n].volume_ml), 
                                                    user_id = search_raw_output[i][n].user_id, 
                                                    notes = search_raw_output[i][n].notes))
            elif search_raw_output[0][i-1] == "Peptide":
                search_output.append(Search_Result(sample_type = search_raw_output[0][i-1], 
                                                    lab_id = search_raw_output[i][n].lab_id,
                                                    box_id = search_raw_output[i][n].box_id,
                                                    position = search_raw_output[i][n].position,
                                                    id = search_raw_output[i][n].id, 
                                                    cell_type = search_raw_output[i][n].cell_type, 
                                                    sample_date = str(search_raw_output[i][n].sample_date), 
                                                    batch_number = str(search_raw_output[i][n].batch_number), 
                                                    vial_source = search_raw_output[i][n].vial_source, 
                                                    lot_number = search_raw_output[i][n].lot_number, 
                                                    volume_ml = str(search_raw_output[i][n].volume_ml), 
                                                    user_id = search_raw_output[i][n].user_id, 
                                                    notes = search_raw_output[i][n].notes))
            elif search_raw_output[0][i-1] == "Supernatant":
                search_output.append(Search_Result(sample_type = search_raw_output[0][i-1], 
                                                    lab_id = search_raw_output[i][n].lab_id,
                                                    box_id = search_raw_output[i][n].box_id,
                                                    position = search_raw_output[i][n].position,
                                                    id = search_raw_output[i][n].id, 
                                                    sample_date = str(search_raw_output[i][n].sample_date), 
                                                    volume_ml = str(search_raw_output[i][n].volume_ml), 
                                                    user_id = search_raw_output[i][n].user_id, 
                                                    notes = search_raw_output[i][n].notes))
            elif search_raw_output[0][i-1] == "Other":
                search_output.append(Search_Result(sample_type = search_raw_output[0][i-1],
                                                    lab_id = search_raw_output[i][n].lab_id,
                                                    box_id = search_raw_output[i][n].box_id,
                                                    position = search_raw_output[i][n].position, 
                                                    id = search_raw_output[i][n].id, 
                                                    sample_date = str(search_raw_output[i][n].sample_date), 
                                                    volume_ml = str(search_raw_output[i][n].volume_ml), 
                                                    user_id = search_raw_output[i][n].user_id, 
                                                    notes = search_raw_output[i][n].notes))
    
    print(search_raw_output)
    print(search_output)
    print()
    
    for i in range(len(search_output)):
        if (len(search_output[i].box_id) > 20):
            search_output[i].box_id = "-"
        if (len(search_output[i].id) > 20):
            search_output[i].id = "-"
        if (search_output[i].sample_date == "1900-01-01"):
            search_output[i].sample_date = "-"
        if (search_output[i].passage_number == "-9999"):
            search_output[i].passage_number = "-" 
        if (search_output[i].passage_number == None):
            search_output[i].passage_number = "[N/A]"
        if (search_output[i].volume_ml == "-9999"):
            search_output[i].volume_ml = "-"
        if (search_output[i].volume_ml == "0.0"):
            search_output[i].volume_ml = "-"
        if (search_output[i].growth_media == "UNKNOWN"):
            search_output[i].growth_media = "-"
        if (search_output[i].growth_media == None):
            search_output[i].growth_media = "[N/A]"
        if (search_output[i].batch_number == "-9999"):
            search_output[i].batch_number = "-"
        if (search_output[i].batch_number == None):
            search_output[i].batch_number = "[N/A]"
        if (search_output[i].lot_number == "-UNKNOWN"):
            search_output[i].lot_number = "-"
        if (search_output[i].lot_number == None):
            search_output[i].lot_number = "[N/A]"
        if (search_output[i].cell_count == "-9999"):
            search_output[i].cell_count = "-"
        if (search_output[i].cell_count == None):
            search_output[i].cell_count = "[N/A]"
        if (search_output[i].visit_number == "-9999"):
            search_output[i].visit_number = "-"
        if (search_output[i].visit_number == None):
            search_output[i].visit_number = "[N/A]"
        if (search_output[i].pathwest_id == "UNKNOWN"):
            search_output[i].pathwest_id = "-"
        if (search_output[i].pathwest_id == None):
            search_output[i].pathwest_id = "[N/A]"
        if (search_output[i].patient_code == "UNKNOWN"):
            search_output[i].patient_code = "-"
        if (search_output[i].patient_code == None):
            search_output[i].patient_code = "[N/A]"
        if (search_output[i].notes == "UNKNOWN"):
            search_output[i].notes = "-"
        if (search_output[i].notes == None):
            search_output[i].notes = "[N/A]"
        if (search_output[i].vial_source == "UNKNOWN"):
            search_output[i].vial_source = "-"
        if (search_output[i].vial_source == None):
            search_output[i].vial_source = "[N/A]"
        if (search_output[i].user_id == "UNKNOWN"):
            search_output[i].user_id = "-"
        if (search_output[i].user_id == None):
            search_output[i].user_id = "[N/A]"

    return render_template(
        'search_base.html',
        sample_type='search_result',
        target_sample_header_html_file='search_header_stub.html',
        target_sample_data_html_file='search_data_stub.html',
        samples=search_output,
        form=form,
        title="Samples"
    )
'''
@SEARCH.route('/form/', methods=['GET', 'POST'])
def create_cell_line_form():
    form = SearchForm()

    if form.validate_on_submit():
        print("valid")
        print(form.data)
        search_input[0] = form.sample_type.data
        search_input[1] = form.pw_id.data
        search_input[2] = form.id.data
        search_input[3] = form.cell_type.data
        if form.need_date.data:
            print("daterange specified")
            search_input[4][0] = form.start_date.data
            search_input[4][1] = form.end_date.data
        search_input[5] = form.visit_number.data
        search_input[6] = form.batch_number.data
        search_input[7] = form.passage_number.data
        search_input[8] = form.cell_count.data
        search_input[9] = form.growth_media.data
        search_input[10] = form.vial_source.data
        search_input[11] = form.lot_number.data
        search_input[12] = form.volume_ml.data
        search_input[13] = form.patient_code.data
        search_input[14] = form.user_id.data
        search_input[15] = form.notes.data

        print(search_input)
        
        search_raw_output = query_data_from_database(search_input)
        search_output = []
        for i in range(1, len(search_raw_output)):
            for n in range(0, len(search_raw_output[i])):
                if search_raw_output[0][i-1] == "Serum":
                    search_output.append(Search_Result(sample_type = search_raw_output[0][i-1], 
                                                        lab_id = search_raw_output[i][n].lab_id,
                                                        box_id = search_raw_output[i][n].box_id,
                                                        position = search_raw_output[i][n].position,
                                                        pathwest_id = search_raw_output[i][n].pathwest_id, 
                                                        id = search_raw_output[i][n].id, 
                                                        sample_date = str(search_raw_output[i][n].sample_date), 
                                                        volume_ml = str(search_raw_output[i][n].volume_ml), 
                                                        user_id = search_raw_output[i][n].user_id, 
                                                        notes = search_raw_output[i][n].notes))
                elif search_raw_output[0][i-1] == "Virus Isolation":
                    search_output.append(Search_Result(sample_type = search_raw_output[0][i-1], 
                                                        lab_id = search_raw_output[i][n].lab_id,
                                                        box_id = search_raw_output[i][n].box_id,
                                                        position = search_raw_output[i][n].position,
                                                        pathwest_id = search_raw_output[i][n].pathwest_id, 
                                                        id = search_raw_output[i][n].id,
                                                        sample_date = str(search_raw_output[i][n].sample_date), 
                                                        batch_number = str(search_raw_output[i][n].batch_number), 
                                                        passage_number = str(search_raw_output[i][n].passage_number), 
                                                        growth_media = search_raw_output[i][n].growth_media, 
                                                        volume_ml = str(search_raw_output[i][n].volume_ml), 
                                                        user_id = search_raw_output[i][n].user_id, 
                                                        notes = search_raw_output[i][n].notes))
                elif search_raw_output[0][i-1] == "Virus Culture":
                    search_output.append(Search_Result(sample_type = search_raw_output[0][i-1], 
                                                        lab_id = search_raw_output[i][n].lab_id,
                                                        box_id = search_raw_output[i][n].box_id,
                                                        position = search_raw_output[i][n].position,
                                                        pathwest_id = search_raw_output[i][n].pathwest_id, 
                                                        id = search_raw_output[i][n].id, 
                                                        sample_date = str(search_raw_output[i][n].sample_date), 
                                                        batch_number = str(search_raw_output[i][n].batch_number), 
                                                        passage_number = str(search_raw_output[i][n].passage_number), 
                                                        growth_media = search_raw_output[i][n].growth_media, 
                                                        volume_ml = str(search_raw_output[i][n].volume_ml), 
                                                        user_id = search_raw_output[i][n].user_id, 
                                                        notes = search_raw_output[i][n].notes))
                elif search_raw_output[0][i-1] == "Plasma":
                    search_output.append(Search_Result(sample_type = search_raw_output[0][i-1], 
                                                        lab_id = search_raw_output[i][n].lab_id,
                                                        box_id = search_raw_output[i][n].box_id,
                                                        position = search_raw_output[i][n].position,
                                                        id = search_raw_output[i][n].id, 
                                                        sample_date = str(search_raw_output[i][n].sample_date), 
                                                        visit_number = str(search_raw_output[i][n].visit_number), 
                                                        volume_ml = str(search_raw_output[i][n].volume_ml), 
                                                        user_id = search_raw_output[i][n].user_id, 
                                                        notes = search_raw_output[i][n].notes))
                elif search_raw_output[0][i-1] == "PBMC":
                    search_output.append(Search_Result(sample_type = search_raw_output[0][i-1], 
                                                        lab_id = search_raw_output[i][n].lab_id,
                                                        box_id = search_raw_output[i][n].box_id,
                                                        position = search_raw_output[i][n].position,
                                                        id = search_raw_output[i][n].id, 
                                                        sample_date = str(search_raw_output[i][n].sample_date), 
                                                        visit_number = str(search_raw_output[i][n].visit_number), 
                                                        volume_ml = str(search_raw_output[i][n].volume_ml), 
                                                        patient_code = search_raw_output[i][n].patient_code, 
                                                        user_id = search_raw_output[i][n].user_id, 
                                                        notes = search_raw_output[i][n].notes))
                elif search_raw_output[0][i-1] == "Cell Line":
                    search_output.append(Search_Result(sample_type = search_raw_output[0][i-1], 
                                                        lab_id = search_raw_output[i][n].lab_id,
                                                        box_id = search_raw_output[i][n].box_id,
                                                        position = search_raw_output[i][n].position,
                                                        id = search_raw_output[i][n].id, 
                                                        cell_type = search_raw_output[i][n].cell_type, 
                                                        sample_date = str(search_raw_output[i][n].sample_date), 
                                                        passage_number = str(search_raw_output[i][n].passage_number), 
                                                        cell_count = str(search_raw_output[i][n].cell_count), 
                                                        growth_media = search_raw_output[i][n].growth_media, 
                                                        lot_number = search_raw_output[i][n].lot_number, 
                                                        volume_ml = str(search_raw_output[i][n].volume_ml), 
                                                        user_id = search_raw_output[i][n].user_id, 
                                                        notes = search_raw_output[i][n].notes))
                elif search_raw_output[0][i-1] == "Mosquito":
                    search_output.append(Search_Result(sample_type = search_raw_output[0][i-1], 
                                                        lab_id = search_raw_output[i][n].lab_id,
                                                        box_id = search_raw_output[i][n].box_id,
                                                        position = search_raw_output[i][n].position,
                                                        id = search_raw_output[i][n].id, 
                                                        sample_date = str(search_raw_output[i][n].sample_date), 
                                                        volume_ml = str(search_raw_output[i][n].volume_ml), 
                                                        user_id = search_raw_output[i][n].user_id, 
                                                        notes = search_raw_output[i][n].notes))
                elif search_raw_output[0][i-1] == "Antigen":
                    search_output.append(Search_Result(sample_type = search_raw_output[0][i-1], 
                                                        lab_id = search_raw_output[i][n].lab_id,
                                                        box_id = search_raw_output[i][n].box_id,
                                                        position = search_raw_output[i][n].position,
                                                        pathwest_id = search_raw_output[i][n].pathwest_id, 
                                                        id = search_raw_output[i][n].id, 
                                                        sample_date = str(search_raw_output[i][n].sample_date), 
                                                        batch_number = str(search_raw_output[i][n].batch_number), 
                                                        lot_number = search_raw_output[i][n].lot_number, 
                                                        volume_ml = str(search_raw_output[i][n].volume_ml), 
                                                        user_id = search_raw_output[i][n].user_id, 
                                                        notes = search_raw_output[i][n].notes))
                elif search_raw_output[0][i-1] == "Rna":
                    search_output.append(Search_Result(sample_type = search_raw_output[0][i-1],
                                                        lab_id = search_raw_output[i][n].lab_id,
                                                        box_id = search_raw_output[i][n].box_id,
                                                        position = search_raw_output[i][n].position, 
                                                        pathwest_id = search_raw_output[i][n].pathwest_id, 
                                                        id = search_raw_output[i][n].id, 
                                                        sample_date = str(search_raw_output[i][n].sample_date), 
                                                        batch_number = str(search_raw_output[i][n].batch_number), 
                                                        lot_number = search_raw_output[i][n].lot_number, 
                                                        volume_ml = str(search_raw_output[i][n].volume_ml), 
                                                        user_id = search_raw_output[i][n].user_id, 
                                                        notes = search_raw_output[i][n].notes))
                elif search_raw_output[0][i-1] == "Peptide":
                    search_output.append(Search_Result(sample_type = search_raw_output[0][i-1], 
                                                        lab_id = search_raw_output[i][n].lab_id,
                                                        box_id = search_raw_output[i][n].box_id,
                                                        position = search_raw_output[i][n].position,
                                                        id = search_raw_output[i][n].id, 
                                                        cell_type = search_raw_output[i][n].cell_type, 
                                                        sample_date = str(search_raw_output[i][n].sample_date), 
                                                        batch_number = str(search_raw_output[i][n].batch_number), 
                                                        vial_source = search_raw_output[i][n].vial_source, 
                                                        lot_number = search_raw_output[i][n].lot_number, 
                                                        volume_ml = str(search_raw_output[i][n].volume_ml), 
                                                        user_id = search_raw_output[i][n].user_id, 
                                                        notes = search_raw_output[i][n].notes))
                elif search_raw_output[0][i-1] == "Supernatant":
                    search_output.append(Search_Result(sample_type = search_raw_output[0][i-1], 
                                                        lab_id = search_raw_output[i][n].lab_id,
                                                        box_id = search_raw_output[i][n].box_id,
                                                        position = search_raw_output[i][n].position,
                                                        id = search_raw_output[i][n].id, 
                                                        sample_date = str(search_raw_output[i][n].sample_date), 
                                                        volume_ml = str(search_raw_output[i][n].volume_ml), 
                                                        user_id = search_raw_output[i][n].user_id, 
                                                        notes = search_raw_output[i][n].notes))
                elif search_raw_output[0][i-1] == "Other":
                    search_output.append(Search_Result(sample_type = search_raw_output[0][i-1],
                                                        lab_id = search_raw_output[i][n].lab_id,
                                                        box_id = search_raw_output[i][n].box_id,
                                                        position = search_raw_output[i][n].position, 
                                                        id = search_raw_output[i][n].id, 
                                                        sample_date = str(search_raw_output[i][n].sample_date), 
                                                        volume_ml = str(search_raw_output[i][n].volume_ml), 
                                                        user_id = search_raw_output[i][n].user_id, 
                                                        notes = search_raw_output[i][n].notes))
        
        print(search_raw_output)
        print(search_output)
        print()
        
        for i in range(len(search_output)):
            if (len(search_output[i].box_id) > 20):
                search_output[i].box_id = "-"
            if (len(search_output[i].id) > 20):
                search_output[i].id = "-"
            if (search_output[i].sample_date == "1900-01-01"):
                search_output[i].sample_date = "-"
            if (search_output[i].passage_number == "-9999"):
                search_output[i].passage_number = "-" 
            if (search_output[i].passage_number == None):
                search_output[i].passage_number = "[N/A]"
            if (search_output[i].volume_ml == "-9999"):
                search_output[i].volume_ml = "-"
            if (search_output[i].volume_ml == "0.0"):
                search_output[i].volume_ml = "-"
            if (search_output[i].growth_media == "UNKNOWN"):
                search_output[i].growth_media = "-"
            if (search_output[i].growth_media == None):
                search_output[i].growth_media = "[N/A]"
            if (search_output[i].batch_number == "-9999"):
                search_output[i].batch_number = "-"
            if (search_output[i].batch_number == None):
                search_output[i].batch_number = "[N/A]"
            if (search_output[i].lot_number == "-UNKNOWN"):
                search_output[i].lot_number = "-"
            if (search_output[i].lot_number == None):
                search_output[i].lot_number = "[N/A]"
            if (search_output[i].cell_count == "-9999"):
                search_output[i].cell_count = "-"
            if (search_output[i].cell_count == None):
                search_output[i].cell_count = "[N/A]"
            if (search_output[i].visit_number == "-9999"):
                search_output[i].visit_number = "-"
            if (search_output[i].visit_number == None):
                search_output[i].visit_number = "[N/A]"
            if (search_output[i].pathwest_id == "UNKNOWN"):
                search_output[i].pathwest_id = "-"
            if (search_output[i].pathwest_id == None):
                search_output[i].pathwest_id = "[N/A]"
            if (search_output[i].patient_code == "UNKNOWN"):
                search_output[i].patient_code = "-"
            if (search_output[i].patient_code == None):
                search_output[i].patient_code = "[N/A]"
            if (search_output[i].notes == "UNKNOWN"):
                search_output[i].notes = "-"
            if (search_output[i].notes == None):
                search_output[i].notes = "[N/A]"
            if (search_output[i].vial_source == "UNKNOWN"):
                search_output[i].vial_source = "-"
            if (search_output[i].vial_source == None):
                search_output[i].vial_source = "[N/A]"
            if (search_output[i].user_id == "UNKNOWN"):
                search_output[i].user_id = "-"
            if (search_output[i].user_id == None):
                search_output[i].user_id = "[N/A]"

        return render_template(
            'search_base.html',
            sample_type='search_result',
            target_sample_header_html_file='search_header_stub.html',
            target_sample_data_html_file='search_data_stub.html',
            samples=search_output,
            form=form,
            title="Samples"
        )

    return render_template(
        'search_form.html',
        form=form,
        title="Samples Search")
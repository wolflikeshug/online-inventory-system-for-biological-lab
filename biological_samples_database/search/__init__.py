"""

Cell Line

All API information related to Cell Line samples

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

from ..model.sample import Search_Result

from .search_from_database import query_data_from_database

SEARCH = Blueprint(
    'search_output',
    __name__,
    template_folder='templates'
)

class SearchForm(FlaskForm):
    '''Website link for page holding RSS data'''

    Serum_sele = BooleanField('Serum', default=False)
    Virus_Isolation_sele = BooleanField('Virus Isolation', default=False)
    Virus_Culture_sele = BooleanField('Virus Culture', default=False)
    Plasma_sele = BooleanField('Plasma', default=False)
    PBMC_sele = BooleanField('PBMC', default=False)
    Cell_Line_sele = BooleanField('Cell Line', default=False)
    Mosquito_sele = BooleanField('Mosquito', default=False)
    Antigen_sele = BooleanField('Antigen', default=False)
    RNA_sele = BooleanField('RNA', default=False)
    Peptide_sele = BooleanField('Peptide', default=False)
    Supernatant_sele = BooleanField('Supernatant', default=False)
    Other_sele = BooleanField('Other', default=False)

    pw_id = StringField('PW_ID')
    id = StringField('ID')
    cell_type = StringField('Type')

    start_date = DateField(
        'Start Date',
        default=datetime.strptime(
            '2022-01-01',
            '%Y-%m-%d'),
        format='%Y-%m-%d'
    )
    end_date = DateField(
        'End Date(This need to be later than the start date)',
        default=datetime.strptime(
            '2022-01-01',
            '%Y-%m-%d'),
        format='%Y-%m-%d'
    )
    need_date = BooleanField('Choose if you wish to search with a period of time', default=False)

    visit_number = IntegerField('Visit Number')
    batch_number = IntegerField('Batch Number')
    passage_number = IntegerField('Passage Number')
    cell_count = IntegerField('Total Count')
    growth_media = StringField('Media')
    vial_source = StringField('Source')
    lot_number = StringField('Lot Number')
    volume_ml = FloatField('Volume (ml)')
    patient_code = StringField('Patient Code')
    initials = StringField('Initials')
    other = StringField('Other')

search_input = [[], None, None, None, [None, None], None, None, None, None, None, None, None, None, None, None, None]

@SEARCH.route('/', methods=['GET'])
def read_all():
    """Placeholder for retrieving Cell Line data from the SQLite database"""

    form = SearchForm()

    if request.form.get('Serum_sele') == 'y':
        search_input[0].append('Serum')
    if request.form.get('Virus_Isolation_sele') == 'y':
        search_input[0].append('Virus Isolation')
    if request.form.get('Virus_Culture_sele') == 'y':
        search_input[0].append('Virus Culture')
    if request.form.get('Plasma_sele') == 'y':
        search_input[0].append('Plasma')
    if request.form.get('PBMC_sele') == 'y':
        search_input[0].append('PBMC')
    if request.form.get('Cell_Line_sele') == 'y':
        search_input[0].append('Cell Line')
    if request.form.get('Mosquito_sele') == 'y':
        search_input[0].append('Mosquito')
    if request.form.get('Antigen_sele') == 'y':
        search_input[0].append('Antigen')
    if request.form.get('RNA_sele') == 'y':
        search_input[0].append('RNA')
    if request.form.get('Peptide_sele') == 'y':
        search_input[0].append('Peptide')
    if request.form.get('Supernatant_sele') == 'y':
        search_input[0].append('Supernatant')
    if request.form.get('Other_sele') == 'y':
        search_input[0].append('Other')
    
    search_input[1] = request.form.get('pw_id')
    search_input[2] = request.form.get('id')
    search_input[3] = request.form.get('cell_type')
    if request.form.get('need_date') == 'y':
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
    search_input[14] = request.form.get('initials')
    search_input[15] = request.form.get('other')

    search_raw_output = query_data_from_database(search_input)
    search_output = []
    for i in range(0, search_raw_output[0]):
        for n in range(0, search_raw_output[i]):
            if search_raw_output[0][i] == "Serum":
                search_output.append(Search_Result(pathwest_id = search_raw_output[i][n].pathwest_id, \
                                                    id = search_raw_output[i][n].id, \
                                                    sample_date = search_raw_output[i][n].sample_date, \
                                                    volume_ml = search_raw_output[i][n].volume_ml, \
                                                    initials = search_raw_output[i][n].initials, \
                                                    other = search_raw_output[i][n].other))
            elif search_raw_output[0][i] == "Virus Isolation":
                search_output.append(Search_Result(pathwest_id = search_raw_output[i][n].pathwest_id, \
                                                    id = search_raw_output[i][n].id,\
                                                    sample_date = search_raw_output[i][n].sample_date, \
                                                    batch_number = search_raw_output[i][n].batch_number, \
                                                    passage_number = search_raw_output[i][n].passage_number, \
                                                    growth_media = search_raw_output[i][n].growth_media, \
                                                    volume_ml = search_raw_output[i][n].volume_ml, \
                                                    initials = search_raw_output[i][n].initials, \
                                                    other = search_raw_output[i][n].other))
            elif search_raw_output[0][i] == "Virus Culture":
                search_output.append(Search_Result(pathwest_id = search_raw_output[i][n].pathwest_id, \
                                                    id = search_raw_output[i][n].id, sample_date = search_raw_output[i][n].sample_date, \
                                                    batch_number = search_raw_output[i][n].batch_number, \
                                                    passage_number = search_raw_output[i][n].passage_number, \
                                                    growth_media = search_raw_output[i][n].growth_media, \
                                                    volume_ml = search_raw_output[i][n].volume_ml, \
                                                    initials = search_raw_output[i][n].initials, \
                                                    other = search_raw_output[i][n].other))
            elif search_raw_output[0][i] == "Plasma":
                search_output.append(Search_Result(id = search_raw_output[i][n].id, \
                                                    sample_date = search_raw_output[i][n].sample_date, \
                                                    visit_number = search_raw_output[i][n].visit_number, \
                                                    volume_ml = search_raw_output[i][n].volume_ml, \
                                                    initials = search_raw_output[i][n].initials, \
                                                    other = search_raw_output[i][n].other))
            elif search_raw_output[0][i] == "PBMC":
                search_output.append(Search_Result(id = search_raw_output[i][n].id, \
                                                    sample_date = search_raw_output[i][n].sample_date, \
                                                    visit_number = search_raw_output[i][n].visit_number, \
                                                    volume_ml = search_raw_output[i][n].volume_ml, \
                                                    patient_code = search_raw_output[i][n].patient_code, \
                                                    initials = search_raw_output[i][n].initials, \
                                                    other = search_raw_output[i][n].other))
            elif search_raw_output[0][i] == "Cell Line":
                search_output.append(Search_Result(id = search_raw_output[i][n].id, \
                                                    cell_type = search_raw_output[i][n].cell_type, \
                                                    sample_date = search_raw_output[i][n].sample_date, \
                                                    passage_number = search_raw_output[i][n].passage_number, \
                                                    cell_count = search_raw_output[i][n].cell_count, \
                                                    growth_media = search_raw_output[i][n].growth_media, \
                                                    lot_number = search_raw_output[i][n].lot_number, \
                                                    volume_ml = search_raw_output[i][n].volume_ml, \
                                                    initials = search_raw_output[i][n].initials, \
                                                    other = search_raw_output[i][n].other))
            elif search_raw_output[0][i] == "Mosquito":
                search_output.append(Search_Result(id = search_raw_output[i][n].id, \
                                                    sample_date = search_raw_output[i][n].sample_date, \
                                                    volume_ml = search_raw_output[i][n].volume_ml, \
                                                    initials = search_raw_output[i][n].initials, \
                                                    other = search_raw_output[i][n].other))
            elif search_raw_output[0][i] == "Antigen":
                search_output.append(Search_Result(pathwest_id = search_raw_output[i][n].pathwest_id, \
                                                    id = search_raw_output[i][n].id, \
                                                    sample_date = search_raw_output[i][n].sample_date, \
                                                    batch_number = search_raw_output[i][n].batch_number, \
                                                    lot_number = search_raw_output[i][n].lot_number, \
                                                    volume_ml = search_raw_output[i][n].volume_ml, \
                                                    initials = search_raw_output[i][n].initials, \
                                                    other = search_raw_output[i][n].other))
            elif search_raw_output[0][i] == "RNA":
                search_output.append(Search_Result(pathwest_id = search_raw_output[i][n].pathwest_id, \
                                                    id = search_raw_output[i][n].id, \
                                                    sample_date = search_raw_output[i][n].sample_date, \
                                                    batch_number = search_raw_output[i][n].batch_number, \
                                                    lot_number = search_raw_output[i][n].lot_number, \
                                                    volume_ml = search_raw_output[i][n].volume_ml, \
                                                    initials = search_raw_output[i][n].initials, \
                                                    other = search_raw_output[i][n].other))
            elif search_raw_output[0][i] == "Peptide":
                search_output.append(Search_Result(id = search_raw_output[i][n].id, \
                                                    cell_type = search_raw_output[i][n].cell_type, \
                                                    sample_date = search_raw_output[i][n].sample_date, \
                                                    batch_number = search_raw_output[i][n].batch_number, \
                                                    vial_source = search_raw_output[i][n].vial_source, \
                                                    lot_number = search_raw_output[i][n].lot_number, \
                                                    volume_ml = search_raw_output[i][n].volume_ml, \
                                                    initials = search_raw_output[i][n].initials, \
                                                    other = search_raw_output[i][n].other))
            elif search_raw_output[0][i] == "Supernatant":
                search_output.append(Search_Result(id = search_raw_output[i][n].id, \
                                                    sample_date = search_raw_output[i][n].sample_date, \
                                                    volume_ml = search_raw_output[i][n].volume_ml, \
                                                    initials = search_raw_output[i][n].initials, \
                                                    other = search_raw_output[i][n].other))
            elif search_raw_output[0][i] == "Other":
                search_output.append(Search_Result(id = search_raw_output[i][n].id, \
                                                    sample_date = search_raw_output[i][n].sample_date, \
                                                    volume_ml = search_raw_output[i][n].volume_ml, \
                                                    initials = search_raw_output[i][n].initials, \
                                                    other = search_raw_output[i][n].other))
    return render_template(
        'search_base.html',
        sample_type='search_result',
        target_sample_header_html_file='search_header_stub.html',
        target_sample_data_html_file='search_data_stub.html',
        samples=search_output,
        form=form
    )

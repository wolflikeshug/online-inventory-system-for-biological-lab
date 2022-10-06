"""

Search

All API information related to search samples

"""
# Flask
from flask import Blueprint, render_template

# Local imports
from ..model.search import Search_Result
from ..model.storage import Box
from .search_from_database import query_data_from_database
from ..forms import SearchForm
from ..database import create_new_session
from biological_samples_database.authentication import guest_required


SEARCH = Blueprint(
    'search_output',
    __name__,
    template_folder='templates'
)

search_input = [[], None, None, None, [None, None], None, None, None, None, None, None, None, None, None, None, None, 0]


@SEARCH.route('/', methods=['GET', 'POST'])
@guest_required
def search():
    form = SearchForm()

    if form.validate_on_submit():
        
        #print(form.data)

        search_input[0] = form.sample_type.data
        search_input[1] = form.pw_id.data
        search_input[2] = form.id.data
        search_input[3] = form.cell_type.data
        if form.need_date.data:
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
        search_input[16] = int(form.used.data)

        #print(search_input)
        
        search_raw_output = query_data_from_database(search_input)
        search_output = []
        with create_new_session() as session:
            for i in range(1, len(search_raw_output)):
                for n in range(0, len(search_raw_output[i])):
                    box = session.query(
                            Box
                        ).filter(
                            Box.id == search_raw_output[i][n].box_id
                        ).first()
                    box_label = "[N/A]"
                    if box:
                            box_label = box.label
                        
                    if search_raw_output[0][i-1] == "Serum":
                        search_output.append(Search_Result(sample_type = search_raw_output[0][i-1], 
                                                            lab_id = search_raw_output[i][n].lab_id,
                                                            box_id = search_raw_output[i][n].box_id,
                                                            box_name = box_label,
                                                            position = search_raw_output[i][n].position,
                                                            pathwest_id = search_raw_output[i][n].pathwest_id, 
                                                            id = search_raw_output[i][n].id, 
                                                            sample_date = str(search_raw_output[i][n].sample_date), 
                                                            volume_ml = str(search_raw_output[i][n].volume_ml), 
                                                            user_id = search_raw_output[i][n].user_id, 
                                                            notes = search_raw_output[i][n].notes,
                                                            used = str(search_raw_output[i][n].used)))
                    elif search_raw_output[0][i-1] == "Virus Isolation":
                        search_output.append(Search_Result(sample_type = search_raw_output[0][i-1], 
                                                            lab_id = search_raw_output[i][n].lab_id,
                                                            box_id = search_raw_output[i][n].box_id,
                                                            box_name = box_label,
                                                            position = search_raw_output[i][n].position,
                                                            pathwest_id = search_raw_output[i][n].pathwest_id, 
                                                            id = search_raw_output[i][n].id,
                                                            sample_date = str(search_raw_output[i][n].sample_date), 
                                                            batch_number = search_raw_output[i][n].batch_number, 
                                                            passage_number = search_raw_output[i][n].passage_number, 
                                                            growth_media = search_raw_output[i][n].growth_media, 
                                                            volume_ml = str(search_raw_output[i][n].volume_ml), 
                                                            user_id = search_raw_output[i][n].user_id, 
                                                            notes = search_raw_output[i][n].notes,
                                                            used = str(search_raw_output[i][n].used)))
                    elif search_raw_output[0][i-1] == "Virus Culture":
                        search_output.append(Search_Result(sample_type = search_raw_output[0][i-1], 
                                                            lab_id = search_raw_output[i][n].lab_id,
                                                            box_id = search_raw_output[i][n].box_id,
                                                            box_name = box_label,
                                                            position = search_raw_output[i][n].position,
                                                            pathwest_id = search_raw_output[i][n].pathwest_id, 
                                                            id = search_raw_output[i][n].id, 
                                                            sample_date = str(search_raw_output[i][n].sample_date), 
                                                            batch_number = search_raw_output[i][n].batch_number, 
                                                            passage_number = search_raw_output[i][n].passage_number, 
                                                            growth_media = search_raw_output[i][n].growth_media, 
                                                            volume_ml = str(search_raw_output[i][n].volume_ml), 
                                                            user_id = search_raw_output[i][n].user_id, 
                                                            notes = search_raw_output[i][n].notes,
                                                            used = str(search_raw_output[i][n].used)))
                    elif search_raw_output[0][i-1] == "Plasma":
                        search_output.append(Search_Result(sample_type = search_raw_output[0][i-1], 
                                                            lab_id = search_raw_output[i][n].lab_id,
                                                            box_id = search_raw_output[i][n].box_id,
                                                            box_name = box_label,
                                                            position = search_raw_output[i][n].position,
                                                            id = search_raw_output[i][n].id, 
                                                            sample_date = str(search_raw_output[i][n].sample_date), 
                                                            visit_number = search_raw_output[i][n].visit_number, 
                                                            volume_ml = str(search_raw_output[i][n].volume_ml), 
                                                            user_id = search_raw_output[i][n].user_id, 
                                                            notes = search_raw_output[i][n].notes,
                                                            used = str(search_raw_output[i][n].used)))
                    elif search_raw_output[0][i-1] == "PBMC":
                        search_output.append(Search_Result(sample_type = search_raw_output[0][i-1], 
                                                            lab_id = search_raw_output[i][n].lab_id,
                                                            box_id = search_raw_output[i][n].box_id,
                                                            box_name = box_label,
                                                            position = search_raw_output[i][n].position,
                                                            id = search_raw_output[i][n].id, 
                                                            sample_date = str(search_raw_output[i][n].sample_date), 
                                                            visit_number = search_raw_output[i][n].visit_number, 
                                                            volume_ml = str(search_raw_output[i][n].volume_ml), 
                                                            patient_code = search_raw_output[i][n].patient_code, 
                                                            user_id = search_raw_output[i][n].user_id, 
                                                            notes = search_raw_output[i][n].notes,
                                                            used = str(search_raw_output[i][n].used)))
                    elif search_raw_output[0][i-1] == "Cell Line":
                        search_output.append(Search_Result(sample_type = search_raw_output[0][i-1], 
                                                            lab_id = search_raw_output[i][n].lab_id,
                                                            box_id = search_raw_output[i][n].box_id,
                                                            box_name = box_label,
                                                            position = search_raw_output[i][n].position,
                                                            id = search_raw_output[i][n].id, 
                                                            cell_type = search_raw_output[i][n].cell_type, 
                                                            sample_date = str(search_raw_output[i][n].sample_date), 
                                                            passage_number = search_raw_output[i][n].passage_number, 
                                                            cell_count = str(search_raw_output[i][n].cell_count), 
                                                            growth_media = search_raw_output[i][n].growth_media, 
                                                            lot_number = search_raw_output[i][n].lot_number, 
                                                            volume_ml = str(search_raw_output[i][n].volume_ml), 
                                                            user_id = search_raw_output[i][n].user_id, 
                                                            notes = search_raw_output[i][n].notes,
                                                            used = str(search_raw_output[i][n].used)))
                    elif search_raw_output[0][i-1] == "Mosquito":
                        search_output.append(Search_Result(sample_type = search_raw_output[0][i-1], 
                                                            lab_id = search_raw_output[i][n].lab_id,
                                                            box_id = search_raw_output[i][n].box_id,
                                                            box_name = box_label,
                                                            position = search_raw_output[i][n].position,
                                                            id = search_raw_output[i][n].id, 
                                                            sample_date = str(search_raw_output[i][n].sample_date), 
                                                            volume_ml = str(search_raw_output[i][n].volume_ml), 
                                                            user_id = search_raw_output[i][n].user_id, 
                                                            notes = search_raw_output[i][n].notes,
                                                            used = str(search_raw_output[i][n].used)))
                    elif search_raw_output[0][i-1] == "Antigen":
                        search_output.append(Search_Result(sample_type = search_raw_output[0][i-1], 
                                                            lab_id = search_raw_output[i][n].lab_id,
                                                            box_id = search_raw_output[i][n].box_id,
                                                            box_name = box_label,
                                                            position = search_raw_output[i][n].position,
                                                            pathwest_id = search_raw_output[i][n].pathwest_id, 
                                                            id = search_raw_output[i][n].id, 
                                                            sample_date = str(search_raw_output[i][n].sample_date), 
                                                            batch_number = search_raw_output[i][n].batch_number, 
                                                            lot_number = search_raw_output[i][n].lot_number, 
                                                            volume_ml = str(search_raw_output[i][n].volume_ml), 
                                                            user_id = search_raw_output[i][n].user_id, 
                                                            notes = search_raw_output[i][n].notes,
                                                            used = str(search_raw_output[i][n].used)))
                    elif search_raw_output[0][i-1] == "Rna":
                        search_output.append(Search_Result(sample_type = search_raw_output[0][i-1],
                                                            lab_id = search_raw_output[i][n].lab_id,
                                                            box_id = search_raw_output[i][n].box_id,
                                                            box_name = box_label,
                                                            position = search_raw_output[i][n].position, 
                                                            pathwest_id = search_raw_output[i][n].pathwest_id, 
                                                            id = search_raw_output[i][n].id, 
                                                            sample_date = str(search_raw_output[i][n].sample_date),
                                                            volume_ml = str(search_raw_output[i][n].volume_ml), 
                                                            user_id = search_raw_output[i][n].user_id, 
                                                            notes = search_raw_output[i][n].notes,
                                                            used = str(search_raw_output[i][n].used)))
                    elif search_raw_output[0][i-1] == "Peptide":
                        search_output.append(Search_Result(sample_type = search_raw_output[0][i-1], 
                                                            lab_id = search_raw_output[i][n].lab_id,
                                                            box_id = search_raw_output[i][n].box_id,
                                                            box_name = box_label,
                                                            position = search_raw_output[i][n].position,
                                                            id = search_raw_output[i][n].id, 
                                                            cell_type = search_raw_output[i][n].cell_type, 
                                                            sample_date = str(search_raw_output[i][n].sample_date), 
                                                            batch_number = search_raw_output[i][n].batch_number, 
                                                            vial_source = search_raw_output[i][n].vial_source, 
                                                            lot_number = search_raw_output[i][n].lot_number, 
                                                            volume_ml = str(search_raw_output[i][n].volume_ml), 
                                                            user_id = search_raw_output[i][n].user_id, 
                                                            notes = search_raw_output[i][n].notes,
                                                            used = str(search_raw_output[i][n].used)))
                    elif search_raw_output[0][i-1] == "Supernatant":
                        search_output.append(Search_Result(sample_type = search_raw_output[0][i-1], 
                                                            lab_id = search_raw_output[i][n].lab_id,
                                                            box_id = search_raw_output[i][n].box_id,
                                                            box_name = box_label,
                                                            position = search_raw_output[i][n].position,
                                                            id = search_raw_output[i][n].id, 
                                                            sample_date = str(search_raw_output[i][n].sample_date), 
                                                            volume_ml = str(search_raw_output[i][n].volume_ml), 
                                                            user_id = search_raw_output[i][n].user_id, 
                                                            notes = search_raw_output[i][n].notes,
                                                            used = str(search_raw_output[i][n].used)))
                    elif search_raw_output[0][i-1] == "Other":
                        search_output.append(Search_Result(sample_type = search_raw_output[0][i-1],
                                                            lab_id = search_raw_output[i][n].lab_id,
                                                            box_id = search_raw_output[i][n].box_id,
                                                            box_name = box_label,
                                                            position = search_raw_output[i][n].position, 
                                                            id = search_raw_output[i][n].id, 
                                                            sample_date = str(search_raw_output[i][n].sample_date), 
                                                            volume_ml = str(search_raw_output[i][n].volume_ml), 
                                                            user_id = search_raw_output[i][n].user_id, 
                                                            notes = search_raw_output[i][n].notes,
                                                            used = str(search_raw_output[i][n].used)))
        
        #print(search_raw_output)
        #print(search_output)
        #print()
        
        for i in range(len(search_output)):
            #Needed values for box,edit, delete links (No longer displayed):
            if (search_output[i].sample_date == "1900-01-01"):
                search_output[i].sample_date = "-"
            if (search_output[i].passage_number == "UNKNOWN"):#
                search_output[i].passage_number = "-" 
            if (search_output[i].passage_number == None):
                search_output[i].passage_number = "[N/A]"
            if (search_output[i].volume_ml == "-9999.0"):
                search_output[i].volume_ml = "-"
            if (search_output[i].volume_ml == "-"):
                search_output[i].volume_ml = "-"
            if (search_output[i].growth_media == "UNKNOWN"):
                search_output[i].growth_media = "-"
            if (search_output[i].growth_media == None):
                search_output[i].growth_media = "[N/A]"
            if (search_output[i].batch_number == "UNKNOWN"):#
                search_output[i].batch_number = "-"
            if (search_output[i].batch_number == None):
                search_output[i].batch_number = "[N/A]"
            if (search_output[i].lot_number == "UNKNOWN"):
                search_output[i].lot_number = "-"
            if (search_output[i].lot_number == None):
                search_output[i].lot_number = "[N/A]"
            if (search_output[i].cell_count == "-9999"):
                search_output[i].cell_count = "-"
            if (search_output[i].cell_count == None):
                search_output[i].cell_count = "[N/A]"
            if (search_output[i].visit_number == "UNKNOWN"):#
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
            if (search_output[i].cell_type == "UNKNOWN"):
                search_output[i].cell_type = "-"
            if (search_output[i].cell_type == None):
                search_output[i].cell_type = "[N/A]"

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
        title="Samples")
"""
User

"""

# System
import os
from werkzeug.utils import secure_filename
# Flask
from flask import Blueprint, render_template, current_app, redirect, request
from ..forms import UploadFileForm
# Local Imports

from ..authentication import phd_required
UPLOAD = Blueprint(
    'upload',
    __name__,
    template_folder='templates'
)

@UPLOAD.route("/", methods=['GET','POST'])
@phd_required
def home():
    form = UploadFileForm()
    if form.validate_on_submit():
        file = form.file.data # First grab the file
        path = os.path.join(current_app.root_path,current_app.config['UPLOAD_FOLDER'],secure_filename(file.filename)) #Build path
        file.save(path)# Then save the file
        return redirect(request.referrer)
    return render_template('import.html', form=form)





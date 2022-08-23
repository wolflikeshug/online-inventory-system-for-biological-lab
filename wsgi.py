'''
    WSGI Configuration File

    @author: run.seven
    @date:   20-Aug-2022


    TO START RUN THIS IN THE FOLDER WITH THE WSGI.PY FILE
    gunicorn --bind 0.0.0.0:5000 bio:app

    gunicorn --timeout 6000 --access-logfile logs/incident_management.log
             --error-logfile logs/incident_management.log -b 0.0.0.0:3000 wsgi
    gunicorn --timeout 6000  -b 0.0.0.0:5000 wsgi

'''

from waitress import serve

import biological_samples_database as bio
application = bio.initialise_app()

if __name__ == '__main__':
    serve(
        application,
        host='0.0.0.0',
        port=5000)

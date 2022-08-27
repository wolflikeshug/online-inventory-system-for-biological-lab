'''
    WSGI Configuration File

    @author: run.seven
    @date:   20-Aug-2022

'''

from waitress import serve

import biological_samples_database as bio

application = bio.initialise_app()

if __name__ == '__main__':
    serve(
        application,
        host='127.0.0.1',
        port=5000)


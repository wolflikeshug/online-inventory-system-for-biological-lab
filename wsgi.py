'''
    WSGI Configuration File

    @author: run.seven
    @date:   20-Aug-2022

'''

from waitress import serve

import src as bio

# <--- Simon's code ---
application = bio.initialise_app()

if __name__ == '__main__':
    serve(
        application,
        host='0.0.0.0',
        port=5000)
# --- Simon's code --->

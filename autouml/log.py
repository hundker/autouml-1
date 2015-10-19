'''
plantuml files are generated through a logger
'''

import logging
import logging.handlers
import atexit


logger = logging.getLogger('autouml')

handler1 = logging.handlers.RotatingFileHandler('autouml.log', backupCount=0)
handler2 = logging.FileHandler('autouml.log')

log_format = logging.Formatter('%(message)s')

handler1.setFormatter(log_format)
handler2.setFormatter(log_format)


handler1.doRollover()
logger.addHandler(handler1)
# logger.addHandler(handler2)

logger.setLevel(logging.INFO)


logger.info("/' Log generated by autouml '/")
logger.info('''@startuml
skinparam handwritten true''')


def closeuml():
    '''
    Closes plantuml diagram syntax and tries to generate the image.
    Intended to be called on program exit
    '''
    logger.info("@enduml")
    try:
        import plantuml
        logger.info("/' generating image at autouml.png'/")
        plantuml.PlantUML().processes_file('autouml.log', outfile='autouml.png')
    except Exception, captured_except:
        logger.error('Unable to generate image file')
        logger.error(captured_except)


atexit.register(closeuml)

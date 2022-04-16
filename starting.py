import logging
from botDB import db_dir
from botTools import mkdir, init_db
from botSession import scheduler, idle_mark
from register import register_handlers, manager


def starting():
    logging.basicConfig(
        format='%(asctime)s %(levelname)-8s %(message)s',
        level=logging.INFO,
        datefmt='%Y-%m-%d %H:%M:%S')

    register_handlers()
    manager()
    scheduler.start()

    mkdir(db_dir)
    init_db('NGA')

    idle_mark.buf[0] = 1

    return logging.info('Starting fine.')

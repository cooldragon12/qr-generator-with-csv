from helpers.exceptions import DirectoryNotFoundError, FileNotFoundError
from qr.generator import QRGenerator
from helpers.parser import parse_args
from helpers.validators import check_if_file_exists
from settings import LOG_FILE as LOGS_LOCATION
import logging.config
import logging
from os import path

logging.config.fileConfig(
    fname=path.join(path.dirname(path.dirname(path.abspath(__file__))), "config\\logging_config.ini"),
    defaults={
        "logfilename": LOGS_LOCATION
    },
    disable_existing_loggers=False,
    encoding="utf-8"
    )
logger = logging.getLogger()


def main(args):
    # Let's give a little message that the program is running
    logger.info(
'''
===========================================
=     WELCOME LET's MAkE YOUR QR          =
=                                         =
=       Created by: GE WebDue3s           =
===========================================
'''
    )
    try:
        # Let's check if the user wants to insert a logo in the qr code
        if args.logo is None:
            # Let's check if the user wants to insert a logo in the qr code
            qr = QRGenerator(args.data)
        else:
            # Let's generate the qr code
            qr = QRGenerator(args.data, logo=args.logo)


        for data in qr.start_generate():
            if not check_if_file_exists(path.join(qr.output, f'{data}.png')):
                raise FileNotFoundError(f'QR Code Generation Failed: {data}')
            else:
                logger.info(f'QR Code Generated: {data}')
        logger.info(f'QR Codes has been saved in this location: {qr.output}')
        logger.info("QR Code Generation Completed")
    
    except Exception as e:
        logger.error(e, exc_info=True)

    logger.info("Exiting Program")



if __name__ == '__main__':
    args = parse_args()
    main(args)
import logging

# logger = logging.getLogger(__name__)
# logger.setLevel(level=logging.INFO)
# handler = logging.FileHandler('./out/output.log')
# formatter = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')
# handler.addFormatter(formatter)
# logger.addHandler(handler)
logging.basicConfig(filename='./out/output.log', level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s', datefmt='%m/%d/%Y')


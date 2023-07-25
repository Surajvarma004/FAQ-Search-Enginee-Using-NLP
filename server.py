from app import app
from config import *
from waitress import serve
import logging


logger = logging.getLogger("main")


logger.debug("[INFO] Server Started....")
serve(app, host=SERVER, port=PORT)
print("Serving on http:{}/{}".format(SERVER, PORT))
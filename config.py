import os

PORT = os.environ.get("PORT",'9555')
MAX_ADS_TO_SERVE = int(os.environ.get("MAX_ADS_TO_SERVE",'2'))
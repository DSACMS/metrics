import datetime, os

BASE_PATH = os.path.dirname(os.path.abspath(__file__))
# Folder Names to send over our projects tracked data
PATH_TO_METRICS_DATA = "_data"
PATH_TO_METADATA = "_metadata"
DATESTAMP = datetime.datetime.now().date().isoformat()
TOKEN = os.getenv("GITHUB_TOKEN")
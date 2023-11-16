"""
Defines constants for use in metricsLib
"""
import datetime
import os
from pathlib import Path

TIMEOUT_IN_SECONDS = 60
BASE_PATH = os.path.dirname(os.path.abspath(__file__))
# Folder Names to send over our projects tracked data
PATH_TO_METRICS_DATA = (Path(__file__).parent /
                        "../../app/site/_data").resolve()
PATH_TO_REPORTS_DATA = (Path(__file__).parent /
                        "../../app/site/_posts").resolve()
PATH_TO_GRAPHS_DATA = (Path(__file__).parent /
                       "../../app/site/_graphs").resolve()

PATH_TO_METADATA = Path("_metadata").resolve()
DATESTAMP = datetime.datetime.now().date().isoformat()
TOKEN = os.getenv("GITHUB_TOKEN")
GH_GQL_ENDPOINT = "https://api.github.com/graphql"

PATH_TO_TEMPLATES = (Path(__file__).parent / "../../templates").resolve()

template_path = os.path.join(PATH_TO_TEMPLATES, "repo_report_template.md")
with open(template_path, "r", encoding="utf-8") as file:
    REPO_REPORT_TEMPLATE = file.read()

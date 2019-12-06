import json
import textwrap
import os
import pandas as pd
from sqlalchemy import DateTime, String
from sqlalchemy.sql import column

from superset import db, security_manager
from superset.connectors.sqla.models import SqlMetric, TableColumn
from superset.utils.core import get_example_database

from .helpers import (
    config,
    Dash,
    get_example_data,
    get_slice_json,
    merge_slice,
    misc_dash_slices,
    Slice,
    TBL,
    update_slice_ids,
)

with open("./superset/examples/d2Dec.json") as f:
    data = json.load(f)

# print(data)

def load_couture_dashboard(only_metadata=False, force=False):

    print("Creating Couture Dashboards...")

    dash = db.session.query(Dash).filter_by(slug="d2-couture").first()
    dash.slug = "d2-couture"


    db.session.add(dash)
    db.session.commit()



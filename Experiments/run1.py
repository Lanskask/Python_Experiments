import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile


from sqlalchemy import create_engine
engine = create_engine('sqlite://', echo=False)

engine.execute("""select * from Availability where "('Grade', 'Location')" == 'Saint-Petersburg'""").fetchall()



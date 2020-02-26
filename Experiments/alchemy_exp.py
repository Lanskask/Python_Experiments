from sqlalchemy import create_engine

engine = create_engine('sqlite://', echo=False)

engine.execute('DROP TABLE IF EXISTS Availability')


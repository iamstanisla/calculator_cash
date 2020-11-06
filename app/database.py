from pony.orm import Database


db = Database()
db.bind(**app.config['PONY'])
db.generate_mapping(create_tables=True)

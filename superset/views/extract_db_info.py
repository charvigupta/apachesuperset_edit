import sqlite3


## path to .db
connection = sqlite3.connect("/home/charvi/.superset/superset.db")

def sql_table_fetch(con):
	
	datasource_dict = {}
	database_dict = {}

	cursorObj = con.cursor()
	cursorObj.execute('SELECT * FROM tables')
	rows = cursorObj.fetchall()
	for row in rows:

		db_val = str(list(row)[6])
		param = list(row)[-5:-4][0].split(".")
		db_key = param[0][1:-1]
		ds_key = param[-1].split("](id:")[0][1:]
		ds_value = param[-1].split("](id:")[1][:-1]
		
		database_dict[db_key] = db_val
		datasource_dict[ds_key] = ds_value
	
	return datasource_dict, database_dict

datasource_dict, database_dict = sql_table_fetch(connection)


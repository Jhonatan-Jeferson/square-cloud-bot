#pylint:disable=E0401
import sqlite3 as db


class MongoDB:
	
	def __init__(self):
		
		pass
		
class SQLDatabase:
	
	def __init__(self):
		
		pass

class Database:
	
	def __new__(cls):
		
		from bot.config import database_type 
		
		if database_type == str("local"):
			return SQLDatabase()
		elif database_type == str("nuvem"):
			return MongoDB()
		else:
			return super().__new__(cls)
		
		
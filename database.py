import sqlite3

database = sqlite3.connect('database.db')
cursor = database.cursor()

def add_user(message):
	cursor.execute("SELECT id FROM users WHERE id=?",(message.chat.id,))
	user = cursor.fetchone()
	if not user:
		cursor.execute("INSERT INTO users VALUES(?,?,?,?)",(message.chat.id,'name','numb','klass'))
		database.commit()
	else:
		pass


def add_user_name(message):
	cursor.execute("UPDATE users SET name=? WHERE id=?",(message.text, message.chat.id,))
	database.commit()

def add_user_numb(message):
	cursor.execute("UPDATE users SET numb=? WHERE id=?",(message.text, message.chat.id,))
	database.commit()

def add_user_klass(message):
	cursor.execute("UPDATE users SET klass=? WHERE id=?",(message.text, message.chat.id,))
	database.commit()
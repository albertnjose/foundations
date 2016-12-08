
import csv, sqlite3

con = sqlite3.connect("twittertop100.db")
con.text_factory = str
cur = con.cursor()

input_file = input("Please enter csv filename: ")
with open(input_file,'r') as fin: # `with` statement available in 2.5+
    # csv.DictReader uses first line in file for column headings by default
    dr = csv.DictReader(fin) # comma is default delimiter
    to_db = [(i['user'], i['id'], i['created_at'], i['text']) for i in dr]

cur.executemany("INSERT INTO t (user, id, created_at, text) VALUES (?, ?, ?, ?);", to_db)
con.commit()
con.close()
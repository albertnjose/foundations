import csv, sqlite3

con = sqlite3.connect("twittertop100.db")
con.text_factory = str
cur = con.cursor()
cur.execute("CREATE TABLE t (user, id, created_at, text);") # use your column names here

with open('realDonaldTrump_tweets.csv','rb') as fin: # `with` statement available in 2.5+
    # csv.DictReader uses first line in file for column headings by default
    dr = csv.DictReader(fin) # comma is default delimiter
    to_db = [(i['user'], i['id'], i['created_at'], i['text']) for i in dr]

cur.executemany("INSERT INTO t (user, id, created_at, text) VALUES (?, ?, ?, ?);", to_db)
con.commit()
con.close()
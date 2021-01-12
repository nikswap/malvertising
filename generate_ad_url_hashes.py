import sqlite3
import hashlib
import sys

FILE=sys.argv[1]

conn = sqlite3.connect('ad_hash_scanner.db')
stmt = 'INSERT INTO ad_url_hash (domain,ad_hash) VALUES (?,?)'

c=conn.cursor()
counter = 0
with open(FILE,encoding='ascii',errors='ignore') as f:
    for line in f:
        md5 = hashlib.md5()
        line = line.split(' ')[-1]
        md5.update(line.encode())
        c.execute(stmt,(line,md5.hexdigest()))
    if counter % 1000 == 0:
        conn.commit()
    counter +=1
conn.commit()
c.close()
conn.close()


#!/var/www/test/.venv/bin/cgi_venv_launch

# Show better error messages in HTML output
import cgitb
cgitb.enable()

# Print necessary headers.
print("Content-Type: text/html")
print()

# Connect to the database.
#import pymysql
import mysql.connector as mariadb
conn = mariadb.connect(
    db='example',
    user='admin',
    passwd='password',
    host='localhost')
c = conn.cursor()


print("<!DOCTYPE html><html><head><title>Labor Server</title></head><body>")
# Insert some example data.
try:
    c.execute("INSERT INTO numbers VALUES (1, 'One!')")
    c.execute("INSERT INTO numbers VALUES (2, 'Two!')")
    c.execute("INSERT INTO numbers VALUES (3, 'Three!')")
    conn.commit()
    print("Entries have been added.<br>")
except mariadb.IntegrityError:
    print("Entries already present, DB not modified. <br>")

# Print the contents of the database.
c.execute("SELECT * FROM numbers")
print("<br>Entries:<br>")
for row in c.fetchall():
    num: int = int(row[0]) 
    name: str = str(row[1])
    print(f"<span style=\"display: inline-block; width: 2em; text-align: right;\">{num: 5}</span>: <span style=\"color: #34b7eb;\">{name}</span><br>")

print("</body></html>")



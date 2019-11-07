import psycopg2
import psycopg2.extras
from flask import Flask

app = Flask(__name__)


@app.route('/country/<id>')
def get_country(id):
    # Connect to an existing database
    conn = psycopg2.connect(dbname="postgres", user="postgres", password="postgres", host="localhost", port=5432)
    # Open a cursor to perform database operations
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    print("Looking for country: ", id)
    cur.execute("SELECT * FROM country WHERE country_id =  %s;", (id, )) 
    res = cur.fetchone()
    print("Found a result: ", res)
    cur.close()
    conn.close()
    return res



@app.route('/country', methods=['POST'])
def add_country():
    # Connect to an existing database
    conn = psycopg2.connect(dbname="postgres", user="postgres", password="postgres", host="localhost", port=5432)
    # Open a cursor to perform database operations
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
   
    name  = request.json.get('name')

    cur.execute("INSERT INTO country(name) VALUES(%s) ", (name,))
 


    res = cur.fetchone()
    print("Found a result: ", res)
    cur.close()
    conn.close()
    return res

@app.route('/')
def hello():
    return {"message": "Hello World!"}

if __name__ == '__main__':
    app.run()


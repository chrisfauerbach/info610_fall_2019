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


@app.route('/film/<id>')
def get_film(id):
    # Connect to an existing database
    conn = psycopg2.connect(dbname="postgres", user="postgres", password="postgres", host="localhost", port=5432)
    # Open a cursor to perform database operations
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    print("Looking for film: ", id)
    cur.execute("SELECT title,description,release_year FROM film WHERE film_id =  %s;", (id, ))
    res = cur.fetchone()
    print("Found a result: ", res)
    cur.close()
    conn.close()
    return res  

@app.route('/film/<id>/category')
def get_film_categories(id):
    # Connect to an existing database
    conn = psycopg2.connect(dbname="postgres", user="postgres", password="postgres", host="localhost", port=5432)
    # Open a cursor to perform database operations
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    print("Looking for film: ", id)
    cur.execute( """
           SELECT film.film_id, film.title, category.name FROM FILM
           join film_category on film.film_id  = film_category.film_id
            join CATEGORY on film_category.category_id = category.category_id
            where film.film_id = %s
           """
, (id, ))
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


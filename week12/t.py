import psycopg2
from  psycopg2 import extras
from flask import request
import flask
from functools import wraps
import traceback
import sys


app = flask.Flask(__name__)


def data_connection(func):
    @wraps(func)
    def wrapper_to_add(*args, **kwargs):
        cur = None
        conn = None
        try:
            conn = psycopg2.connect(dbname="postgres", user="postgres", password="postgres", host="localhost", port=5432)
            cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
            a = func(*args, cur=cur, **kwargs)
            print("Func returned a: ", a)
            conn.commit()
            
            return a
        except:
            print("Exception while processing. Will Attempt to Rollback")
            traceback.print_exc(file=sys.stdout)
            try:
                if conn:  conn.rollback()
            except:
                print("Had an issue rolling back.")
                traceback.print_exc(file=sys.stdout)
        finally:
            if cur:  cur.close()
            if conn:  conn.close()
    return wrapper_to_add


# Adding GET
@app.route('/country', methods=['GET'])
@data_connection
def get_countries(cur=None):
    name = request.args.get('name', None)
    if name:
        cur.execute("SELECT * FROM country where country = %s limit 10", (name,))
    else:
        cur.execute("SELECT * FROM country limit 10")
    res = cur.fetchall()
    print("Countries REs: ", res)
    res = {"countries": res}
    return res

#  SELECT * FROM country join continent on country.continent_id = continent.id;
# Adding GET
@app.route('/country/<id>', methods=['GET'])
@data_connection
def get_country(id, cur=None):
    cur.execute("SELECT * FROM country WHERE country_id =  %s;", (id, ))
    res = cur.fetchone()
    print("Country res: ", res)
    return res

# Adding DELETE
@app.route('/country/<id>', methods=['DELETE'])
@data_connection
def del_country(id,cur=None):
    cur.execute("DELETE FROM country WHERE country_id =  %s;", (id, ))
    res = cur.fetchone()
    return res

@app.route('/country', methods=['POST'])
@data_connection
def add_country(cur=None): 
    json_data = request.get_json()
    new_country_name = json_data.get('name')
    cur.execute("""INSERT INTO country(country, last_update) values (%s, now()) 
    returning country_id""",
      (new_country_name,))
    res = cur.fetchone()
    print(res)
    return res



if __name__ == '__main__':
    app.run()

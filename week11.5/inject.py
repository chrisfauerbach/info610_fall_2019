import sys
import traceback
import psycopg2
import psycopg2.extras

def data_connection(func):
    def wrapper_to_add(*args, **kwargs):
        cur = None
        conn = None
        try:
            conn = psycopg2.connect(dbname="postgres", user="postgres", password="postgres", host="localhost", port=5432)
            cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
            func(*args, cur=cur, **kwargs)
        except:
            print("Exception while processing. Will Attempt to Rollback")
            traceback.print_exc(file=sys.stdout)
            try:
                if cur:  cur.rollback()
            except:
                print("Had an issue rolling back.")
                traceback.print_exc(file=sys.stdout)
        finally:
            if cur:  cur.close()
            if conn:  conn.close()
    return wrapper_to_add


def my_function(parm, cur=None):
    print("Parm: ", parm)
    print("Cursor: ", cur)

@data_connection
def my_function_wrapped(parm, cur=None):
    print("Parm: ", parm)
    print("Cursor: ", cur)

if __name__ == "__main__":
    my_function("not wrapped")
    my_function_wrapped("wrapped")



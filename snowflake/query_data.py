import snowflake.connector

def run_query(conn_params, query):
    conn = snowflake.connector.connect(**conn_params)
    cur = conn.cursor()
    try:
        cur.execute(query)
        for row in cur:
            print(row)
    finally:
        cur.close()
        conn.close()

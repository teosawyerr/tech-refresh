import snowflake.connector

def load_csv_to_snowflake(conn_params, csv_path, table_name):
    conn = snowflake.connector.connect(**conn_params)
    cur = conn.cursor()
    try:
        cur.execute(f"PUT file://{csv_path} @%{table_name}")
        cur.execute(f"COPY INTO {table_name} FILE_FORMAT = (TYPE = CSV FIELD_OPTIONALLY_ENCLOSED_BY='"')")
    finally:
        cur.close()
        conn.close()

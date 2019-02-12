import sqlite3
import os

DEFAULT_PATH = os.path.join(os.path.dirname(__file__), 'pi_prices.db')



TABLE_price_all = """"""

TABLE_price_history = """CREATE TABLE price_history (QueryDate TEXT, MarketID TEXT, ContractID TEXT,
         ContractName TEXT, Date TEXT, DateString TEXT, OpenSharePrice TEXT,
          HighSharePrice TEXT, LowSharePrice TEXT, CloseSharePrice TEXT, TradeVolume  TEXT)"""

TABLE_price_hourly = """CREATE TABLE price_hourly (QueryDate TEXT, MarketID TEXT, ContractID TEXT,
         ContractName TEXT, Date TEXT, DateString TEXT, OpenSharePrice TEXT,
          HighSharePrice TEXT, LowSharePrice TEXT, CloseSharePrice TEXT, TradeVolume  TEXT)"""


TABLE_list = ['price_history', 'price_hourly', 'price_all']
ddl_list = [TABLE_price_history, TABLE_price_all, TABLE_price_hourly]

# Create database to store web data from PredictIt
def create_database(database_path=DEFAULT_PATH):
    conn = sqlite3.connect(database_path)
    with conn:
        cur = conn.cursor()
        for table in TABLE_list:
            cur.execute("DROP TABLE if exists " + table)
        for ddl in ddl_list:
            cur.execute(ddl)
    conn.close()


# Saves data to the database and
def insert_into_database(db_row: list, table_name, database_path=DEFAULT_PATH):
    conn = sqlite3.connect(database_path)
    with conn:
        cur = conn.cursor()
        sql = "INSERT INTO " + table_name + "(QueryDate, MarketID, ContractID," \
              " ContractName, Date, DateString, OpenSharePrice," \
              " HighSharePrice, LowSharePrice, CloseSharePrice, TradeVolume)" \
              "VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
        cur.execute(sql, db_row)


# Execute a SQL statement against created database
def execute_query(sql: str, database_path=DEFAULT_PATH):
    conn = sqlite3.connect(database_path)
    with conn:
        cur = conn.cursor()
        cur.execute(sql)
        return cur.fetchall()


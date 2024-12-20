import pandas as pd
import sqlite3

# data = pd.read_csv("csv/br/crimes_violentos_2012.csv", sep=";")

con = sqlite3.Connection("db/main.db")
cur = con.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS crimes(INT registros, VARCHAR(50), municipio VARCHAR(50), cod_municipio VARCHAR(50) ano INT, risp INT, rmbh VARCHAR(10))")






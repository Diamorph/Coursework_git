import psycopg2
import random
import pandas as pd

def connect_db():
    try:
        conn = psycopg2.connect("dbname='Git' user='postgres' host='localhost' password='Vlad1309'")
        return conn
    except:
        print("I am unable to connect to the database")


def read_data():
    df = pd.read_csv('user-languages.csv', escapechar='`', low_memory=True)
    # print(df)
    # # print(df.loc[1,'state'])
    # # print(df.loc[1, 'state_abbreviation'])
    conn = connect_db()
    cursor = conn.cursor()
    for i in range(0,len(df)-1):
        try:
            user_id = df.loc[i, 'user_id']
            assembly = df.loc[i, 'assembly']
            c = df.loc[i, 'c']
            c1 = df.loc[i, 'c++']
            c2 = df.loc[i, 'c#']
            html = df.loc[i, 'html']
            css = df.loc[i, 'css']
            javascript = df.loc[i, 'javascript']
            php = df.loc[i, 'php']
            python = df.loc[i, 'python']
            angular2 = df.loc[i, 'angular2']
            vue = df.loc[i, 'vue']
            java = df.loc[i, 'java']
            scala = df.loc[i, 'scala']
            print(user_id, assembly, c, c1, c2, html, css, javascript, php, python, angular2, vue, java, scala)
            cursor.execute(
                'INSERT INTO public.git(user_id, assembly, c, c_plus_plus, c_sharp, html, css, javascript, php, python, angular2, vue, java, scala) '
                'VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',
                (user_id, assembly, c, c1, c2, html, css, javascript, php, python, angular2, vue, java, scala))
            conn.commit()
        except ValueError:
             continue


#read_data()
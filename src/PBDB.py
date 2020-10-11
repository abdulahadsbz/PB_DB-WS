import sqlite3

conn = sqlite3.connect('PBDB.db')
c = conn.cursor()


def insert_data(draw):
    '''
    inserts the tuple obtained by the get_data() function
    in PBWS
    '''
    c.executemany("INSERT INTO PBDB VALUES (?,?,?,?,?,?)", draw)
    conn.commit()


def close():
    c.close()


if __name__ == '__main__':
    '''
    creates PBDB.db on inital execution
    '''
    c.execute('''
              CREATE TABLE PBDB
              (PrizeBondNumber INT, PrizeBondRank TINYINT,
               PrizeBondValue SMALLINT,DrawNumber TINYINT,
               DrawDate SMALLDATETIME, DrawLocation CHAR)
              ''')
    c.close()

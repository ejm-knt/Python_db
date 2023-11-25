import pymysql.cursors

#! db接続関数の作成
def connect():
    connection = pymysql.connect(
        host = "localhost",
        user = "root",
        password = "root",
        database = "pybase_db_20230719am",
        cursorclass = pymysql.cursors.DictCursor
    )
    return connection

#! SELECT文でレコード全件取得
#? DB閉じなければならないので、with使ってブロック抜けたら自動で閉じる。上2行は定型文
def find_all():
    result = None
    with connect() as con:
        with con.cursor() as cursor:
            sql = "SELECT * FROM ranking" #* SQL文を文字列で用意
            cursor.execute(sql)
            result = cursor.fetchall()
    return result

# print(find_all()) #* デバック用

#! db追加用関数
def insert_one(user):
    with connect() as con:
        with con.cursor() as cursor:
            sql = "INSERT INTO ranking(name, score) VALUES(%s, %s)" #* %sで内容を仮置き
            cursor.execute(sql, (user["user"], user["score"]))
        con.commit() #* 変更がある場合はCommitする
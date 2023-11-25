import dao

# #! 入れたいデータの定義(テスト)
# user = {"name":"竹島", "score":9999999}
# dao.insert_one(user)

result = dao.find_all()
print(result[0]["name"])
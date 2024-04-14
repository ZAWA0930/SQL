from app import db, User

# User追加
user3 = User("test_user3@test.com", "Test User", "333")
db.session.add(user3)
db.session.commit()

# 全レコード取得
all_users = User.query.all()
print(all_users)

# ID指定 レコード取得
userid_1 = User.query.get(1)  # id1のユーザーを取得
print(userid_1.username)

# フィルタ レコードの取得
username_user2 = User.query.filter_by(username="Test User2")  # TestUser2のユーザーのみ取得
print(username_user2.all())

# レコードの更新
userid_1 = User.query.get(1)  # id1のユーザー取得
userid_1.username = "Test UserA"  # ユーザーネーム変更、修正: userid_1=username ="Test UserA" -> userid_1.username = "Test UserA"
db.session.commit()  # 修正: db.session.add(userid_1) を削除

# レコードの削除
userid_2 = User.query.get(2)
db.session.delete(userid_2)
db.session.commit()

# 全レコードの取得
all_users = User.query.all()
print(all_users)


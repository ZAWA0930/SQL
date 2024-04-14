from app import db,User


db.create_all()

#ユーザー登録情報
user1 = User("test_user1@test.com", "Test User1", "111")
user2 = User("test_user2@test.com", "Test User2", "222")

# #ユーザー登録
# db.session.add(user1)
# db.session.add(user1)

db.session.add_all([user1, user2])

db.session.commit()
print(user1.id)
print(user2.id)


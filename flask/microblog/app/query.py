#!flask/bin python3
# -*- coding: utf-8 -*-
# @Date    : 2016-03-21 23:11:47
# @Author  : Bluethon (j5088794@gmail.com)
# @Link    : http://github.com/bluethon

from app import db, models

# 一种查询
users = models.User.query.all()
print(users)
# [<User u'john'>, <User u'susan'>]
for u in users:
    print(u.id, u.nickname)

# # 添加用户
# u = models.User(nickname='john', email='john@email.com')
# db.session.add(u)
# db.session.commit()

# # 一种查询
# users = models.User.query.all()
# print(users
# # [<User u'john'>, <User u'susan'>]
# for u in users:
#     print(u.id, u.nickname

# # 另一种查询
# u = models.User.query.get(1)
# print(u

# # get all posts from a user
# u = models.User.query.get(1)
# print(u
# # <User u'john'>
# posts = u.posts.all()
# print(posts
# # [<Post u'my first post!'>]

# # obtain author of each post
# for p in posts:
#     print(p.id, p.author.nickname, p.body)
# # 1 john my first post!

# # a user that has no posts
# u = models.User.query.get(2)
# print(u
# # <User u'susan'>
# print(u.posts.all()
# []

# # get all users in reverse alphabetical order
# print(models.User.query.order_by('nickname desc').all()
# # [<User u'susan'>, <User u'john'>]


# # 清理
# users = models.User.query.all()
# for u in users:
#     db.session.delete(u)

# posts = models.Post.query.all()
# for p in posts:
#     db.session.delete(p)

# db.session.commit()

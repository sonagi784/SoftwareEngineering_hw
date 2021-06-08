from diary import db
from diary.models import User, Post

u = User(username='susan', email='susan@example.com')

print(u)
u.set_password('mypassword')
print(u)

print(u.check_password('anotherpassword'))
# 출력값 : False

print(u.check_password('mypassword'))
# 출력값 : True
from getpass import getpass
import sys

from webapp import create_app
from webapp.model import db, User

app = create_app()

with app.app_context():
    email = input('Введите ваш e-mail: ')

    if User.query.filter(User.email == email).count():
        print('Такая почта уже используется')
        sys.exit(0)

    username = input('Введите имя: ')

    if User.query.filter(User.username == username).count():
        print('Такой пользотваель уже существует')
        sys.exit(0)
    
    password1 = getpass('Введите пароль:')
    password2 = getpass('Повторите пароль:')

    if not password1 == password2:
        print('Пароли не совпадают')
        sys.exit(0)

    new_user = User(username=username, role='admin', email=email)
    new_user.set_password(password1)

    db.session.add(new_user)
    db.session.commit()
    print(f'Создан пользователь с id={new_user.id} и почтой {email}')

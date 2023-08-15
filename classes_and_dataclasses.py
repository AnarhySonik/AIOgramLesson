from dataclasses import dataclass


class old_User:
    def __init__(self, user_id, name, age, email):
        self.user_id = user_id
        self.name = name
        self.age = age
        self.email = email


def get_user_info(user: old_User) -> str:
    return f'Возраст пользователя {user.name} - {user.age}, ' \
           f'а email - {user.email}'


user_1: old_User = old_User(42, 'Vasiliy', 23, 'vasya_pupkin@pochta.ru')
print(get_user_info(user_1))


@dataclass
class User:
    user_id: int
    name: str
    age: int
    email: str


def get_user_info_two(user: User) -> str:
    return f'Возраст пользователя {user.name} - {user.age}, ' \
           f'а email - {user.email}'


user_2: User = User(42, 'Vasiliy', 23, 'vasya_pupkin@pochta.ru')
print(get_user_info_two(user_2))


@dataclass
class DatabaseConfig:
    db_host: str
    db_user: str
    db_password: str
    database: str


@dataclass
class TgBot:
    token: str
    admin_ids: list[int]


@dataclass
class Config:
    tg_bot: TgBot
    db: DatabaseConfig


BOT_TOKEN = 'askdjh'
ADMIN_IDS = [1234, 1235]
DB_HOST = 'url.ru'
DB_USER = 'User'
DB_PASSWORD = 'password123'
DATABASE = 'DataBase'

db = DatabaseConfig(db_host=DB_HOST, db_user=DB_USER, db_password=DB_PASSWORD, database=DATABASE)
tg_bot = TgBot(token=BOT_TOKEN, admin_ids=ADMIN_IDS)
config = Config(tg_bot, db)

token = config.tg_bot.token
db_passw = config.db.db_password

print(token)
print(db_passw)


def get_string(string: str, number: int) -> str:
    return string * number


print(get_string.__annotations__)
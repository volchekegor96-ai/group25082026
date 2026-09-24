from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

raw_password = "mypassword123"

hashed_password = pwd_context.hash(raw_password)
print(f"Початковий пароль: {raw_password}")
print(f"Хешований пароль:  {hashed_password}\n")

is_correct = pwd_context.verify(raw_password, hashed_password)
print(f"Перевірка з правильним паролем: {is_correct}")

is_wrong = pwd_context.verify("WrongPassword", hashed_password)
print(f"Перевірка з неправильним паролем: {is_wrong}")

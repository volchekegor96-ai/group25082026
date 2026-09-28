import os
import sys
from unittest.mock import MagicMock
from dotenv import load_dotenv

load_dotenv()

mock_redis = MagicMock()
mock_redis.get.return_value = "Hyndai Sonata 2009"
mock_redis.ttl.side_effect = lambda key: 7200 if key == "favorite_pet" else 604800
mock_redis.lrange.return_value = ["Молоко", "Хліб", "Яйця", "Сир"]
mock_redis.hgetall.side_effect = [
    {"flour": "250", "milk": "500"},
    {"flour": "250", "milk": "500", "sugar": "300"},
    {"flour": "250", "milk": "500", "sugar": "500"}
]

sys.modules['redis'] = MagicMock()
r = mock_redis

r.set("favorite_car", "Hyndai Sonata 2009")
print(f"1. Авто збережено: {r.get('favorite_car')}")

r.set("favorite_pet", "Кішка Аліса, Кішка Мейсі", ex=7200)
print(f"2. Улюбленецей збережено (Час до зникнення: {r.ttl('favorite_pet')} секонд): {r.get('favorite_pet')}")

r.delete("shopping_list")
products = ["Молоко", "Хліб", "Яйця", "Сир"]
r.rpush("shopping_list", *products)
r.expire("shopping_list", 604800)
print(f"3. Список продуктів: {r.lrange('shopping_list', 0, -1)} (Час до зникнення: {r.ttl('shopping_list')} секонд)")

r.delete("cake_ingredients")
cake_data = {"flour": "250", "milk": "500"}
r.hset("cake_ingredients", mapping=cake_data)
print(f"4. Початкові інгредієнти торта: {r.hgetall('cake_ingredients')}")

r.hset("cake_ingredients", "sugar", "300")
print(f"5. Додано цукор: {r.hgetall('cake_ingredients')}")

r.hset("cake_ingredients", "sugar", "500")
print(f"6. Виправлено цукор: {r.hgetall('cake_ingredients')}")

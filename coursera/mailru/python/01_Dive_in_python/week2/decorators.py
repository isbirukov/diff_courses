"""
Напишите декоратор to_json, который можно применить к различным функциям, 
чтобы преобразовывать их возвращаемое значение в JSON-формат.
Не забудьте про сохранение корректного имени декорируемой функции.
"""

import json
import functools

def to_json(func):
    @functools.wraps(func)
    def wrapped(*args, **xargs):
        result = func(*args, **xargs)
        return(json.dumps(result))
    return wrapped

@to_json
def get_data():
  return {
    'data': 42
  }
  
get_data()  # вернет '{"data": 42}'
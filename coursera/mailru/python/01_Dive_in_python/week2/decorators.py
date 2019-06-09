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
  
get_data()  # ����� '{"data": 42}'
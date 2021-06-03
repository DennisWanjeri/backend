#!/usr/bin/env python3
"""redis cache module"""
import redis
from redis import Redis
from uuid import uuid4
from typing import Union, Optional, Callable
from functools import wraps

def count_calls(method: Callable) -> Callable:
    """counting decorator for how many times a function is called"""
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """wrapper for decorator functionality"""
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper

def call_history(method: Callable) -> Callable:
    """decorator to store the history of inputs and outputs for a particular function"""

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """wrapper for decorator functionality"""
        input = str(args)
        self._redis.rpush(method.__qualname__ + ":inputs", input)

        output = str(method(self, *args, **kwargs))
        self._redis.rpush(method.__qualname__ + ":outputs", output)

        return output

    return wrapper

def replay(fn: Callable):
    """Display the history of calls of a particular function"""
    r = redis.Redis()
    f_name = fn.__qualname__
    n_calls = r.get(f_name)
    try:
        n_calls = n_calls.decode('utf-8')
    except Exception:
        n_calls = 0
    print("{} was called {} times:".format(f_name, n_calls))
    ins = r.lrange(f_name + ":inputs", 0, -1)
    outs = r.lrange(f_name + ":outputs", 0, -1)

    for i, o in zip(ins, outs):
        try:
            i = i.decode('utf-8')
        except Exception:
            i = ""
        try:
            o = o.decode('utf-8')
        except Exception:
            o = ""
        print("{}(*{}) -> {}".format(f_name, i, o))
        
class Cache:
    """
    class Cache
    """
    def __init__(self):
        """
        constructor
        """
        self._redis = Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
       """
       stores input data in Redis using a randomly generated key and returns the key
       """
       random_key = str(uuid4())
       self._redis.set(random_key, data)
       return random_key
    
    def get(self, key:str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """reads from Redis and recovers original datatype"""
        value = self._redis.get(key)
        if fn:
              value = fn(value)
        return value

    def get_str(self, key: str) -> str:
        """parameterizes a value to str"""
        value = self._redis.get(key)
        return value.decode("utf-8")

    def get_int(self, key: str) -> int:
        """
        parameterizes a value to int
        """
        value = self._redis.get(key)
        try:
              value = int(value.decode("utf-8"))
        except Exception:
              value = 0
        return value

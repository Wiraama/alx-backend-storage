#!/usr/bin/env python3
""" ... """
from functools import wraps
import redis
import uuid
from typing import Union, Callable, Optional


def count_calls(method: Callable) -> Callable:
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        key = method.__qualname__
        self.__redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


class Cache:
    """ class Cache """
    def __init__(self):
        """ initializing cache class """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        data = self._redis.get(key)
        if data is None:
            return None

        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> Optional[str]:
        return self.get(key, fn=lambda x: x.decode('utf-8'))


    def get_int(self, key: str) -> Optional[int]:
        return self.get(key, fn=int)


#!/usr/bin/env python3
from exercise import replay
from exercise import Cache

cache = Cache()
cache.store("foo")
cache.store("bar")
cache.store(42)
replay(cache.store)

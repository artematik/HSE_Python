"""
leetcode.com/problem-list/hash-table/
url: https://leetcode.com/problems/lru-cache/
"""


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> Optional[Any]:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: Any) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)

    def print_cache(self) -> None:
        print("Current cache contents:")
        for key, value in reversed(self.cache.items()):
            print(f"{key}: {value}")

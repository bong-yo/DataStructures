class HashTable:
    def __init__(self, size: int = 10, max_load: float = 0.4):
        self.table = [None] * size
        self.size = size
        self.used_space = 0
        self.max_load = max_load

    def insert(self, key: str, value) -> None:
        i = self.hashfunc(key)
        # Check for collisions.
        if self.table[i] is None:
            self.table[i] = [(key, value)]
        else:
            for j in range(self.table[i]):
                if self.table[i][j][0] == key:
                    self.table[i][j][1] = value
                    break
            self.table[i].append((key, value))
        self.used_space += 1
        self.table_load_check()

    def get(self, key: str, default=None) -> str:
        i = self.hashfunc(key)
        if self.table[i] is not None:
            for k, v in self.table[i]:
                if key == k:
                    return v
        return default

    def hashfunc(self, s: str) -> int:
        sumx = 0
        for x in s:
            sumx += abs(ord(x))
        return sumx % self.size

    def table_load_check(self):
        if self.used_space / self.size > self.max_load:
            self.resize

    def resize(self):
        self.size = 2 * self.size
        self.table_old = self.table.copy()
        self.table = [None] * self.size
        # Copy the old values into the new resized table.
        for kv_pair in self.table_old:
            if kv_pair is not None:
                k, v = kv_pair
                self.insert(k, v)


if __name__ == "__main__":
    ht = HashTable(size=1000, max_load=0.7)
    ht.insert('lala', 4)
    ht.insert('upa', 7)
    print(ht.get('hsf'))
    print(ht.get('upa'))

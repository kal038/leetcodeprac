class MyHashMap:

    def __init__(self):
        self.map = [[] for _ in range(100000)]
        

    def put(self, key: int, value: int) -> None:
        #hasing function is going to be the modulo approach and use chain hashing
        idx = key % len(self.map)
        for i, tup in enumerate(self.map[idx]):
            if key == tup[0]:
                self.map[idx][i] = (key, value)
                return
                
        self.map[idx].append((key, value))
        return
        

    def get(self, key: int) -> int:
        idx = key % len(self.map)
        for k, val in self.map[idx]:
            if key == k:
                return val
        return -1

    def remove(self, key: int) -> None:
        print(key)
        idx = key % len(self.map)
        del_idx = 0
        print(self.map[idx])
        for i in range(len(self.map[idx])):
            print(i)
            if self.map[idx][i][0] == key:
                del_idx = i
                del self.map[idx][del_idx]
       
        #print(self.map[idx])
        return 
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
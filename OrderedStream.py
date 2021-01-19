from typing import Any, Dict, Iterable, List, Optional, Union


class OrderedStream:
    def __init__(self, n: int):
        self.n = n
        self.dct = {}
        self.track = 1

    def insert(self, id: int, value: str) -> List[str]:
        result = []
        self.dct[id] = value
        for i in range(self.track, self.n + 1):
            if i in self.dct.keys():
                result.append(self.dct[i])
                self.track = i + 1
                del self.dct[i]
            else:
                break
        return result


# Your OrderedStream object will be instantiated and called as such:
obj = OrderedStream(5)
param_1 = obj.insert(3, "ccccc")
param_2 = obj.insert(1, "aaaaa")
param_3 = obj.insert(2, "bbbbb")
param_4 = obj.insert(5, "eeeee")
param_5 = obj.insert(4, "ddddd")
# print(param_1)
# print(param_2)
# print(param_3)
# print(param_4)
print(param_5)

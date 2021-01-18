from helper import sprint
from typing import Any, Dict, Iterable, List, Optional, Union
from icecream import ic

lst1 = ["ParkingSystem", "addCar", "addCar", "addCar", "addCar"]
lst_lst = [lst1]
extralst1 = [[1, 1, 0], [1], [2], [3], [1]]
extralst_lst = [extralst1]

class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.big = big
        self.medium = medium
        self.small = small

    def addCar(self, carType: int) -> bool:
        if carType == 1:
            if self.big > 0:
                self.big -= 1
                return True
            else:
                return False
        elif carType == 2:
            if self.medium > 0:
                self.medium -= 1
                return True
            else:
                return False
        elif carType == 3:
            if self.small > 0:
                self.small -= 1
                return True
            else:
                return False


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)


ps = ParkingSystem(extralst1[0][0], extralst1[0][1], extralst1[0][2])

for i in range (1, len(extralst1)):
    print(ps.addCar(extralst1[i][0]))

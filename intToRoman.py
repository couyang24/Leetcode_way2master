class Solution:
    def intToRoman(self, num: int) -> str:
        int_roman = {1:"I", 5:"V", 10:"X", 50:"L", 100:"C", 500:"D", 1000:"M"}
        result = ""
        # for i in sorted(int_roman.keys(), reverse=True):
        #     result += int_roman[i]*(num//i)
        # return result
        for i, d in enumerate(str(num)):
            if d == '4':
                if len(str(num)) - i == 3:
                    result += "CD"
                if len(str(num)) - i == 2:
                    result += "XL"
                if len(str(num)) - i == 1:
                    result += "IV"
            elif d == '9':
                if len(str(num)) - i == 3:
                    result += "CM"
                if len(str(num)) - i == 2:
                    result += "XC"
                if len(str(num)) - i == 1:
                    result += "IX"
            else:
                if int(d)>=5:
                    if len(str(num)) - i == 3:
                        result += "D"+"C"*(int(d)-5)
                    elif len(str(num)) - i == 2:
                        result += "L"+"X"*(int(d)-5)
                    else:
                        result += "V"+"I"*(int(d)-5)
                else:
                    if len(str(num)) - i == 4:
                        result += "M"*(int(d))
                    elif len(str(num)) - i == 3:
                        result += "C"*(int(d))
                    elif len(str(num)) - i == 2:
                        result += "X"*(int(d))
                    else:
                        result += "I"*(int(d))
        return result

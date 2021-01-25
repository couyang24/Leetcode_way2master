class Solution:
    def freqAlphabets(self, s: str) -> str:
        result = ""
        for i in range(len(s)): 
            if i <= len(s)-3:
                if (s[i+1] == "#") or (s[i] == "#"):
                    pass
                elif s[i+2] != "#":
                    result += chr(int(s[i])+96)
                else:
                    result += chr(int(s[i:i+2])+96)
            elif (s[-1]=="#") or (s[i]=="#"):
                pass
            else:
                result += chr(int(s[i])+96)
        return result

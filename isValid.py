class Solution:
    def isValid(self, s: str) -> bool:
        open1id = []
        open2id = []
        open3id = []
        nopen = 0
        left_dct = {"(": open1id, "{": open2id, "[": open3id}
        right_dct = {")": open1id, "}": open2id, "]": open3id}
        for i in range(len(s)):
            if s[i] in left_dct.keys():
                nopen += 1
                left_dct[s[i]].append(nopen)

            if s[i] in right_dct.keys():
                if nopen == 0:
                    # ic()
                    return False
                else:
                    if nopen in right_dct[s[i]]:
                        # ic(nopen, open1id)
                        right_dct[s[i]].remove(nopen)
                        nopen -= 1
                    else:
                        # ic(nopen, open1id)
                        return False
        if nopen == 0:
            return True
        else:
            # ic()
            return False

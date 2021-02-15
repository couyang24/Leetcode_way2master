class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        dct = {}
        result = []
        for i in cpdomains:
            count = i.split()[0]
            lst = i.split()[1].split(".")
            while len(lst) >= 1:
                pdomain = ".".join(lst)
                if pdomain in dct.keys():
                    dct[pdomain] += int(count)
                else:
                    dct[pdomain] = int(count)
                if len(lst) > 1:
                    lst = pdomain.split(".")[1:]
                else:
                    break
        for j in dct.keys():
            item = " ".join([str(dct[j]), j])
            result.append(item)
        return result

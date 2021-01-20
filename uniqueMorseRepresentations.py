class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        lst = []
        count = 0
        cmap = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        for word in words:
            code = ""
            for l in word:
                code += cmap[ord(l)-97]
            if code not in lst:
                lst.append(code)
                count += 1
        return count

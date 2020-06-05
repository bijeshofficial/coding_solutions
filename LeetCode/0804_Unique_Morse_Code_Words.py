class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        list_1 = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        code = ''
        list_2 = []
        for i in words:
            for j in i:
                code += list_1[ord(j)-97]
            list_2.append(code)
            code = ''
        return len(set(list_2))
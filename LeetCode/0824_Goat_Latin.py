class Solution:
    def toGoatLatin(self, S: str) -> str:
        ans = ''
        list_1 = []
        S = S.split()
        vowels = 'aeiouAEIOU'
        index = 1
        for i in S:
            if i[0] in vowels:
                ans+= i + 'ma' + index*'a'
                list_1.append(ans)
                index +=1
                ans = ''
            elif i[0] not in vowels and len(i)>1:
                ans += i[1:] + i[0] + 'ma' + index*'a'
                list_1.append(ans)
                index+=1
                ans = ''
            else:
                ans += i + 'ma' + index*'a'
                list_1.append(ans)
                index +=1
                ans = ''
        return ' '.join(list_1)
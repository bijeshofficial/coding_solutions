n= input()
vowels = 'aeiouy'
ans = ''
out = ''
for i in n.lower():
    if i not in vowels:
         ans += i
for i in ans:
    out += f'.{i}'
print(out)
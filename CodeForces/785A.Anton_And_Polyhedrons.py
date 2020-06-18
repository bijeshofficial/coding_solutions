def func(n):
    dictionary = {
    'Tetrahedron' : 4,
    'Cube' : 6,
    'Octahedron' : 8,
    'Dodecahedron' : 12,
    'Icosahedron' : 20
    }
    sum = 0
    for i in range(n):
        k = list(map(str,input().split()))
        sum += dictionary[k[0]]
    print(sum)
n = int(input())
func(n)
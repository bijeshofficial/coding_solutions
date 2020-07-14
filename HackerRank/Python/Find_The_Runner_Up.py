if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    new_set = set(arr)
    max_set = max(new_set)
    new_set.remove(max_set)
    print(max(new_set))

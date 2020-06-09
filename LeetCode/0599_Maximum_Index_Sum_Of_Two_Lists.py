class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        dict_list1 = {}
        dict_2 = {}
        emp = []
        for i, v in enumerate(list1):
            if v not in dict_list1:
                dict_list1[v] = i
        for i,v in enumerate(list2):
            if v in dict_list1.keys():
                dict_list1[v] += i
        a = set(list1).intersection(set(list2))
        print(dict_list1, a)
        for k,v in dict_list1.items():
            if k in a:
                dict_2[k] = v
        print(dict_2)
        for k,v in dict_2.items():
            if dict_2[k] == min(dict_2.values()):
                emp.append(k)
        return emp
class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        empty_dict = {}
        empty_dict[keysPressed[0]] = releaseTimes[0]
        for i in range(1, len(keysPressed)):
            if keysPressed[i] not in empty_dict:
                empty_dict[keysPressed[i]] = releaseTimes[i] - \
                    releaseTimes[i-1]
                continue
            if (releaseTimes[i] - releaseTimes[i-1]) > empty_dict[keysPressed[i]]:
                empty_dict[keysPressed[i]] = releaseTimes[i] - \
                    releaseTimes[i-1]
        max_value = max(empty_dict.values())
        max_keys = [k for k, v in empty_dict.items() if v == max_value]
        if len(max_keys) == 1:
            return max_keys[0]
        answer = ''
        for i in range(len(max_keys) - 1):
            if ord(max_keys[i]) > ord(max_keys[i+1]):
                answer = max_keys[i]
            else:
                answer = max_keys[i+1]
        return answer

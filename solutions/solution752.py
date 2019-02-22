from queue import Queue


class Solution:
    def openLock(self, deadends: 'List[str]', target: 'str') -> 'int':
        status = {"0000": 0}
        for deadend in deadends:
            status[deadend] = -1
        if status["0000"] == -1:
            return -1
        q = Queue()
        q.put("0000")
        while not q.empty():
            current = q.get()
            if current == target:
                return status[current]
            for i in range(4):
                for d in [-1, 1]:
                    c = current[:i] + str((int(current[i]) + d + 10) % 10) + current[i + 1:]
                    if c not in status:
                        status[c] = status[current] + 1
                        q.put(c)
        return -1


if __name__ == "__main__":
    print(Solution().openLock(["0201", "0101", "0102", "1212", "2002"], "0202"))
    print(Solution().openLock(["8888"], "0009"))
    print(Solution().openLock(["8887", "8889", "8878", "8898", "8788", "8988", "7888", "9888"], "8888"))
    print(Solution().openLock(["0000"], "8888"))

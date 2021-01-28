class RecentCounter:

    def __init__(self):
        self.record = []

    def ping(self, t: int) -> int:
        self.record.append(t)
        record = self.record.copy()
        count = 0
        rm_list = []
        for i in record:
            if i in range(t-3000, t+1):
                count += 1
            else:
                self.record.remove(i)
        return count

class RabinKarp:
    def __init__(self, pattern, text):
        self.pattern = pattern
        self.text = text
        self.prime = 1000000007
        self.x = 263
        self.patternHash = self.polyHash(pattern)
        self.textHashes = self.precomputeHashes()

    def polyHash(self, s):
        h = 0
        for i in reversed(s):
            h = (h * self.x + ord(i)) % self.prime
        return h

    def precomputeHashes(self):
        t = self.text
        p = self.pattern
        t_len = len(t)
        p_len = len(p)
        h = [0] * (t_len - p_len + 1)
        s = t[t_len - p_len:]
        h[t_len - p_len] = self.polyHash(s)
        y = 1
        for i in range(p_len):
            y = (y * self.x) % self.prime
        for i in range(t_len - p_len - 1, -1, -1):
            h[i] = (self.x * h[i + 1] + ord(t[i]) - y * ord(t[i + p_len])) % self.prime
        return h

    def getOccurrences(self):
        occurrences = []
        p = self.pattern
        t = self.text
        p_len = len(p)
        t_len = len(t)
        for i in range(t_len - p_len + 1):
            if self.patternHash != self.textHashes[i]:
                continue
            if self.pattern == t[i:i + p_len]:
                occurrences.append(i)
        return occurrences

    def solve(self):
        occurrences = self.getOccurrences()
        return occurrences

def main():
    pattern = input()
    text = input()
    rk = RabinKarp(pattern, text)
    print(" ".join(map(str, rk.solve())))

if __name__ == '__main__':
    main()

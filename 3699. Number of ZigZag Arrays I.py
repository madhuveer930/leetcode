class Solution:
    MOD = 10**9 + 7

    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        m = r - l + 1

        up = [0] * (m + 1)
        down = [0] * (m + 1)

        for v in range(1, m + 1):
            up[v] = v - 1
            down[v] = m - v

        pref = [0] * (m + 1)
        suff = [0] * (m + 2)
        new_up = [0] * (m + 1)
        new_down = [0] * (m + 1)

        MOD = self.MOD

        for _ in range(3, n + 1):

            cur = 0
            for i in range(1, m + 1):
                cur += down[i]
                pref[i] = cur % MOD

            cur = 0
            for i in range(m, 0, -1):
                cur += up[i]
                suff[i] = cur % MOD

            for x in range(1, m + 1):
                new_up[x] = pref[x - 1]
                new_down[x] = suff[x + 1]

            up, new_up = new_up, up
            down, new_down = new_down, down

        return (sum(up[1:]) + sum(down[1:])) % MOD

# algo_solutions.py

from typing import List

# ---- UVA 100 ----
def collatz_len(n: int, memo={1: 1}):
    if n not in memo:
        memo[n] = 1 + (collatz_len(3 * n + 1, memo) if n % 2 else collatz_len(n // 2, memo))
    return memo[n]

def uva_100(i: int, j: int) -> int:
    if i > j:
        i, j = j, i
    return max(collatz_len(n) for n in range(i, j + 1))


# ---- UVA 11150 ----
def uva_11150(n: int) -> int:
    total = empty = n
    while empty >= 3:
        exchange = empty // 3
        total += exchange
        empty = exchange + (empty % 3)
    return total


# ---- UVA 10327 ----
def count_inversions(arr):
    if len(arr) <= 1:
        return arr, 0
    mid = len(arr) // 2
    left, inv_l = count_inversions(arr[:mid])
    right, inv_r = count_inversions(arr[mid:])
    merged = []
    i = j = 0
    inv_split = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i]); i += 1
        else:
            merged.append(right[j]); j += 1
            inv_split += len(left) - i
    merged.extend(left[i:]); merged.extend(right[j:])
    return merged, inv_l + inv_r + inv_split

def uva_10327(nums):
    _, inv = count_inversions(nums)
    return inv


# ---- UVA 11586 ----
def uva_11586(segments):
    m = f = 0
    for seg in segments:
        m += seg.count('M')
        f += seg.count('F')
    return "LOOP" if m == f and len(segments) > 1 else "NO LOOP"


# ---- LC 5 ----
def longest_palindrome(s: str) -> str:
    n = len(s)
    if n < 2:
        return s
    def expand(l, r):
        while l >= 0 and r < n and s[l] == s[r]:
            l -= 1; r += 1
        return l + 1, r - 1
    start = end = 0
    for i in range(n):
        a1, b1 = expand(i, i)
        a2, b2 = expand(i, i + 1)
        if b1 - a1 > end - start: start, end = a1, b1
        if b2 - a2 > end - start: start, end = a2, b2
    return s[start:end + 1]


# ---- LC 17 ----
phone_map = {
    '2': "abc", '3': "def", '4': "ghi", '5': "jkl",
    '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"
}

def letter_combinations(digits: str) -> List[str]:
    if not digits:
        return []
    res = []
    def dfs(idx, path):
        if idx == len(digits):
            res.append("".join(path)); return
        for ch in phone_map[digits[idx]]:
            path.append(ch)
            dfs(idx + 1, path)
            path.pop()
    dfs(0, [])
    return res


# ---- Demo ----
if __name__ == "__main__":
    print("UVA100(1,10) =", uva_100(1,10))         # 20
    print("UVA11150(9) =", uva_11150(9))         # 15
    print("UVA10327([2,3,1]) =", uva_10327([2,3,1]))  # 2
    print("UVA11586(['FM','FF','MF','MM']) =", uva_11586(['FM','FF','MF','MM']))  # LOOP
    print("LC5('babad') =", longest_palindrome("babad"))
    print("LC17('23') =", letter_combinations("23"))

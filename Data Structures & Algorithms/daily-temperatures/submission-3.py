class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        out = [0] * len(temperatures)
        stack = []
        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                prev_index, prev_temp = stack.pop()
                out[prev_index] = i - prev_index
            stack.append((i, temp))
        return out
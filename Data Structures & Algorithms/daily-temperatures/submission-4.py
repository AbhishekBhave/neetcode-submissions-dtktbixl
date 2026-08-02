class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        out = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][1]:
                prev_index, prev_temp = stack.pop()
                diff = i - prev_index
                out[prev_index] = diff
            stack.append((i, t))
        return out
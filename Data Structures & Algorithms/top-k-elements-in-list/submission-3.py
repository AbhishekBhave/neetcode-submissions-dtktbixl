class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_map = {}
        for num in nums:
            count_map[num] = count_map.get(num, 0) + 1
            
        # 2. Sort the numbers (the keys) based on their frequency (the values) in descending order
        # We use a lambda function to tell python to sort by the dictionary values
        sorted_nums = sorted(count_map.keys(), key=lambda x: count_map[x], reverse=True)
        
        # 3. Pull the first k elements from that list
        return sorted_nums[:k]
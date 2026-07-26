class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        numsFrequencyDict = {}
        numsFirstIndexDict = {}
        numsLastIndexDict = {}
        resultDegree = float('inf')

        for index, number in enumerate(nums):
            if number not in numsFrequencyDict:
                numsFirstIndexDict[number] = index
            numsLastIndexDict[number] = index
            numsFrequencyDict[number] = numsFrequencyDict.get(number, 0) + 1

        degree = max(numsFrequencyDict.values())

        for number, frequency in numsFrequencyDict.items():
            if frequency == degree:
                resultDegree = min(resultDegree, numsLastIndexDict[number] - numsFirstIndexDict[number] + 1)
        
        return resultDegree
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Brute Force solution for the 3Sum problem.

        Note: This approach may cause a Time Limit Exceeded (TLE) error for large inputs while submitting.
        """

        # Step 1: Create an empty array to store the result
        result = []

        # Step 2: Triple nested loop to check all triplets
        n = len(nums)
        for i in range(n):  # i loop from 0 to n-1
            for j in range(i + 1, n):  # j should be greater than i
                for k in range(j + 1, n):  # k should be greater than j
                    # Step 3: Check if sum is zero
                    if nums[i] + nums[j] + nums[k] == 0:
                        # Step 4: Sort the triplet
                        triplet = sorted([nums[i], nums[j], nums[k]])

                        # Step 5: Check if triplet is already present in result
                        if triplet not in result:
                            # Step 6: Push triplet to result
                            result.append(triplet)

        return result


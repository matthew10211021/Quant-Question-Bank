def Boyer_Moore_Voting(nums):
    # edge cases, note that we are guarenteed to have a majority
    if len(nums) == 1 or len(nums) == 2: return nums[0]

    cur = nums[0]
    cur_count = 1

    for num in nums:
        if num == cur: cur_count += 1
        else: cur_count -= 1

        if cur_count == 0:
            cur = num
            cur_count = 1

    return cur
        

if __name__ == "__main__":
    arr = [7, 3, 7, 3, 7, 5, 45, 2, 7, 2, 6, 7, 7, 7, 7, 7, 3]
    num = Boyer_Moore_Voting(arr)
    print(f"The majority element is {num}")
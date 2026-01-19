Conversation opened. 1 unread message.

Skip to content
Using Gmail with screen readers
1 of 425
(no subject)
Inbox

Afa Fahma
1:30 PM (0 minutes ago)
to me

# # Question 1: Reverse Digits of Each Element in an Array
# # You are given an array of positive integers. Your task is to reverse the digits of each element in
# # the array without the use of built-in functions and return a new array with these reversed
# # numbers.(Use any language.)
# # Input:
#  array: [12, 23, 54]
arr = [12, 23, 54]
reversed_arr = []

for num in arr:
    rev = 0
    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num = num // 10
    reversed_arr.append(rev)

print(reversed_arr)

# # Question 2: Butterfly Pattern
# # Write a program to print the Butterfly Pattern like given below:

n = 4

# Upper part
for i in range(1, n + 1):
    print("*" * i + " " * (2 * (n - i)) + "*" * i)

# Lower part
for i in range(n, 0, -1):
    print("*" * i + " " * (2 * (n - i)) + "*" * i)


# # 1. Write a program bn3that takes a list of integers and a target sum. Return all unique pairs of
# # numbers from the list that add up to the target.
# # 📥 Input Example:
# # nums = [2, 4, 3, 5, 6, -1]
# # target = 5
# # 📤 Expected Output:
# # [(2, 3), (6, -1)]
# # Order doesn’t matter. Pairs (3, 2) and (2, 3) are considered the same.
# # 🧪 Test Cases:
# # Input: nums = [1, 2, 3, 4, 5], target = 6
# # Output: [(1, 5), (2, 4)]
# # Input: nums = [0, -1, 2, -3, 1], target = -2
# # Output: [(-3, 1)]
# # Input: nums = [3, 3, 3, 3], target = 6
# # Output: [(3, 3)]

def find_pairs(nums, target):
    seen = set()
    pairs = set()

    for num in nums:
        req = target - num
        if req in seen:
            pair = tuple(sorted((num, req)))
            pairs.add(pair)
        seen.add(num)

    return list(pairs)

print(find_pairs([2, 4, 3, 5, 6, -1], 5))
print(find_pairs([1, 2, 3, 4, 5], 6))
print(find_pairs([0, -1, 2, -3, 1], -2))
print(find_pairs([3, 3, 3, 3], 6))


# # 2. A Happy Number is a number defined by the following process:
# # 1. Starting with any positive integer,
# # 2. Replace the number by the sum of the squares of its digits,
# # 3. Repeat the process until the number equals 1 (where it will stay), or it loops endlessly
# # in a cycle that does not include 1.
# # If it ends in 1, it is a Happy Number
# # 📥 Input Example:
# # 19
# # 📤 Expected Output:
# # True
# # Explanation:
# # ● 1² + 9² = 82
# # ● 8² + 2² = 68
# # ● 6² + 8² = 100
# # ● 1² + 0² + 0² = 1 ✅
# # 🧪 Test Cases:
# # Input: 19 → Output: True
# # Input: 2 → Output: False
# # Input: 7 → Output: True
# # Input: 20 → Output: False

def is_happy(n):
    seen = set()

    while n != 1:
        if n in seen:
            return False
        seen.add(n)

        sum_sq = 0
        while n > 0:
            digit = n % 10
            sum_sq += digit * digit
            n //= 10

        n = sum_sq

    return True
print(is_happy(19))  
print(is_happy(2))   
print(is_happy(7))   
print(is_happy(20)) 



# 1.You are given two strings: haystack and needle. Your task is to determine the first position
# where the substring needle appears in the string haystack. If the substring needle does not exist
# in haystack, you should return -1.
# Example Inputs and Outputs:
# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0(since "sad" first occurs at index 0)
# Input: haystack = "leetcode", needle = "leeto"
# Output: -1(since "leeto" does not exist in "leetcode")
# Input: haystack = "hello" , needle = "ll"
# Output:?

def a(haystack,needle):
  if needle in haystack:
     return haystack.find(needle)
     

  else:
    return -1
  
print(a("hello","li"))
print(a("world","orl"))

# 2. Given an integer n representing the number of pairs of parentheses, write a function to
# generate all possible combinations of well-formed parentheses.
# A combination is considered well-formed if:
# ● Every opening parenthesis ( has a corresponding closing parenthesis ).
# ● Parentheses are properly nested.
# Input:
# An integer n (number of pairs of parentheses)
# Output:
# A list of strings containing all valid combinations of well-formed parentheses.
# Examples:
# Input:n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# What will be the output
# Input:n = 5
# Output:?
def generate_parentheses(n):
    result = []

    def make(s, open_b, close_b):
        if open_b == n and close_b == n:
            result.append(s)
            return

        if open_b < n:
            make(s + "(", open_b + 1, close_b)

        if close_b < open_b:
            make(s + ")", open_b, close_b + 1)

    make("", 0, 0)
    return result


n = int(input("Enter number of pairs: "))
print(generate_parentheses(n))

    
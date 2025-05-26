class Solution:
    def __init__(self):
        self.stack = []
        self.queue = []

    def pushCharacter(self, ch):
        self.stack.append(ch)

    def enqueueCharacter(self, ch):
        self.queue.append(ch)

    def popCharacter(self):
        return self.stack.pop()

    def dequeueCharacter(self):
        return self.queue.pop(0)

# ✅ Make sure to run this in a Python environment that supports input.
s = input("Enter a word: ").strip()
obj = Solution()

# Enqueue and push all characters
for ch in s:
    obj.pushCharacter(ch)
    obj.enqueueCharacter(ch)

# Check for palindrome
is_palindrome = True
for i in range(len(s) // 2):
    if obj.popCharacter() != obj.dequeueCharacter():
        is_palindrome = False
        break

# Print the result
if is_palindrome:
    print(f"The word, {s}, is a palindrome.")
else:
    print(f"The word, {s}, is not a palindrome.")

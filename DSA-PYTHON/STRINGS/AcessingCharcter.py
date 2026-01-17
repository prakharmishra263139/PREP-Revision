# # Class containing the method to access characters
# class Solution:
#     # Function to print each character of a string
#     def accessCharacters(self, s):
#         # Loop through each index
#         for i in range(len(s)):
#             # Print the character at index i
#             print(s[i])

# # Driver code
# if __name__ == "__main__":
#     # Create object of Solution class
#     obj = Solution()
#     # Input string
#     s = "Hello"
#     # Call the function
#     obj.accessCharacters(s)

class Solution:
    def access_char(self, s):
        for i in range(len(s)):
            print(s[i])

if __name__ == "__main__":
    obj = Solution()
    s = "Hello"
    obj.access_char(s)  


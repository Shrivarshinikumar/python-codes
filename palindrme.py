def is_palindrome(s):
    s=s.lower().replace(" ","")
    return s==s[::-1]
string = input("enter a string")
print(f"Is '{string}' a palindrome?", is_palindrome(string))
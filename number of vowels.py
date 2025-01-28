def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels )

string = "beautiful world"
print(f"number of vowels in '{string}':",count_vowels(string))
import re

def contains_pattern(pattern: str, text: str) -> bool:
    return re.search(pattern, text) is not None #Interesting when I didn't add the Not None then that shi was giving me none for first one


print(contains_pattern("dog", "The cat is black."))  
print(contains_pattern("cat", "The cat is black."))  

def has_three_digits(text: str) -> bool:
    return re.search(r"\d{3}", text) is not None

print(has_three_digits("abc123def"))  
print(has_three_digits("ab12c"))      

print(re.findall(r"\b\w{4}\b", "The fast blue crab swims"))  

def extract_four_digit_numbers(text: str) -> list:
    return re.findall(r"\b\d{4}\b", text)

print(extract_four_digit_numbers('Simon has 1234 thousand dollars in his bank account, and his code is 0023'))


text = "Order #1234: $45.67"
pattern = r"Order #(\d+): \$(\d+\.\d{2})"


match = re.search(pattern, text)
print(match.groups())  # Output: ('1234', '45.67')

text = "That movie was fucking ass and retarded"

pattern = r"(fucking|ass|retarded)"
censored = re.sub(pattern, "*****", text)

print(censored)



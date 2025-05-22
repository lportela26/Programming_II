
#try:
   # x = 1 / 0
#except ZeroDivisionError:
    #print("You can't divide by zero gang")



try:
    x = int('dog')

except:
    print("shi don't work bro")

else:
    print('yay')

finally:
    print('gone')


def scream(text: str) -> str:
    if type(text) != str:
        raise TypeError("Text is not a string")
    return text.upper


print(scream("hello"))    
#print(scream(123))       

def is_prime(n):
    if not isinstance(n, int):
        raise TypeError("That's a string") 
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


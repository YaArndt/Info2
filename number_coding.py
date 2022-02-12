from numpy import binary_repr

def twos_comp(val: int, bits: int = 4):
    """Function to calculate the twos complement from a given  decimal number.

    Args:
        val (int): Number to be used.
        bits (int, optional): Bit length for the complement. Defaults to 4.
    """
    print(f'2-Komplement von {val}: {binary_repr(val, bits)}')

def BCD_to_decimal(s: str):
    """Returns a decimal from a given string BCD representation.

    Args:
        s (str): BCD-Code
    """
 
    length = len(s)
    check = 0
    check0 = 0
    num = 0
    sum = 0
    mul = 1
    rev = 0
     
    # Iterating through the bits backwards
    for i in range(length - 1, -1, -1):
         
        # Forming the equivalent
        # digit(0 to 9)
        # from the group of 4.
        sum += (ord(s[i]) - ord('0')) * mul
        mul *= 2
        check += 1
         
        # Reinitialize all variables
        # and compute the number
        if (check == 4 or i == 0):
            if (sum == 0 and check0 == 0):
                num = 1
                check0 = 1
                 
            else:
                 
                # Update the answer
                num = num * 10 + sum
                 
            check = 0
            sum = 0
            mul = 1
             
    # Reverse the number formed.
    while (num > 0):
        rev = rev * 10 + (num % 10)
        num //= 10
         
    if (check0 == 1):
        print(f'Dezimal aus {s}: {rev-1}')
         
    print(f'Dezimal aus {s}: {rev}')

def BCD_from_decimal(s: int) :
    """Creates a BCD representation from a given decimal.

    Args:
        s (int): Decimal number to be converted.
    """
    
    print(f"BCD aus {s}: ", end='')
 
    # Base Case
    if (s == 0) :
        print("0000")
        return
 
    # To store the reverse of n
    rev = 0
 
    # Reversing the digits
    while (s > 0) :
        rev = rev * 10 + (s % 10)
        s = s // 10
    
    # Iterate through all digits in rev
    while (rev > 0) :
 
        # Find Binary for each digit
        # using bitset
        b = str(rev % 10)
         
        # Print the Binary conversion
        # for current digit
        print("{0:04b}".format(int(b, 16)), end = " ")
 
        # Divide rev by 10 for next digit
        rev = rev // 10
    
    print("")
    
# Driver Code
if __name__ == "__main__":

    BCD_to_decimal('0001')
    
    BCD_from_decimal(0)
    
    twos_comp(-1, 4)

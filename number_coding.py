from numpy import binary_repr

def twos_comp(val: int, bits: int = 4):
    """Function to calculate the twos complement from a given  decimal number.

    Args:
        val (int): Number to be used.
        bits (int, optional): Bit length for the complement. Defaults to 4.
    """
    print(f'2-Komplement von {val}: {binary_repr(val, bits)}')    
    
def BCD_from_decimal(val: str, print_res: bool = True):
    
    val = val.replace(" ", "")
    
    final_str = ""
    
    mapping = {
        "0": "0000",
        "1": "0001",
        "2": "0010",
        "3": "0011",
        "4": "0100",
        "5": "0101",
        "6": "0110",
        "7": "0111",
        "8": "1000",
        "9": "1001"
    }
    
    for character in val:
        final_str += f"{mapping.get(character)} "
    
    if print_res: print(final_str)
    return final_str

def BCD_to_decimal(val: str, print_res: bool = True):
    
    val = val.replace(" ", "")
    
    split_string = [val[i:i+4] for i in range(0, len(val), 4)]
    
    final_str = ""
    
    mapping = {
        "0000": "0",
        "0001": "1",
        "0010": "2",
        "0011": "3",
        "0100": "4",
        "0101": "5",
        "0110": "6",
        "0111": "7",
        "1000": "8",
        "1001": "9"
    }
    
    for character in split_string:
        final_str += mapping.get(character)
    
    if print_res: print(final_str)
    return final_str

def EXC3_from_decimal(val: str, print_res: bool = True):
    
    val = val.replace(" ", "")
    
    final_str = ""
    
    mapping = {
        "0": "0011",
        "1": "0100",
        "2": "0101",
        "3": "0110",
        "4": "0111",
        "5": "1000",
        "6": "1001",
        "7": "1010",
        "8": "1011",
        "9": "1100"
    }
    
    for character in val:
        final_str += f"{mapping.get(character)} "
    
    if print_res: print(final_str)
    return final_str

def EXC3_to_decimal(val: str, print_res: bool = True):
    
    val = val.replace(" ", "")
    
    split_string = [val[i:i+4] for i in range(0, len(val), 4)]
    
    final_str = ""
    
    mapping = {
        "0011": "0",
        "0100": "1",
        "0101": "2",
        "0110": "3",
        "0111": "4",
        "1000": "5",
        "1001": "6",
        "1010": "7",
        "1011": "8",
        "1100": "9"
    }
    
    for character in split_string:
        final_str += f"{mapping.get(character)}"
    
    if print_res: print(final_str)
    return final_str

def AIKEN_from_decimal(val: str, print_res: bool = True):
    
    val = val.replace(" ", "")
    
    final_str = ""
    
    mapping = {
        "0": "0000",
        "1": "0001",
        "2": "0010",
        "3": "0011",
        "4": "0100",
        "5": "1011",
        "6": "1100",
        "7": "1101",
        "8": "1110",
        "9": "1111"
    }
    
    for character in val:
        final_str += f"{mapping.get(character)} "
    
    if print_res: print(final_str)
    return final_str

def AIKEN_to_decimal(val: str, print_res: bool = True):
    
    val = val.replace(" ", "")
    
    split_string = [val[i:i+4] for i in range(0, len(val), 4)]
    
    final_str = ""
    
    mapping = {
        "0000": "0",
        "0001": "1",
        "0010": "2",
        "0011": "3",
        "0100": "4",
        "1011": "5",
        "1100": "6",
        "1101": "7",
        "1110": "8",
        "1111": "9"
    }
    
    for character in split_string:
        final_str += f"{mapping.get(character)}"
    
    if print_res: print(final_str)
    return final_str
    
def get_valid_encoding(val: str, print_res: bool = True):
    
    val = val.replace(" ", "")
    split_string = [val[i:i+4] for i in range(0, len(val), 4)]
    
    bcd = True
    exc3 = True
    aiken = True
    
    bcd_mapping = {
        "0000": "0",
        "0001": "1",
        "0010": "2",
        "0011": "3",
        "0100": "4",
        "0101": "5",
        "0110": "6",
        "0111": "7",
        "1000": "8",
        "1001": "9"
    }
    
    exc3_mapping = {
        "0011": "0",
        "0100": "1",
        "0101": "2",
        "0110": "3",
        "0111": "4",
        "1000": "5",
        "1001": "6",
        "1010": "7",
        "1011": "8",
        "1100": "9"
    }
    
    aiken_mapping = {
        "0000": "0",
        "0001": "1",
        "0010": "2",
        "0011": "3",
        "0100": "4",
        "1011": "5",
        "1100": "6",
        "1101": "7",
        "1110": "8",
        "1111": "9"
    }
    
    for character in split_string:
        if bcd_mapping.get(character) is None:
            bcd = False
        elif exc3_mapping.get(character) is None:
            exc3 = False
        elif aiken_mapping.get(character) is None:
            aiken = False
    
    print(f"Searching for a valid encoding for:\n{val}" )
            
    if bcd: print(f"Encoded in BCD: {BCD_to_decimal(val, False)}")
    else: print("Not valid in BCD")
    
    if exc3: print(f"Encoded in Excess3: {EXC3_to_decimal(val, False)}")
    else: print("Not valid in Excess3")
    
    if aiken: print(f"Encoded in AIKEN: {AIKEN_to_decimal(val, False)}")
    else: print("Not valid in AIKEN")
    
    print("\n")

def encode_in_all(val: str): 
    
    print(f"Encoding {val}:")
    print(f"Encoded in BCD: {BCD_from_decimal(val, False)}")
    print(f"Encoded in Excess3: {EXC3_from_decimal(val, False)}")
    print(f"Encoded in AIKEN: {AIKEN_from_decimal(val, False)}")
    print("\n")
    
if __name__ == "__main__":
    
    BCD_from_decimal("89684943")
    BCD_to_decimal("10001001011010000100100101000011")
    
    EXC3_from_decimal("193")
    EXC3_to_decimal("10011100")
    
    AIKEN_from_decimal("234")
    AIKEN_to_decimal("11001111")
    
    get_valid_encoding("01110011010110100100101101100101")
    
    encode_in_all("69")
    
    twos_comp(-1, 4)

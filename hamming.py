from scipy.spatial import distance as d
from typing import *
from math import floor

def hamming(arrayA, arrayB) -> int:
    """Return the hamming distance between two arrays.

    Args:
        arrayA ([type]): Array number 1.
        arrayB ([type]): Array number 2.

    Returns:
        int: Hamming distance as an integer. 
    """
    
    # Calculate the distance and return.
    distance = d.hamming(arrayA, arrayB)
    
    # Retrun the distance.
    return int(len(arrayA) * distance)

def listed_hamming(input_array: List[str]):
    """Calculates the minimal hamming distance between all the provided strings.

    Args:
        input_array (List[str]): Array of strings to be compared against one another.
    """
    
    # Convert strings in the input into arrays of single characters.
    arrays = arrayify(input_array)
    
    # Create a distance set.
    distances = set()
    
    # Iterate throught the arrays.
    for array in arrays:
        
        # Remove the current array to minimize calculations.
        arrays.pop(arrays.index(array))
        
        # If there are any arrays left to compare to...
        if arrays != None:
            
            # Compare the current array.
            for check_array in arrays:
                
                # Add the distance to the result set.
                distances.add(hamming(array, check_array))

    # Minimize the recirded distances and calkulate ks
    hc = int(min(distances))
    notice = max({hc - 1, 0})
    correct = max({floor((hc - 1)/2), 0})
    
    # Create the result string and print it.
    result = f"h(c) = {hc}\n{notice}-Erkennbar\n{correct}-Korrigierbar"
    print(result)
    
    # Return the hamming distance for good measure...
    return hc
        
def to_array(input_string: str) -> List[str]:
    """Converts a string into an array of single characters.

    Args:
        input_string (str): String to be split up.

    Returns:
        List[str]: Array representation of the string.
    """
    
    # initialize the final array.
    final_list = []
    
    # Add every single character.
    for i in input_string:
        final_list.append(i)
    
    # Return the result.    
    return final_list

def arrayify(input_array: List[str]) -> List[List[str]]:
    """Apply the to_array function onto an array of strings.

    Args:
        input_array (List[str]): Input array.

    Returns:
        List[List[str]]: Array of converted arrays.
    """
    return [to_array(i) for i in input_array]


if __name__ == "__main__":

    listed_hamming([
        "1111000000000000",
        "0000111100000000",
        "0000000011110000",
        "0000000000001111",
        "1100110000000000",
        "0000000011001100",
        "0000110011000000",
        "1100000000001100"
    ])
from typing import *
from tkinter import Tk
import pyperclip

def addToClipBoard(text: str):
    """Function to replace a clipboard.

    Args:
        text (str): Text to be copied.
    """
    
    pyperclip.copy(text)

def num_states(number: int, start: int = 0, character: str = "s") -> List[str]:
    """This function creates a list of strings to act as states for FSMs.

    Args:
        number (int): Number of states to be created.
        start (int): Start number to be used. Defaults to 0. 
        character (str, optional): Character to be used. Defaults to "s".

    Returns:
        List[str]: A list of state strings.
    """
    
    # Create result list and initialize starting number.
    result = []
    num = start
    
    # Iterate through the range specified by the number parameter.
    for _ in range(number):
        
        # Add a new state to the list
        result.append(f"{character}{num}")
        
        # Increment the number of states
        num += 1
        
    return result

def fsm_template(states: List[str], arrows: List[str], character: str = "s") -> None:
    """This function creates a template for creating and minimizing FSMs.

    Args:
        states (List[str]): List of states to be included.
        arrows (List[str]): List of possible arrows per state.
        character (str, optional): Character to be used in the "=>" operation. Defaults to "s".
    """    
    
    # Initialize the final string
    final_str = "fsm:\n"
    
    # Iterate through the states provided.
    for element in states:
        
        # Iterate through the possible arrow descriptions.
        for arrow in arrows:
            
            # Add a state change to the string.
            final_str += f"({element}, {arrow}) => {character};\n"
    
    # Finalize the string by declarations.        
    final_str += """--declarations--
e=#n#;
animate=this;
simulateToStep=-1;
input=null;
s0=;
F=;
displayMode=0;
showMinimizedFSM=true;
showDeterministicFSM=false
--declarations-end--"""

    return final_str


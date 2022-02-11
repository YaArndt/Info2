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

def fsm_template(states: List[str], arrows: List[str], character: str = "s", starting: str = "s0") -> None:
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
    final_str += f"""--declarations--
e=#n#;
animate=this;
simulateToStep=-1;
input=null;
s0={starting};
F=;
displayMode=1;
showMinimizedFSM=true;
--declarations-end--"""

    return final_str

def pda_template(states: List[str], entry_alphabet: List[str], stack_alphabet: List[str], starting: str = "s0", protected_stack_character: str = "k", character: str = "s"):
    """Function to create a PDA template for the Xwizard.

    Args:
        states (List[str]): List of states to be used for the Xwizard
        entry_alphabet (List[str]): Entry Alphabet
        stack_alphabet (List[str]): Stack Alphabet
        starting (str, optional): Starting state. Defaults to "s0".
        protected_stack_character (str, optional): Stack Character k0. Defaults to "k".
        character (str, optional): State character for the transitions. Defaults to "s".
    """    
    
    if not "lambda" in entry_alphabet:
        entry_alphabet.append("lambda")
        
    if not protected_stack_character in stack_alphabet:
        stack_alphabet.append(protected_stack_character)
    
    
    # Initialize the final string
    final_str = "pda:\n"
    
    # Iterate through the states provided.
    for state in states:
        
        # Iterate through the possible entry characters.
        for entry_character in entry_alphabet:
            
            # Iterate Through the possible stack characters
            for stack_character in stack_alphabet:
            
                # Add a state change to the string.
                final_str += f"({state}, {entry_character}, {stack_character}) => ({character}, );\n"

    # Finalize the string by declarations.        
    final_str += f"""--declarations--
e=#n#;
s0={starting};
F=;
kSymb={protected_stack_character};
inputs=null;
simSteps=0
--declarations-end--
"""

    return final_str
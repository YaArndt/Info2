from xwizard_templates import *
from hamming import *

if __name__ == "__main__":
    
    alph = ["a", "b"]
    bin = [0, 1]
    
    states = num_states(7)
    
    template = fsm_template(states, bin)
    addToClipBoard(template)
    
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
    
    
    # pda_template_text = pda_template(states, alph, bin)
    # addToClipBoard(pda_template_text)
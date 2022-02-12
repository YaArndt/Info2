from xwizard_templates import *
from hamming import *
from number_coding import *

# Requires Pyperclip:
# pip install pyperclip

if __name__ == "__main__":
    
    alph = ["a", "b"]
    bin = [0, 1]
    
    # -----------------------------------------------------------------------
    # FSM AUTOMATION
    # -----------------------------------------------------------------------
    
    # fsm_states = num_states(7)
    # fsm_template = fsm_template(fsm_states, bin)
    # addToClipBoard(fsm_template)
    
    # -----------------------------------------------------------------------
    # PDA AUTOMATION
    # -----------------------------------------------------------------------
    
    # pda_states = num_states(7)    
    # pda_template_text = pda_template(pda_states, alph, bin)
    # addToClipBoard(pda_template_text)
    
    # -----------------------------------------------------------------------
    # HAMMING  AUTOMATION
    # -----------------------------------------------------------------------
    
    listed_hamming([
        "HUFFMAN",
        "HOFMANN"
    ])
    
    # -----------------------------------------------------------------------
    # NUMBER AUTOMATION
    # -----------------------------------------------------------------------
    
    twos_comp(-4, 4)
    
    BCD_to_decimal('0111')
    
    BCD_from_decimal(8)
from xwizard_templates import *

if __name__ == "__main__":
    
    alph = ["a", "b"]
    bin = [0, 1]
    
    states = num_states(3)
    
    template = fsm_template(states, bin)
    addToClipBoard(template)
    
    
    # pda_template_text = pda_template(states, alph, bin)
    # addToClipBoard(pda_template_text)
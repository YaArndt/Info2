from xwizard_templates import *

if __name__ == "__main__":
    
    states = num_states(3)
    arrows = ["a", "b"]
    
    template = fsm_template(states, arrows)
    addToClipBoard(template)
from typing import *


def num_states(character: str, number: int, start: int) -> List[str]:
    
    result = []
    num = start
    
    for _ in range(number):
        result.append(f"{character}{num}")
        num += 1
        
    return result

def fsm_template(states: List[str], arrows: List[str], char: str = None) -> None:
    
    final_str = "fsm:\n"
    
    for element in states:
        for arrow in arrows:
            final_str += f"({element}, {arrow}) => {char};\n"
            
    final_str += """--declarations--
e=#n#;
animate=this;
simulateToStep=-1;
input=null;
s0=              ;
F=                ;
displayMode=0;
showMinimizedFSM=true;
showDeterministicFSM=false
--declarations-end--"""

    return final_str

states = num_states("s", 6, 0)

print(fsm_template(states, ["a", "b"], "s"))

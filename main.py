from xwizard_templates import *
from hamming import *
from number_coding import *
from cache_calculator import *

# REQUIREMENTS!!! EXECUTE THIS IN  THE TERMINAL!!!
# pip install pyperclip numpy scipy pandas

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
    
    # listed_hamming([
    #     "HUFFMAN",
    #     "HOFMANN"
    # ])
    
    # -----------------------------------------------------------------------
    # NUMBER AUTOMATION
    # -----------------------------------------------------------------------
    
    # BCD_from_decimal("89684943")
    # BCD_to_decimal("10001001011010000100100101000011")
    
    # EXC3_from_decimal("193")
    # EXC3_to_decimal("10011100")
    
    # AIKEN_from_decimal("234")
    # AIKEN_to_decimal("11001111")
    
    # # Check which encoding  is valid and return the corresponding decimal
    # get_valid_encoding("01110011010110100100101101100101")
    
    # # Encode in BCD, Excess3 and AIKEN
    # encode_in_all("69")
    
    # twos_comp(-1, 4)
    
    # -----------------------------------------------------------------------
    # CACHE SIMULATION
    # -----------------------------------------------------------------------
    
    # directly_mapped_cache(8, [
    #     101, 102, 104, 108, 104, 103, 104, 102, 107, 180, 101, 102, 103, 110, 111, 112
    # ])
        
            
    # associative_cache(8, [
    #     101, 102, 104, 108, 104, 103, 104, 102, 107, 180, 101, 102, 103, 110, 111, 112
    # ])
    
    
    # block_cache(5, 3, [
    #     67, 49, 156, 95, 12, 38, 128, 92, 106, 78, 117, 38, 67, 45, 128, 38, 60, 53, 3, 78, 63, 206, 175, 38, 184, 156, 211
    # ])
from textwrap import fill
from typing import *
import pandas as pd

def directly_mapped_cache(k: int, addresses: List[int]):
    
    cache_row = [i for i in range(k)]
    cache_addresses = [[] for _ in range(k)]
    cache_tag = [None] * k
    
    while len(addresses) > 0:
        
        current_address = addresses.pop(0) 
        
        line_index = current_address % k  
        
        cache_tag[line_index] = current_address
        
        if cache_tag[line_index] is not None:
            if cache_addresses[line_index] is not None:
                cache_addresses[line_index].append(current_address)
            else:
                cache_addresses[line_index] = [current_address]
        
    for i in range(k):
        if cache_tag[i] is not None:
            cache_tag[i] = cache_tag[i] // k

    result = pd.DataFrame(data=[], columns=[])
    
    result["Row"] = cache_row
    result["Addresses"] = cache_addresses
    result["Tags"] = cache_tag
    
    print(result)
        
        
def associative_cache(k: int, addresses: List[int]):
    
    seen = set()
    
    cache_row = [i for i in range(k)]
    cache_addresses = [[] for _ in range(k)]
    cache_tag = [None] * k
    cache_dates = [[] for _ in range(k)]
    cache_date = [None] * k

    time_counter = 0
    
    filled = False
    last_empty = 0
    
    for address in addresses:
        
        if address in seen:
            line_index = cache_tag.index(address)
            cache_dates[line_index].append(time_counter + 1)
            cache_date[line_index] = time_counter + 1
            
            time_counter += 1
            
        elif filled:
            
            replace_line = cache_date.index(min(set(cache_date)))
            seen.remove(cache_tag[replace_line])
            
            replaced_address = cache_tag[replace_line]
            
            cache_addresses[replace_line].append(replaced_address)
            
            cache_tag[replace_line] = address
            seen.add(address)
            
            replaced_times = [f"({replaced_address}: {cache_dates[replace_line]})", time_counter + 1]
            cache_dates[replace_line] = replaced_times
            
            cache_date[replace_line] = time_counter + 1
            
            time_counter += 1
            
        else: 
            
            if last_empty == k-1:
                filled = True
                
            cache_tag[last_empty] = address
            cache_addresses[last_empty] = [address]
            seen.add(address)
            
            cache_dates[last_empty] = [time_counter + 1]
            cache_date[last_empty] = time_counter + 1
            
            time_counter += 1
            last_empty += 1
                
    result = pd.DataFrame(data=[], columns=[])
    
    result["Row"] = cache_row
    result["Addresses"] = cache_addresses
    result["Dates"] = cache_dates
    result["Last Date"] = cache_date
    result["Tags"] = cache_tag
        
    print(result)
        
        
        
if __name__ == "__main__":      
    
    directly_mapped_cache(8, [
        101, 102, 104, 108, 104, 103, 104, 102, 107, 180, 101, 102, 103, 110, 111, 112
    ])
        
            
    associative_cache(8, [
        101, 102, 104, 108, 104, 103, 104, 102, 107, 180, 101, 102, 103, 110, 111, 112
    ])
        
        
        
        
        
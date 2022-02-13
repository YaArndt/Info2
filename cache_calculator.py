from typing import *
import pandas as pd

def directly_mapped_cache(k: int, addresses: List[int], print_res: bool = True) -> pd.DataFrame:
    """Function to simulate a directly mapped cache.

    Args:
        k (int): Number of lines in the cache.
        addresses (List[int]): Addresses to be mapped.
        print_res (bool, optional): Wheather or not to print the result directly. Defaults to True.

    Returns:
        pd.DataFrame: Dataframe of the cache.
    """
    
    cache_row = [i for i in range(k)]
    cache_addresses = [[] for _ in range(k)]
    cache_tag = [None] * k
    cache_tag_div = [None] * k
    
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
            cache_tag_div[i] = cache_tag[i] // k

    result = pd.DataFrame(data=[], columns=[])
    
    result["Row"] = cache_row
    result["Addresses"] = cache_addresses
    result["Tags"] = cache_tag
    result["Tags Devided"] = cache_tag_div
    
    if print_res:
        print(result)
    
    return result
        
        
def associative_cache(k: int, addresses: List[int], print_res: bool = True) -> pd.DataFrame:
    """Function to simulate an associative cache with LRU replacement policy.

    Args:
        k (int): Number of lines in the cache.
        addresses (List[int]): Addresses to be mapped.
        print_res (bool, optional): Wheather or not to prit the results directly. Defaults to True.

    Returns:
        pd.DataFrame: Dataframe of the results
    """
    
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
            seen.add(address)
            
            cache_dates[last_empty] = [time_counter + 1]
            cache_date[last_empty] = time_counter + 1
            
            time_counter += 1
            last_empty += 1
                
    for i in range(k):
        
        if cache_tag[i] is not None:
            cache_addresses[i].append(cache_tag[i])           
                
    result = pd.DataFrame(data=[], columns=[])
    
    result["Row"] = cache_row
    result["Addresses"] = cache_addresses
    result["Dates"] = cache_dates
    result["Last Date"] = cache_date
    result["Tags"] = cache_tag
        
    if print_res:    
        print(result)
    
    return result
        
def block_cache(blocks: int, lines: int, addresses: List[str]) -> pd.DataFrame:
    """Simulates a block cache with direct mapping of blocks and associative mapping inside the blocks.
    Uses LRU in the associative part.

    Args:
        blocks (int): Number of blocks.
        lines (int): Number of lines per block.
        addresses (List[str]): Addresses to be mapped.
    """
    
    direct_coolection = directly_mapped_cache(blocks, addresses, False)["Addresses"]
    counter = 1
    
    for collection in direct_coolection:
        
        print(f"--------------------------------------------------------------------------\nBLOCK {counter}")
        
        associative_result = associative_cache(lines, collection, False)
        
        associative_result["Tags Devided"] = [tag // blocks for tag in associative_result["Tags"]]
        print(associative_result)
        
        print("\n\n")
        
        counter += 1
    
    
    
        
if __name__ == "__main__":      
    
    directly_mapped_cache(5, [
        67, 49, 156, 95, 12, 38, 128, 92, 106, 78, 117, 38, 67, 45, 128, 38, 60, 53, 3, 78, 63, 206, 175, 38, 184, 156, 211
    ])
            
    # associative_cache(8, [
    #     12,34,56,78
    # ])
    
    # block_cache(5, 3, [
    #     67, 49, 156, 95, 12, 38, 128, 92, 106, 78, 117, 38, 67, 45, 128, 38, 60, 53, 3, 78, 63, 206, 175, 38, 184, 156, 211
    # ])
        
        
        
        
        
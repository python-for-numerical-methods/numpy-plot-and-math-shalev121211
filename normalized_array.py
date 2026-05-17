import numpy as np

def normalize_array(input_array):
    arr_min = np.min(input_array)
    arr_max = np.max(input_array)
    
    if arr_min == arr_max:
        return np.zeros_like(input_array, dtype=float)
        
    new_array = (input_array - arr_min) / (arr_max - arr_min)
    
    return new_array

if __name__ == "__main__":
    test_data = np.array([10, 20, 30, 40, 50])
    print(f"Original: {test_data}")
    print(f"Normalized: {normalize_array(test_data)}")

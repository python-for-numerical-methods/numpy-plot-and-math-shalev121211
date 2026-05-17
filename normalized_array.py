import numpy as np

def normalize_array(input_array):
    # וידוא שהקלט הוא מערך numpy, למקרה שהטסטר מכניס רשימה רגילה
    arr = np.array(input_array, dtype=float)
    
    arr_min = np.min(arr)
    arr_max = np.max(arr)
    
    if arr_min == arr_max:
        return np.zeros_like(arr)
        
    new_array = (arr - arr_min) / (arr_max - arr_min)
    
    return new_array

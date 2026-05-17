import numpy as np

def normalize_array(input_array):
    arr_min = np.min(input_array)
    arr_max = np.max(input_array)
    
    if arr_min == arr_max:
        return np.zeros_like(input_array, dtype=float)
        
    new_array = (input_array - arr_min) / (arr_max - arr_min)
    
    return new_array
    # חשוב לזכור להחליף את pass ב- return

if __name__ == "__main__":
    # כאן הסטודנטים יכולים להריץ בדיקה עצמית מהירה
    test_data = [10, 20, 30, 40, 50]
    print(f"Original: {test_data}")
    print(f"Normalized: {normalized_array(test_data)}")

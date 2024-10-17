import numpy as np

def choice_numbers(_data, _sid_time, _size=6):
    numbers = list(map(int, _data.keys()))
    weights = list(map(int, _data.values()))
    
    np.random.seed(int(_sid_time.timestamp()))
    selected_numbers = np.random.choice(numbers, size=_size, replace=False, p=np.array(weights) / sum(weights))
    return selected_numbers
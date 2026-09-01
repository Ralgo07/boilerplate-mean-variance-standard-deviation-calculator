import numpy as np

def calculate(list):

    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")

    matrix = np.array(list).reshape(3, 3)

    mean = [
        matrix.mean(axis=0).tolist(),
        matrix.mean(axis=1).tolist(),
        matrix.mean()
    ]

    variance = [
        matrix.var(axis=0).tolist(),
        matrix.var(axis=1).tolist(),
        matrix.var()
    ]

    std_dev = [
        matrix.std(axis=0).tolist(),
        matrix.std(axis=1).tolist(),
        matrix.std()
    ]

    max_val = [
        matrix.max(axis=0).tolist(),
        matrix.max(axis=1).tolist(),
        matrix.max()
    ]

    min_val = [
        matrix.min(axis=0).tolist(),
        matrix.min(axis=1).tolist(),
        matrix.min()
    ]

    sum_val = [
        matrix.sum(axis=0).tolist(),
        matrix.sum(axis=1).tolist(),
        matrix.sum()
    ]

    # 4. Estructurar el diccionario de salida
    calculations = {
        'mean': mean,
        'variance': variance,
        'standard deviation': std_dev,
        'max': max_val,
        'min': min_val,
        'sum': sum_val
    }

    return calculations
def dot(v, w):
    """(v_1 * w_1) + (v_2 * w_2)  ... + (v_n * w_n)"""
    return sum(v_i * w_i
               for v_i, w_i in zip(v, w))

def sum_of_squares(v):
    """v_1 * v_1 + ... + v_n * v_n"""
    return dot(v, v)

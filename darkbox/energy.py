import numpy as np


def square(x):
    """Calculate the sum-of-squares energy of the input.

    Some more details here. 
    
    Parameters
    ----------
    x : ndarray
        Input signal.

    Returns
    -------
    energy : float
             Energy of the signal `x`.
             
    """
    return np.sum(x**2)

import numpy as np
cimport numpy as np

ctypedef np.float64_t DTYPE_t  # Define Cython's fast double type
def smooth(np.ndarray[DTYPE_t, ndim=1] Y):
    """
    Argument:
    Y -> a 1D numpy array
    Function:
    Perform rough smoothing by averaging every three data points.
    """
    cdef int N = Y.shape[0]  # the number of data points
    cdef np.ndarray[DTYPE_t, ndim=1]  YAVE = np.empty(N, dtype=np.float64)  # array to store the smoothed data
    YAVE[0] = Y[0]
    YAVE[-1] = Y[-1]
    for i in range(1, N-1):
        YAVE[i] = (Y[i-1] + Y[i] + Y[i+1])/3
    return YAVE
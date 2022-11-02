"""
This module contains general helper functions.
"""

import numpy as np

def load_spectrum(path_to_file: str,
                  fft_size: int,
                  dtype: type) -> np.array:
    """
    Simple function to load the FFT spectrum from a binary file into a numpy array.

    Parameters
    ----------
    path_to_file
        Path to the binary file.
    fft_size
        Size of the FFT used to produce the file.
    dtype
        Data type of the binary.

    Returns
    -------
    spectrum_array
        Array containing one spectrum per timestep.
    """

    spectrum_array = np.fromfile(path_to_file, dtype=dtype).reshape((-1, fft_size))
    return spectrum_array
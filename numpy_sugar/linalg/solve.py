from numpy.linalg import solve as npy_solve
from numpy import array
from numpy import dot


def solve(A, b):
    r"""Solve for the linear equations :math:`\mathrm A \mathbf x = \mathbf b`.

    Args:
        A (array_like): Coefficient matrix.
        b (array_like): Ordinate values.

    Returns:
        :class:`numpy.ndarray`: Solution ``x``.
    """
    if A.shape[0] == 1:
        A_ = array([[1. / A[0, 0]]])
        return dot(A_, b)
    elif A.shape[0] == 2:
        a = A[0, 0]
        b = A[0, 1]
        c = A[1, 0]
        d = A[1, 1]
        A_ = array([[d, -b], [-c, a]])
        A_ /= a * d - b * c
        return dot(A_, b)
    return _solve(A, b)

def _solve(A, b):
    return npy_solve(A, b)

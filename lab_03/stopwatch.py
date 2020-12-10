import os
import sys
from time import process_time


def stopwatch(function, params) -> float:
    """
    :param function: function-pointer, that you want to test

    :param params: array of parametres, that your function requires

    :return: float of time, that your function runs

    Process time of your function: sum of the kernel and user-space CPU time.

    Uses process_time library

    P.S. if you're using array, just wrap it in another array. For example:

    def f(array):
        for i in array:
            print(i)

    stopwatch.stopwatch(f, [2, 3, 4, 5]) -> error
    stopwatch.stopwatch(f, [[2, 3, 4, 5]]) -> working good!
    """

    class HiddenPrints:
        """
        uses to disable prints, that your function may use

        Uses just to keep terminal clean :)
        """

        def __enter__(self):
            self._original_stdout = sys.stdout
            sys.stdout = open(os.devnull, 'w')

        def __exit__(self, exc_type, exc_val, exc_tb):
            sys.stdout.close()
            sys.stdout = self._original_stdout

    start = process_time()

    with HiddenPrints():
        function(*params)

    end = process_time()

    return end - start
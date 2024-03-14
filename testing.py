import sys

verbose = False

def print_(
    *values: object,
    sep: str | None = " ",
    end: str | None = "\n",
) -> None:
        if verbose:
                print(values, sep, end)
        else:
                pass
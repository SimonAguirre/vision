import sys

VERBOSE = True

def print_(
    *values: object,
    sep: str | None = " ",
    end: str | None = "\n",
) -> None:
        if VERBOSE:
                print(values, sep, end)
        else:
                pass
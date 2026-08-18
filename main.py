"""Path of the Bloodied One entry point.

The former monolithic runtime is now classified by subsystem.  The bootstrap keeps
a shared namespace during this compatibility-preserving refactor so save files,
combat timings, globals and patch-order semantics remain unchanged.
"""

from core.bootstrap import run


if __name__ == "__main__":
    run(__file__)

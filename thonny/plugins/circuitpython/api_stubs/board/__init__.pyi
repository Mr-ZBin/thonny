"""Board specific pin names

Common container for board base pin names. These will vary from board to
board so don't expect portability when using this module.

.. warning:: The board module varies by board. The APIs documented here may or may not be
             available on a specific board."""

from __future__ import annotations

import busio

board_id: str
"""Board ID string. The unique identifier for the board model in
circuitpython, as well as on circuitpython.org.
Example: "hallowing_m0_express"."""

def I2C() -> busio.I2C:
    """Returns the `busio.I2C` object for the board's designated I2C bus(es).
    The object created is a singleton, and uses the default parameter values for `busio.I2C`."""
    ...

def SPI() -> busio.SPI:
    """Returns the `busio.SPI` object for the board's designated SPI bus(es).
    The object created is a singleton, and uses the default parameter values for `busio.SPI`."""
    ...

def UART() -> busio.UART:
    """Returns the `busio.UART` object for the board's designated UART bus(es).
    The object created is a singleton, and uses the default parameter values for `busio.UART`."""
    ...

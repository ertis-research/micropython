# This module just allows `import umodbus` to work. It lazy-loads from
# `umodbus` without duplicating its globals dict.


def __getattr__(attr):
    import umodbus

    return getattr(umodbus, attr)

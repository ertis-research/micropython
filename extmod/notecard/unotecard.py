# This module just allows `import unotecard` to work. It lazy-loads from
# `notecard` without duplicating its globals dict.


def __getattr__(attr):
    import notecard

    return getattr(notecard, attr)

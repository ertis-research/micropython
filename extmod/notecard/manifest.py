package(
    "notecard",
    (
        "__init__.py",
        "binary_helpers.py",
        "card.py",
        "cobs.py",
        "crc32.py",
        "env.py",
        "file.py",
        "gpio.py",
        "hub.py",
        "md5.py",
        "note.py",
        "notecard.py",
        "timeout.py",
        "transaction_manager.py",
        "validators.py"
    ),
    base_path="..",
    opt=3,
)

# Backwards-compatible notecard module.
module("unotecard.py", opt=3)

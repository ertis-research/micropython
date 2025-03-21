package(
    "umodbus",
    (
        "__init__.py",
        "common.py",
        "const.py",
        "functions.py",
        "modbus.py",
        "serial.py",
        "tcp.py",
        "typing.py",
        "version.py"
    ),
    base_path="..",
    opt=3,
)

# Backwards-compatible notecard module.
module("umodbus.py", opt=3)

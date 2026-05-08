import logging
import os

LOG_FILE = "trading_bot.log"

def setup_logger(name: str) -> logging.Logger:
    """
    Sets up a logger that writes to both:
    - The terminal (so you can see what's happening)
    - A log file (so you have a record of everything)
    """

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # Don't add duplicate handlers if logger already exists
    if logger.handlers:
        return logger

    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    # --- File Handler (writes to trading_bot.log) ---
    file_handler = logging.FileHandler(LOG_FILE)
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    # --- Console Handler (prints to terminal) ---
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger

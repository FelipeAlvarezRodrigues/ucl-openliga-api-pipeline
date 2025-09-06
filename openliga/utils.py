import logging


def setup_logging():
    # Configures the logging system for the project.
    logging.basicConfig(
        level=logging.INFO,  # Sets the minimum level of messages to INFO (shows INFO, WARNING, ERROR)
        format="%(asctime)s - %(levelname)s - %(message)s",  # Defines the format: timestamp, level, message
        filename="data/project.log",
        filemode="w",  # "w" overwrites the log file each run; use "a" to append to the file instead
    )

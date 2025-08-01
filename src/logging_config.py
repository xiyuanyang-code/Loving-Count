import logging
import os
import sys

sys.path.append(os.getcwd())

SHARED_LOGGER_NAME = "LovingCount"
LOG_DIR_HOME = os.path.join(os.getcwd(), "log")


def setup_logging_config():
    logger = logging.getLogger(SHARED_LOGGER_NAME)
    if logger.handlers:
        return logger
    logger.setLevel(logging.INFO)
    log_dir_home = LOG_DIR_HOME
    log_file_path = os.path.join(log_dir_home, "love.log")

    try:
        os.makedirs(log_dir_home, exist_ok=True)
        with open(log_file_path, "a") as f:
            f.write("")
    except OSError as e:
        print(
            f"Warning: Could not create or write to log file at '{log_dir_home}'. Using /tmp instead. Error: {e}",
            file=sys.stderr,
        )
        log_file_path = os.path.join("/tmp", "love.log")
        try:
            with open(log_file_path, "a") as f:
                f.write("")
        except OSError as e:
            print(
                f"Critical Warning: Could not create or write to log file in /tmp. File logging will be disabled. Error: {e}",
                file=sys.stderr,
            )
            log_file_path = None
    formatter = logging.Formatter("%(asctime)s %(levelname)s [%(name)s]: %(message)s")
    if log_file_path:
        file_handler = logging.FileHandler(log_file_path, encoding="utf-8")
        file_handler.setLevel(logging.INFO)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.WARNING)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    logger.propagate = False
    return logger


if __name__ == "__main__":
    logger = setup_logging_config()
    logger.info("Hello world")

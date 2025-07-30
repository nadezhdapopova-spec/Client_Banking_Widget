import logging
import os.path
from pathlib import Path
from typing import Literal

from config import ROOT_DIR

# masks_logger = logging.getLogger("masks_logger")
# masks_handler = logging.FileHandler(os.path.join(ROOT_DIR, "logs", "masks.log"), "w", encoding="utf-8")
# masks_formatter = logging.Formatter("%(asctime)s - %(filename)s - %(levelname)s - %(message)s",
#                                     datefmt="%Y-%m-%d %H:%M:%S")
# masks_handler.setFormatter(masks_formatter)
# masks_logger.addHandler(masks_handler)
# masks_logger.setLevel(logging.DEBUG)
#
#
# utils_logger = logging.getLogger("utils_logger")
# utils_handler = logging.FileHandler(os.path.join(ROOT_DIR, "logs", "utils.log"), "w", encoding="utf-8")
# utils_formatter = logging.Formatter("%(asctime)s - %(filename)s - %(levelname)s - %(message)s",
#                                     datefmt="%Y-%m-%d %H:%M:%S")
# utils_handler.setFormatter(utils_formatter)
# utils_logger.addHandler(utils_handler)
# utils_logger.setLevel(logging.DEBUG)
#
#
# reading_csv_excel_logger = logging.getLogger("reading_csv_excel_logger")
# reading_csv_excel_handler = logging.FileHandler(os.path.join(ROOT_DIR, "logs", "reading_csv_excel_.log"),
#                                                 "w", encoding="utf-8")
# reading_csv_excel_formatter = logging.Formatter("%(asctime)s - %(filename)s - %(levelname)s - %(message)s",
#                                                 datefmt="%Y-%m-%d %H:%M:%S")
# reading_csv_excel_handler.setFormatter(reading_csv_excel_formatter)
# reading_csv_excel_logger.addHandler(reading_csv_excel_handler)
# reading_csv_excel_logger.setLevel(logging.DEBUG)

LogLevel = int | Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]

def setup_logger(name: str,
                 level: LogLevel = "INFO",
                 log_file: str | None = None,
                 log_to_console: bool = False,
                 fmt: str = "%(asctime)s - %(levelname) - logger:%(name)s - module:%(module)s - func:%(funcName)s:%(lineno)d - %(message)s"
                 ) -> logging.Logger:
    """
    Настраивает универсальный логгер для проекта.
    :param name: Имя логгера (обычно __name__)
    :param level: уровень логирования (по умолчанию INFO)
    :param log_file: путь к лог-файлу (если нужно логировать в файл)
    :param log_to_console: по умолчанию не создается (если нужно логировать в консоль)
    :param fmt: формат сообщения
    :return: настроенный логгер
    """

    logger = logging.getLogger(name)
    logger.setLevel(level)
    formatter = logging.Formatter(fmt, datefmt="%Y-%m-%d %H:%M:%S")

    if log_to_console:
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    if log_file:
        logs_dir = Path(__file__).resolve().parent.parent / "logs"
        log_path = logs_dir / log_file
        file_handler = logging.FileHandler(log_path, mode="w", encoding="utf-8")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger





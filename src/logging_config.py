import logging
import os.path

from config import ROOT_DIR

masks_logger = logging.getLogger("masks_logger")
masks_handler = logging.FileHandler(os.path.join(ROOT_DIR, "logs", "masks.log"), "w", encoding="utf-8")
masks_formatter = logging.Formatter("%(asctime)s - %(filename)s - %(levelname)s - %(message)s",
                                    datefmt="%Y-%m-%d %H:%M:%S")
masks_handler.setFormatter(masks_formatter)
masks_logger.addHandler(masks_handler)
masks_logger.setLevel(logging.DEBUG)


utils_logger = logging.getLogger("utils_logger")
utils_handler = logging.FileHandler(os.path.join(ROOT_DIR, "logs", "utils.log"), "w", encoding="utf-8")
utils_formatter = logging.Formatter("%(asctime)s - %(filename)s - %(levelname)s - %(message)s",
                                    datefmt="%Y-%m-%d %H:%M:%S")
utils_handler.setFormatter(utils_formatter)
utils_logger.addHandler(utils_handler)
utils_logger.setLevel(logging.DEBUG)


reading_csv_excel_logger = logging.getLogger("reading_csv_excel_logger")
reading_csv_excel_handler = logging.FileHandler(os.path.join(ROOT_DIR, "logs", "reading_csv_excel_.log"),
                                                "w", encoding="utf-8")
reading_csv_excel_formatter = logging.Formatter("%(asctime)s - %(filename)s - %(levelname)s - %(message)s",
                                                datefmt="%Y-%m-%d %H:%M:%S")
reading_csv_excel_handler.setFormatter(reading_csv_excel_formatter)
reading_csv_excel_logger.addHandler(reading_csv_excel_handler)
reading_csv_excel_logger.setLevel(logging.DEBUG)

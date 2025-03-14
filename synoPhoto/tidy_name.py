"""

Script pour ranger les images qui arrivent sur le NAS

python /volume1/batch/photo/__main__.py \
--root_path=/volume1/homes/*/photo  \
--image=PXL_YYYYMM*_*.jpg  \
--path_dest=/volume1/photo/

"""
import logging
import os
import argparse
from glob import glob
from os import PathLike
from typing import Union
from freeMobileSMS.logging import Logger
from .results import ResultsReports


def range_photos(root_path: Union[PathLike, str],
                 image: Union[PathLike, str],
                 path_dest: Union[PathLike, str],
                 file_extension: str,
                 logger: Union[Logger, None] = None
                 ) -> ResultsReports:
    """
    List images file matching a pattern and moves it in photo folder.

    :param root_path: In images folder.
    :param image: image pattern
    :param path_dest: destination folder
    :param logger: Log object
    :param file_extension: file extension

    returns ResultsReports

    """

    reports = ResultsReports()

    file_path_glob = os.path.join(root_path, image) + f".{file_extension}"  # Images to move

    if logger is not None:
        logger.log(level=logging.INFO, message=f"Start {file_path_glob}")

    file_path = glob(file_path_glob.replace("YYYYMM", "*"))  # Images to move

    year_s = image.index("YYYY")
    month_s = image.index("MM")
    file_year_month = {(os.path.basename(p)[year_s:year_s + 4], os.path.basename(p)[month_s:month_s + 2]) for p in file_path}

    for year, month in file_year_month:

        logger.log(level=logging.INFO, message=f"Start: {year}/{month}")
        if year.isnumeric() and month.isnumeric() :
            # Check both year and month are int
            if logger is not None:
                logger.log(level=logging.INFO, message=f"Start: {year}/{month}")

            # Folder creation if needed
            path_in = file_path_glob.replace("YYYY", year).replace("MM", month)
            path_out = os.path.join(path_dest, year, month)
            os.makedirs(path_out, exist_ok=True)  # Create folder if needed

            cmd = f"mv {os.path.abspath(path_in)} {os.path.abspath(path_out)}"
            try:
                os.system(cmd)

                if logger is not None:
                    logger.log(level=logging.INFO, message=f"Run {cmd}")

                reports.log_file_move()

            except:
                reports.log_error()

                if logger is not None:
                    logger.log(level=logging.ERROR, message=f"Fail to run {cmd}")

    return reports


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--root_path",
                        type=str,
                        required=False,
                        default="/volume1/homes/*/photo/"
                        )
    parser.add_argument("--image",
                        type=str,
                        required=False,
                        default="PXL_YYYYMM*_*"
                        )

    parser.add_argument("--path_dest",
                        type=str,
                        required=False,
                        default="/volume1/photo/"
                        )
    parser.add_argument("--extension",
                        type=str,
                        required=True,
                        default=[],
                        nargs="+",
                        help="File extension"
                        )

    args = parser.parse_args()

    report = ResultsReports()
    for ext in args.extension:
        report += range_photos(root_path=args.root_path,
                               image=args.image,
                               path_dest=args.path_dest,
                               file_extension=ext
                               )

if __name__ == "__main__":
    main()

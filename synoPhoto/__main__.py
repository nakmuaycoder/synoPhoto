"""


"""
import argparse
import logging
from freeMobileSMS.logging import Logger
from .tidy_name import range_photos
from .results import ResultsReports


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--root_path",
                        type=str,
                        required=False,
                        default="/volume1/homes/*/photo/"
                        )
    parser.add_argument("--path_dest",
                        type=str,
                        required=False,
                        default="/volume1/photo/"
                        )
    parser.add_argument("--free_mobile_user",
                        type=str,
                        required=False,
                        default=None,
                        help="Free mobile user"
                        )
    parser.add_argument("--free_mobile_password",
                        type=str,
                        required=False,
                        default=None,
                        help="Free mobile password"
                        )
    parser.add_argument("--video",
                        action="store_true",
                        required=False,
                        default=False,
                        help="Move video file"
                        )
    parser.add_argument("--image",
                        action="store_true",
                        required=False,
                        default=False
                        )
    parser.add_argument("--pixel",
                        action="store_true",
                        required=False,
                        default=False
                        )
    parser.add_argument("--samsung",
                        action="store_true",
                        required=False,
                        default=False
                        )


    args = parser.parse_args()

    logger = Logger(log_name="tidy_photo",
                    free_mobile_user=args.free_mobile_user,
                    free_mobile_pass=args.free_mobile_password
                    )

    extensions = []
    if args.video:
        extensions.append("mp4")
    if args.image:
        extensions.append("jpg")

    patterns = []
    if args.pixel:
        patterns.append("PXL_YYYYMM*")
    if args.samsung:
        patterns.append("YYYYMM*_*")

    report = ResultsReports()
    print("OK")

    for pattern in patterns:

        for ext in extensions:
            logger.log(level=logging.INFO,
                       message=f"Run for: {pattern}.{ext}"
                       )

            report += range_photos(root_path=args.root_path,
                                   image=pattern,
                                   path_dest=args.path_dest,
                                   logger=logger,
                                   file_extension=ext
                                   )


    if report.has_error:
        logger.send_sms(message=f"An error occur: log available at {logger.path_log}")

    if report.has_moved:
        logger.send_sms(message=f"Tidy picture: Done")


if __name__ == "__main__":
    main()
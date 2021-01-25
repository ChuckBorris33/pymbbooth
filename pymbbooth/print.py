from os import path
from sys import argv
from pprint import pprint

from pymbbooth import config

try:
    import cups
except ImportError:
    pass

PRINTER_STATUS_MAP = {
    3: "PENDING",
    4: "HELD",
    5: "PROCESSING",
    6: "STOPPED",
    7: "CANCELED",
    8: "ABORTED",
    9: "COMPLETED",
}


def print_photo(photo):
    conn = cups.Connection()
    printer = conn.getPrinters()[config.PRINTER_NAME]
    filepath = path.abspath(path.join("public/photos", photo))
    job_id = conn.printFile(
        config.PRINTER_NAME, filepath, "photobooth", config.PRINTER_OPTIONS
    )
    return job_id


def job_state(job_id):
    conn = cups.Connection()
    state_id = conn.getJobAttributes(job_id)["job-state"]
    return PRINTER_STATUS_MAP[state_id]


if __name__ == "__main__":
    conn = cups.Connection()
    # print_photo(argv[1])
    # conn.getDests()[('EPSON_XP_6000_Series', None)].options
    pprint(conn.getPrinterAttributes(config.PRINTER_NAME))

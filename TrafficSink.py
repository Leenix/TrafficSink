#!/usr/bin/env python

from SinkNode.Writer.ThingspeakWriter import ThingspeakWriter
from SinkNode.Reader.SerialReader import SerialReader
from SinkNode.Writer.LogFileWriter import LogFileWriter
from SinkNode.Formatter.CSVFormatter import CSVFormatter

from SinkNode import *
import sys
from traffic_count_settings import *


def start_logger():
    logger = logging.getLogger(logger_name)
    logger.setLevel(logger_level)

    # Console Logging
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(logging.Formatter(log_format))
    logger.addHandler(console_handler)

    # File Logging
    if log_filename:
        file_handler = logging.FileHandler(log_filename)
        file_handler.setFormatter(logging.Formatter(log_format))
        file_handler.setLevel(file_logger_level)
        logger.addHandler(file_handler)


if __name__ == '__main__':
    yun_reader = SerialReader(baud_rate=SERIAL_BAUD,
                              port=SERIAL_PORT,
                              start_delimiter=PACKET_START,
                              stop_delimiter=PACKET_STOP,
                              logger_level=logging.DEBUG)

    log_writer = LogFileWriter(log_filename, CSVFormatter())
    uploader = ThingspeakWriter(writer_id='trafficCount', api_key="KY7G0UVNHA25GQ73", key_map=TRAFFIC_KEY_MAP)

    ingestor = SinkNode()
    ingestor.add_reader(yun_reader)
    ingestor.add_logger(log_writer)
    ingestor.add_writer(uploader)

    ingestor.start()

    try:
        while True:
            pass

    except KeyboardInterrupt:
        ingestor.stop()
        sys.exit()
#!/usr/bin/env python

from SinkNode.Writer.ThingspeakWriter import ThingspeakWriter
from SinkNode.Reader.SerialReader import SerialReader
from SinkNode.Writer.LogFileWriter import LogFileWriter
from SinkNode.Formatter.CSVFormatter import CSVFormatter

from SinkNode import *
import sys
from traffic_count_settings import *

if __name__ == '__main__':
    yun_reader = SerialReader(baud_rate=SERIAL_BAUD,
                              port=SERIAL_PORT,
                              start_delimiter=PACKET_START,
                              stop_delimiter=PACKET_STOP,
                              logger_level=logging.DEBUG)

    log_writer = LogFileWriter(filename=log_filename,
                               path="/mnt/sda1/",
                               formatter=CSVFormatter(columns=HEADINGS),
                               file_time_prefix="%Y-%m-%d ",
                               timestamp_format="%Y-%m-%d,%H:%M:%S")

    thingspeak_writer = ThingspeakWriter(writer_id="Flauros",
                                         api_key="KY7G0UVNHA25GQ73",
                                         key_map=TRAFFIC_KEY_MAP)

    ingestor = SinkNode()
    ingestor.add_reader(yun_reader)
    ingestor.add_logger(log_writer)
    ingestor.add_logger(thingspeak_writer)

    ingestor.start()

    try:
        while True:
            pass

    except KeyboardInterrupt:
        ingestor.stop()
        sys.exit()
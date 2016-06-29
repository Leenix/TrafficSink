#!/usr/bin/env python

import sys
import os
sys.path.append(os.getcwd() + "/lib")
from SinkNode.Writer.ThingspeakWriter import ThingspeakWriter
from SinkNode.Reader.SerialReader import SerialReader
from SinkNode.Writer.LogFileWriter import LogFileWriter
from SinkNode.Formatter.CSVFormatter import CSVFormatter
from BluetoothFormatter import BluetoothFormatter
from WifiDeviceReader import WifiDeviceReader
from WiFiFormatter import WiFiFormatter

import logging

from SinkNode import *
from traffic_count_settings import *

reload(sys)
sys.setdefaultencoding("utf8")

if __name__ == '__main__':
    yun_reader = SerialReader(baud_rate=SERIAL_BAUD,
                              port=SERIAL_PORT,
                              start_delimiter=PACKET_START,
                              stop_delimiter=PACKET_STOP,
                              logger_level=logging.DEBUG)

    traffic_log_writer = LogFileWriter(writer_id="Pixie",
                                       filename=log_filename,
                                       # path="/mnt/sda1/",
                                       formatter=CSVFormatter(columns=HEADINGS),
                                       file_time_prefix="%Y-%m-%d ",
                                       timestamp_format="%Y-%m-%d,%H:%M:%S")

    thingspeak_writer = ThingspeakWriter(writer_id="Pixie",
                                         api_key="KY7G0UVNHA25GQ73",
                                         key_map=TRAFFIC_KEY_MAP)

    bluetooth_logger = LogFileWriter(writer_id="Blue",
                                     filename="bluescan.log",
                                     path="/mnt/sda1/",
                                     formatter=BluetoothFormatter(),
                                     file_time_prefix="%Y-%m-%d ",
                                     timestamp_format=None,
                                     logger_level=logging.DEBUG)

    wifi_reader = WifiDeviceReader(dump_period=20,
                                   include_access_points=False,
                                   id='Wifi',
                                   )

    wifi_logger = LogFileWriter(writer_id="Wifi",
                                filename="wifi_devices.log",
                                path="/mnt/sda1/",
                                formatter=WiFiFormatter(),
                                file_time_prefix="%Y-%m-%d ",
                                timestamp_format=None,
                                )

    ingestor = SinkNode(logger_level=logging.DEBUG)
    # ingestor.add_reader(yun_reader)
    ingestor.add_reader(wifi_reader)

    # ingestor.add_writer(traffic_log_writer)
    # ingestor.add_writer(bluetooth_logger)
    # ingestor.add_writer(thingspeak_writer)
    ingestor.add_writer(wifi_logger)

    ingestor.start()

    try:
        while True:
            pass

    except KeyboardInterrupt:
        ingestor.stop()
        sys.exit()

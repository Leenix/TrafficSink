__author__ = 'Leenix'

from sys import platform as _platform
import logging

logger_level = logging.DEBUG
file_logger_level = logging.INFO
logger_name = "trafficCount"
log_filename = "trafficCount.log"
log_format = "%(asctime)s - %(levelname)s - %(message)s"

# Reader Settings #########################################
SERIAL_BAUD = 57600

if _platform == "linux" or _platform == "linux2":
    SERIAL_PORT = "/dev/ttyATH0"
else:
    SERIAL_PORT = "COM14"

PACKET_START = '#'
PACKET_STOP = '$'

HEADINGS = [u'version', u'id', u'event_flag', u'count_pir', u'pir_status', u'count_lidar', u'lidar_range', u'count_uvd',
            u'uvd_range', u'air_temp', u'case_temp', u'road_temp', u'humidity', u'illuminance', u'current_draw',
            u'noise', u'timestamp']


# Processor Settings ######################################

TRAFFIC_KEY_MAP = {

    "count_uvd": "field1",
    "uvd_range": "field2",
    "count_pir": "field3",
    "count_of": "field4",
    "count_lidar": "field5",
    "lidar_range": "field6",
}

TRAFFIC_CHANNEL_MAP = {
    "trafficCount": "KY7G0UVNHA25GQ73",
}



# Uploader Settings #######################################




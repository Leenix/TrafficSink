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

HEADINGS = [u'version', u'id', u'event_flag', u'count_pir', u'pir_status', u'lidar_count', u'lidar_range', u'uvd_count',
            u'uvd_range', u'air_temp', u'case_temp', u'road_temp', u'humidity', u'illuminance', u'current_draw',
            u'noise']


# Processor Settings ######################################

TRAFFIC_KEY_MAP = {

    "count_pir": "field1",
    "lidar_count": "field2",
    "uvd_count": "field3",
    "case_temp": "field4",
    "road_temp": "field5",
    "uvd_range": "field6",
    "humidity": "field7",
    "illuminance": "field8"
}

TRAFFIC_CHANNEL_MAP = {
    "Flauros": "KY7G0UVNHA25GQ73",
}



# Uploader Settings #######################################

# Installing the Prerequisites

Use the LuCi configuration interface to add the software you need.

1) Go to the __System > Software__ tab

2) Hit the button to update the software package list

3) Install the following:

    * pyserial
    * setuptools
    * git

# Set up the Yun for Serial communication

1) Log into the Yun's command line (either through SSH or some other means)

2) Navigate to the home folder. 

    cd ~

3) Download the code repository for the serial config script:

    git clone git://github.com/Leenix/YunSerial

4) Follow the instructions in the README file to set everything up

# Get the ingestor script

1) Log into the Yun's command line (either through SSH or some other means)

2) Navigate to the home folder. 

    cd ~

3) Download the code repository for the ingestor (this repo) by typing:

    git clone git://github.com/Leenix/TrafficSink

4) Install the SinkNode library...

    cd SinkNode
    python setup.py install

# Automatically run sink script

1) Edit the __/etc/rc.local__ file by entering:

    nano /etc/rc.local

2) Add the following line to the end of the file (but before exit 0):
    
    (sleep 10; python /mnt/sda1/TrafficSink/TrafficSink.py)

# Set up grenade timer

The arduino portion of the Yun is a little less stable than the Linux processor. Add this script in to restart the microcontroller at the start of every day.

    export VISUAL=nano
    crontab -e

Add the following lines to the cron table:

    #min hour day month dayofweek command
    00 00 * * * reset-mcu



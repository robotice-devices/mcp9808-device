
================================
MCP9808 - I2C temperature sensor
================================

For the Raspberry Pi this means you should hook up to the only exposed I2C bus from the main GPIO header and the library will figure out the bus number based on the Pi's revision.

For the Beaglebone Black the library will assume bus 1 by default, which is exposed with SCL = P9_19 and SDA = P9_20.

Tested: BB

Requires: Adafruit_I2C

Usage
=========

Get readings from I2C bus 0

    python driver.py -b 0

Read more
=========

* https://learn.adafruit.com/mcp9808-temperature-sensor-python-library?view=all
* https://github.com/adafruit/Adafruit_Python_MCP9808 - This lib is use old version of I2C lib
* https://github.com/philipcristiano/beagleboneblack/blob/master/mcp9808.py - This lib is used as a source

Where to buy
============

* https://www.adafruit.com/product/1782 MCP9808 $5

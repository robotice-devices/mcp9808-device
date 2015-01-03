#!/usr/bin/python

import MCP9808
import logging
LOG = logging.getLogger("robotice.monitor.mcp9808")

def get_data(sensor):
    """
    Run the MCP9808 driver to get the humidity and temperature readings.
    """

    name = sensor.get("name")
    address = sensor.get("address", 0x18)
    bus = int(sensor.get("bus", '1'))

    sensor = MCP9808.MCP9808(address=0x18, busnum=bus)
    sensor.begin()

    temp = sensor.readTempC()
    if temp > -40 and temp < 200:
        pass
    else:
        LOG.error("%s: Invalid values" % name)
        temp = None
  
    values = [
        ('%s.temperature' % name, temp,),
    ]

    return values

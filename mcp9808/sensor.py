#!/usr/bin/python

import logging

import MCP9808

LOG = logging.getLogger("robotice.sensor.mcp9808")

def get_data(sensor):
    """
    Run the MCP9808 driver to get the humidity and temperature readings.
    """

    name = sensor.get("name")
    bus = int(sensor.get("bus", '1'))
#    address = sensor.get("address", 0x18)

    sensor = MCP9808.MCP9808(address=0x18)
    sensor.begin()

    temp = sensor.read_temp_c()
    if temp > -40 and temp < 200:
        pass
    else:
        LOG.error("%s: Value out of range" % name)
        temp = None
  
    values = [
        ('%s.temperature' % name, temp, ),
    ]

    return values

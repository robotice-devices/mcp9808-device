
import logging

from Adafruit_I2C import Adafruit_I2C

logger = logging.getLogger("MCP9808")

MCP9808_I2CADDR_DEFAULT = 0x18
MCP9808_REG_CONFIG_SHUTDOWN = 0x0100
MCP9808_REG_CONFIG_CRITLOCKED = 0x0080
MCP9808_REG_CONFIG_WINLOCKED = 0x0040
MCP9808_REG_CONFIG_INTCLR = 0x0020
MCP9808_REG_CONFIG_ALERTSTAT = 0x0010
MCP9808_REG_CONFIG_ALERTCTRL = 0x0008
MCP9808_REG_CONFIG_ALERTSEL = 0x0002
MCP9808_REG_CONFIG_ALERTPOL = 0x0002
MCP9808_REG_CONFIG_ALERTMODE = 0x0001
MCP9808_REG_CONFIG = 0x01
MCP9808_REG_UPPER_TEMP = 0x02
MCP9808_REG_LOWER_TEMP = 0x03
MCP9808_REG_CRIT_TEMP = 0x04
MCP9808_REG_AMBIENT_TEMP = 0x05
MCP9808_REG_MANUF_ID = 0x06
MCP9808_REG_DEVICE_ID = 0x07

class MCP9808(object):

    def __init__(self, address=MCP9808_I2CADDR_DEFAULT, busnum=-1):
        self._i2c = Adafruit_I2C(address=address, busnum=busnum)

        self._address = address

        # Assert it's the right thing
        if self._readU16(MCP9808_REG_MANUF_ID) != 0x0054:
            logger.error('Not right manufacturer (0x54): %s' % val)
        if self._readU16(MCP9808_REG_DEVICE_ID) != 0x0400:
            logger.error('Not right device ID (0x4): %s' % val)

    def _readU16(self, reg):
        ret = self._i2c.readList(reg, 2)
        print ret
        return (ret[0] << 8) + ret[1]


    def read_temp_c(self):

        t = self._readU16(MCP9808_REG_AMBIENT_TEMP)
        temp = t & 0x0FFF
        temp /= 16.0
        if t & 0x1000: temp -= 256

        #val = self._i2c.reverseByteOrder(self._i2c.readU16(0x05))
        #temp = val & 0x0FFF
        #sign = val & 0x1000
        #temp /= 16.0
        #if sign:
        #    temp *= -1

        return temp

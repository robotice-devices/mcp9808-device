
import logging

from Adafruit_I2C import Adafruit_I2C

logger = logging.getLogger("MCP9808")

class MCP9808(object):

    def __init__(self, address=0x18):
        self._i2c = Adafruit_I2C(address)
        self._address = address

        # Assert it's the right thing
        val = hex(self._i2c.reverseByteOrder(self._i2c.readU16(0x06)))
        print val
        if val != 0x54:
            logger.warning('Not right manufacturer (0x54): %s' val)
#        assert val == 0x54, 'Not right manufacturer'
        val = hex(self._i2c.reverseByteOrder(self._i2c.readU16(0x07)))
        print val
#        assert val == 0x4, 'Not right device ID'

    def read_temp_c(self):
        val = self._i2c.reverseByteOrder(self._i2c.readU16(0x05))
        temp = val & 0x0FFF
        sign = val & 0x1000
        temp /= 16.0
        if sign:
            temp *= -1
        return temp

    def read_temp_f(self):
        return self.read_temp_c() * 9.0/5.0 + 32

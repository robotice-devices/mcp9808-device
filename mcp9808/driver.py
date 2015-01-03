#!/srv/robotice/bin/python

import sys
from oslo.config import cfg
from oslo.config import types

try:
    import sensor
except Exception, e:
    raise e

common_opts = [
    cfg.Opt('name',
            short='n',
            default="mcp9808",
            help='Sensor name'),
#    cfg.Opt('bus',
#            short='b',
#            default="1",
#            help='I2C bus'),
    cfg.Opt('bus',
            short='a',
            default="0x18",
            help='I2C address'),
]

CONF = cfg.CONF
CONF.register_cli_opts(common_opts)
CONF(sys.argv[1:])

print(sensor.get_data(CONF))

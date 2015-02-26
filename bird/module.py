from osv.modules import api

default = api.run(cmdline="/bird.so -c /bird.conf -P bird.pid -f")

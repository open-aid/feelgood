#!/usr/bin/env python

PORT = 9000


import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'feelgood.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

from socketio import SocketIOServer

if __name__ == '__main__':
    print 'Listening on port %s and on port 843 (flash policy server)' % PORT
    SocketIOServer(('', PORT), application, namespace="socket.io").serve_forever()

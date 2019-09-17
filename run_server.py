"""
A simple Flask application calling
"""

import argparse

from sys import exit as sys_exit
from app_service import app


def run_with_twisted(port, debug_mode):
    """
    Import twisted dependencies, set app as WSGIResource and start reactor.
    """
    try:
        from twisted.internet import reactor
        from twisted.web.server import Site
        from twisted.web.wsgi import WSGIResource
    except ImportError:
        print(
            'ERROR: twisted is not installed in this environment,'
            ' Please install appropriate version of twisted and try again.')
        sys_exit(1)
    print(('Twisted on port {port} ...'.format(port=port)))
    app.debug = debug_mode
    resource = WSGIResource(reactor, reactor.getThreadPool(), app)
    site = Site(resource)
    reactor.listenTCP(port, site, interface="0.0.0.0")
    reactor.run()


def main():
    """
    Parse the options to get WSGi container of choice, the debug mode, and the port number"
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', type=int, default=8005)
    parser.add_argument('--debug', default=True)
    args = parser.parse_args()
    run_with_twisted(args.port, args.debug)


if __name__ == '__main__':
    main()
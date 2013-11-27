#!/usr/bin/env python2.7
'''
SSH interceptor and logger.
See --help for usage.
'''

from twisted.internet import reactor
import sys

sys.path.append('../lib')
import mitmproxy
import logging

def main():
    '''
    Parse options, open log and start proxy server
    '''
    (opts, _) = mitmproxy.ssh_proxy_option_parser(22, 2222)

    if opts.debug:
        logging.basicConfig(filename='ssh.log',
                    filemode='w',
                    format='%(levelname)s:%(message)s',
                    level=logging.DEBUG)

    sys.stderr.write(
        'Server running on localhost:%d...\n' % (opts.localport))

    factory = mitmproxy.SSHServerFactory(opts)
    reactor.listenTCP(opts.localport, factory)
    reactor.run()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(0)

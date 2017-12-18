
import urllib.request
import socket
# timeout in seconds
timeout = 2
socket.setdefaulttimeout(timeout)
# this call to urllib.request.urlopen now uses the default timeout
# we have set in the socket module

class HtmlDownloader(object):

    def downloader(self, url):
        if url is None:
            return None

        response =  urllib.request.urlopen(url)
        return response.read()
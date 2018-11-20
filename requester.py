import urllib.parse
import urllib.request

class Requester(object):
    """Call/Response operations"""
    def __init__(self, url, params):
        self.url = url
        self.params = params

    def params_for_call(self):
        """Prepare params for the call"""
        # params should be url encoded
        #  data should be bytes for POST
        self.params = urllib.parse.urlencode(self.params).encode('ascii')
        return self.params

    def make_call(self):
        """"Make a call to NC api and returns the response"""
        self.req = urllib.request.Request(self.url, self.params_for_call())
        return self.req

    def get_response(self):
        """ Read the response and return it as a string """
        with urllib.request.urlopen(self.make_call()) as response:
            the_page = response.read()
            return the_page
import urllib.parse
import urllib.request

class Requester(object):
    """Call/Response operations"""
    def __init__(self, url, params):
        self.url = url
        self.params = params

    def param_ready(self): # func name should be 'what func does' or 'what it gives back'
        """Prepare params for the call"""
        # add .encode('ascii') after urlencode call
        self.params = urllib.parse.urlencode(self.params)   # params should be url encoded
        self.params = self.params.encode('ascii')   # data should be bytes for POST
        return self.params

    def api_call(self):
        """Make a call to NC api"""
        self.req = urllib.request.Request(self.url, self.param_ready())
        return self.req

    # this one shows response of NC api
    def show_response(self):  # rename this like 'get response'
        with urllib.request.urlopen(self.api_call()) as response:
            the_page = response.read()
            return the_page
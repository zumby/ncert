# test oop
import urllib.parse
import urllib.request
import yaml
from XMLpars import XMLparser


class Requester(object):
    """Call/Response operations"""
    def __init__(self, url, params):
        self.url = url
        self.params = params

    def param_ready(self):
        """Prepare params for the call"""
        self.params = urllib.parse.urlencode(self.params)   # params should be url encoded
        self.params = self.params.encode('ascii')   # data should be bytes for POST
        return self.params

    def api_call(self):
        """Make a call to NC api"""
        self.req = urllib.request.Request(self.url, self.param_ready())
        return self.req

    # this one shows response of NC api
    def show_response(self):
        with urllib.request.urlopen(self.api_call()) as response:
            the_page = response.read()
            return the_page


class GlobalParams(object):
    """Working with global API params"""
    def __init__(self):
        self.url = "https://api.sandbox.namecheap.com/xml.response"
        self.params = self.get_global_params()

    def get_global_params(self):
        with open('nc_api_config.yaml', 'r') as stream:
            config = yaml.load(stream)
            return config['GlobalParams']


class Interactor(object):
    """Interaction with user and action"""
    def __init__(self):
        self.interact()

    def interact(self):
        print("Hi. This is ncert. Want to know what I can? (y/n)")
        action = input("> ")

        if action == 'y':
            # this is the instance of the Requester class with url and params as the arguments
            call_request = Requester(GlobalParams().url,
                                     GlobalParams().params)
            # this is calling a function call_request() to get the data from request
            api_response = call_request.show_response()  # .decode('utf-8') - for XML tree response
            cert_list = XMLparser(api_response).get_cert_available()
            print(cert_list)
            print(f"I have {len(cert_list)} new certs that I can use, and here are the IDs: \n", cert_list)
        else:
            exit(1)


Interactor()

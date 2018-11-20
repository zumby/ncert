from xml_parse import XMLparser
from requester import Requester
from global_params import GlobalParams


class Interactor(object):
    """Interaction with user and action"""
    def __init__(self):
        self.interact()

    def interact(self):
        print("Hi. This is ncert. Want to know what I can? (y/n)")
        action = input("> ")
        if action == 'y':
            cert_list = self.action_call()
            print(f"I have {len(cert_list)} new certs that I can use, and here are the IDs: \n", cert_list)
        else:
            print("Well, good bye then!")
            exit(1)

    def action_call(self):
        # this is the instance of the Requester class with url and params as the arguments
        call_request = Requester(GlobalParams().url,
                                 GlobalParams().params)  # HOW TO resolve COUPLING here? IDK :(
        # this is calling a function call_request() to get the data from request
        api_response = call_request.get_response()  # .decode('utf-8') - for XML tree response
        cert_list = XMLparser(api_response).get_cert_available()
        return cert_list


Interactor()
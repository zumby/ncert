from xml_parse import *
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
            # this is the instance of the Requester class with url and params as the arguments
            #  сильная сопряженность - почитать. один клас не должен инстанциироваться внутри другого
            call_request = Requester(GlobalParams().url,
                                     GlobalParams().params)
            # this is calling a function call_request() to get the data from request
            api_response = call_request.show_response()  # .decode('utf-8') - for XML tree response
            cert_list = XMLparser(api_response).get_cert_available()
            print(cert_list)
            print(f"I have {len(cert_list)} new certs that I can use, and here are the IDs: \n", cert_list)
        else:
            exit(1)

#  сильная сопряженность - почитать

Interactor()
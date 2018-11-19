import yaml

class GlobalParams(object):
    """Working with global API params"""
    # url = "https://api.sandbox.namecheap.com/xml.response" then you can do like GlobalParams.url to call url value
    def __init__(self):
        self.url = "https://api.sandbox.namecheap.com/xml.response" # think of putting this to yaml
        self.params = self.get_global_params()

    def get_global_params(self):
        with open('nc_api_config.yaml', 'r') as stream:
            config = yaml.load(stream)
            return config['GlobalParams']
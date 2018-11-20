import yaml

class GlobalParams(object):
    """Working with global API params"""
    def __init__(self):
        self.url = self.get_global_params()["URL"]
        self.params = self.get_global_params()["GlobalParams"]

    def get_global_params(self):
        """Returns the dict with th GlobalParams and NC API URL"""
        with open('nc_api_config.yaml', 'r') as stream:
            params_dict = yaml.load(stream)
            # return config['GlobalParams'], config['URL']
            return params_dict
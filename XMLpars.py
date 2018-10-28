# shdw
import xml.etree.ElementTree as ET

class XMLparser(object):


    def __init__(self, response): # receives a response as a string or b'string
        self.response = response
        self.xml_ns = "{http://api.namecheap.com/xml.response}"
        self.ssl_tag = 'SSL'  # name of the tag with SSL details from xml tree
    """Class for parsing NC API response and getting list of certs available for ncert usage"""

    def get_cert_available(self):
        tag = self.xml_ns + self.ssl_tag
        cert_available = []
        # fromstring() parses XML from a string directly into an Element,
        # which is the root element of the parsed tree.
        tree_root = ET.fromstring(self.response)
        for i in tree_root.iter(tag):
            cert_data = i.attrib  # dict with cert data like 'SSLType': 'ev ssl'
            # to get certs we need only
            if (not bool(cert_data['HostName']) and  # if HostName is empty (literally: if not False == True)
                    cert_data['SSLType'] == 'positivessl' and  # non free, positiveSSL only
                    cert_data['IsExpiredYN'] == 'false' and  # non-expired (this is unnecessary but can save from failing)
                    not bool(cert_data['ActivationExpireDate']) and
                    cert_data['Status'] == 'newpurchase' and  # only non-activated certs
                    cert_data['Years'] == '1'):  # only 1year certs

                cert_available.append(cert_data['CertificateID'])  # add ID to list

        return cert_available




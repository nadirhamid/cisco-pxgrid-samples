from pxgrid import PxgridControl
from config import Config
import urllib.request
import base64
import time
import json
import ssl


def apply_policy(config, secret, url, policy, ip_address):
    payload = json.dumps(dict(
        policyName=policy,
        ipAddress=ip_address  
    ))
    print('query url=' + url)
    print('  request=' + payload)
    ctx = config.get_ssl_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    handler = urllib.request.HTTPSHandler(context=ctx)
    opener = urllib.request.build_opener(handler)
    rest_request = urllib.request.Request(url=url, data=str.encode(payload))
    rest_request.add_header('Content-Type', 'application/json')
    rest_request.add_header('Accept', 'application/json')
    b64 = base64.b64encode((config.get_node_name() + ':' + secret).encode()).decode()
    rest_request.add_header('Authorization', 'Basic ' + b64)
    rest_response = opener.open(rest_request)
    print('  response status=' + str(rest_response.getcode()))
    print('  response content=' + rest_response.read().decode())

if __name__ == '__main__':
    config = Config()
    pxgrid = PxgridControl(config=config)
    #policy = "Quarantine_Group"
    policy = input("Please enter the ANC policy:\r\n")
    #ip_address = "192.168.1.60"
    ip_address = input("Please enter the IP address:\r\n")
    while pxgrid.account_activate()['accountState'] != 'ENABLED':
        time.sleep(60)

    # lookup for session service
    service_lookup_response = pxgrid.service_lookup('com.cisco.ise.config.anc')
    service = service_lookup_response['services'][0]
    node_name = service['nodeName']
    url = service['properties']['restBaseUrl'] + '/applyEndpointByIpAddress'

    secret = pxgrid.get_access_secret(node_name)['secret']

    apply_policy(config, secret, url, policy, ip_address)

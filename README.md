# cisco pxgrid examples

in this repo you will find some python examples for working with cisco ISE and the pxgrid REST API/websocket interface. the examples
are basic but should give an idea of how to use python with the cisco ISE and pxgrid interface.

# examples included

- program_1.py

this example shows you how to put a set device into a cisco ISE endpoint group.
- program_2.py

an example that lists the endpoints on a cisco ISE

## installation / setup

1. install PIP requirements
```
pip install -r requirements.txt
```
2. set up authentication
```
openssl pkcs12 -in mycert.p12 -out ./keys/file.key.pem -nocerts -nodes
openssl pkcs12 -in mycert.p12 -out ./keys/file.crt.pem -clcerts -nokeys
```
* for info on how to export a PKCS in ISE please see link 
[Cisco Identity Services Engine Administrator Guide, Release 2.2  - Manage Certificates \[Cisco Identity Services Engine\] - Cisco](https://www.cisco.com/c/en/us/td/docs/security/ise/2-2/admin_guide/b_ise_admin_guide_22/b_ise_admin_guide_22_chapter_0110.html#ariaid-title63)

3. enable pxGrid in cisco ISE
[click here for instructions](https://www.cisco.com/c/en/us/support/docs/security/identity-services-engine-24/214481-configure-ise-2-4-and-fmc-6-2-3-pxgrid-i.html#anc5)

# running examples

in the examples below i am assuming the ISE is running on "ise24198.acme.local" please replace with your own ISE IP.

- example 1
```
python ./program_1.py -a ise24198.acme.local:8910 -w ise24198 -n xRqoa9zHF3YdCXkb -c ./keys/file.crt.pem -k ./keys/file.key.pem -s ./keys/file.crt.pem -p Testtest10
```

- example 2
```
python ./program_2.py -a ise24198.acme.local:8910 -w ise24198 -n xRqoa9zHF3YdCXkb -c ./keys/file.crt.pem -k ./keys/file.key.pem -s ./keys/file.crt.pem -p Testtest10
```

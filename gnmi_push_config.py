# Purpose: [This script pushes static route configs to SRLinux Leaf Routers via gNMI
#
# Author: Muzaffer Kahraman muzaffer.kahraman@outlook.com

from pygnmi.client import gNMIclient
from jinja2 import Template
import json

class Srlinux_config:

    def set_nhg_properties(self,name,index,ip_address):
        self.name=name
        self.index=index
        self.ip_address=ip_address
        with open("jinja_templates/next-hop-groups.j2") as f:
            template = Template(f.read())
            set_config=[]
            json_config=template.render(name=self.name,index=self.index,ip_address=self.ip_address)
            set_config=[('network-instance[name=default]', json.loads(json_config))]
            print(set_config)
            return set_config

    def set_static_route_properties(self,prefix,next_hop_group):
        self.prefix=prefix
        self.next_hop_group=next_hop_group
        with open("jinja_templates/static_routes.j2") as f:
            template = Template(f.read())
            set_config=[]
            json_config=template.render(prefix=self.prefix,next_hop_group=self.next_hop_group)
            set_config=[('network-instance[name=default]', json.loads(json_config))]
            return set_config

    def push_config(self,router_ip,config):
        host = (router_ip, '57400')


        with gNMIclient(target=host, username='admin', password='NokiaSrl1!',type="CONFIG") as gc:

            data = gc.set(update=config)
            print(json.dumps(data,indent=4))


if __name__ == "__main__":

    conf=Srlinux_config()

    conf.push_config("172.80.80.11",conf.set_nhg_properties("to_spines",1,"10.1.1.0"))
    conf.push_config("172.80.80.11",conf.set_nhg_properties("to_spines",2,"10.2.1.0"))
    conf.push_config("172.80.80.11",conf.set_static_route_properties("192.168.200.0/24","to_spines"))

    conf.push_config("172.80.80.12",conf.set_nhg_properties("to_spines",1,"10.1.2.0"))
    conf.push_config("172.80.80.12",conf.set_nhg_properties("to_spines",2,"10.2.2.0"))
    conf.push_config("172.80.80.12",conf.set_static_route_properties("192.168.100.0/24","to_spines"))

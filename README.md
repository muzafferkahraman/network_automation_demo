# Network Automation Demo

I prepared this repo to demo how we can implement the configurations on SRLinux Routers via gNMI.
The python code utilizes the pygnmi module, in order to send set operations to push the missing static route configs to the Leaf devices.
After the python code sucessfully pushes the configs, the hosts are going to be able to ping each other

![](schema.JPG)


## Testing connectivity between the hosts
> docker exec -ti host10 ping 192.168.200.15
> docker exec -ti host20 ping 192.168.100.15

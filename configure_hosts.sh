docker exec -ti host10 ip li set dev eth1 mtu 1500
docker exec -ti host10 ip li set dev eth1 address 00:00:00:01:01:00
docker exec -ti host10 ip a add 192.168.100.15/24 dev eth1
docker exec -ti host10 ip route add 192.168.200.0/24 via 192.168.100.5

docker exec -ti host20 ip li set dev eth1 mtu 1500
docker exec -ti host20 ip li set dev eth1 address 00:00:00:01:01:00
docker exec -ti host20 ip a add 192.168.200.15/24 dev eth1
docker exec -ti host20 ip route add 192.168.100.0/24 via 192.168.200.5

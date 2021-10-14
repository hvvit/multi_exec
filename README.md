# multi_exec
Python code to run command on multiple hosts using pssh library

To install requirements
```
pip3 install -r requirements.txt
```

To trigger cli environment
```
python3 main.py
```

sample cli output
```
Enter comma seperated hosts example (username@host1,username@host2): ubuntu@10.113.121.129,ubuntu@10.113.121.50
Enter command to execute: cat /etc/hostname
executing command: 
10.113.121.129 -------------------------------------------------------------------> execution completed
10.113.121.50 -------------------------------------------------------------------> execution completed
print output for (y/n): y
10.113.121.129 -------------------------------------------------------------------> execution completed
10.113.121.129 :: new-machine1
10.113.121.50 -------------------------------------------------------------------> execution completed
10.113.121.50 :: new-machine2
Press (y/n) to start again : y
Enter comma seperated hosts example (username@host1,username@host2): ubuntu@10.113.121.129,ubuntu@10.113.121.50
Enter command to execute: cat /etc/lsb-release
executing command: 
10.113.121.129 -------------------------------------------------------------------> execution completed
10.113.121.50 -------------------------------------------------------------------> execution completed
print output for (y/n): y
10.113.121.129 -------------------------------------------------------------------> execution completed
10.113.121.129 :: DISTRIB_ID=Ubuntu
10.113.121.129 :: DISTRIB_RELEASE=20.04
10.113.121.129 :: DISTRIB_CODENAME=focal
10.113.121.129 :: DISTRIB_DESCRIPTION="Ubuntu 20.04.3 LTS"
10.113.121.50 -------------------------------------------------------------------> execution completed
10.113.121.50 :: DISTRIB_ID=Ubuntu
10.113.121.50 :: DISTRIB_RELEASE=20.04
10.113.121.50 :: DISTRIB_CODENAME=focal
10.113.121.50 :: DISTRIB_DESCRIPTION="Ubuntu 20.04.3 LTS"
Press (y/n) to start again : n
```

# METIS
====
# Overview
METIS is a software package with vrious algorithms for dividing graphs.

## Install
```Bash:console
wget http://glaros.dtc.umn.edu/gkhome/fetch/sw/metis/metis-5.1.0.tar.gz  
tar zxfv metis-5.1.0.tar.gz  
cd metis-5.1.0/build  
cmake ../  
make config shared=1  
make && make install  
export PATH=/usr/local/lib:$PATH  
export LD_LIBRARY_PATH=/usr/local/lib/  
python3 -m pip install metis  
```

## Input File
[node id1] [node id2] [weight]
ex) 1 2 5
represent node 1 has an edge at node 2, its weight is 5.

## Usage
python3 metis.py [Input File] [node number] [partition number]

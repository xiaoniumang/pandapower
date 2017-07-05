# pandapower
ieee 33 bus and 69 bus system modelling

Network modelling use the Python package pandapower, which can be found at https://pypi.python.org/pypi/pandapower

The network model data (IEEE 33 bus and 69 bus) are retrieved from the paper "A new approach for optimum simultaneous multi-DG distributed generation Units placement and sizing based on maximization of system loadability using HPSO (hybrid particle swarm optimization) algorithm"
The url link of the paper is http://www.sciencedirect.com/science/article/pii/S0360544213010943
The raw data(two txt files) have been uploaded in this repository

The process_ieee_txt_data.py is the python script to read, restruct and add the column names to the raw data from txt files
The build_ieee_cases.py is the python script to build the IEEE 33 Bus distirbuiton system and IEEE 69 Bus distribution system. 

The power flow analysis can be performed by the pandapower package with the command: pandapower.runpp(net)
It should be noted that the net is the net model built by the python script

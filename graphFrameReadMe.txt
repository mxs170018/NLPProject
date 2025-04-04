I ran this code on databricks community edition,

to do so I started a cluster
then I had to go to https://spark-packages.org/package/graphframes/graphframes to download the spark jar and deploy it to my cluster.

I then uploaded the Slashdot0902 to the dbfs 

afterwards I simply pip installed the libraries that were left and ran the rest of the cells 

to get the connect to work I had to add a checkpoint directory, which is already done in the notebook


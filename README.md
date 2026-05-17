# Knight-LP
Obj: Shortest path for a knight on a chessboard between two given squares on an 8x8 chessboard, A and B.

Solution:
Represent all Squares on the lattice as 64 Xi,j binary variables. 

Constraints: 
Knight has to be able to physically transverse said path.

Create a neighbors set for all neighboring squares knight move wise to every square. 

1- For the Start Points A and B: They only have one neighboring Point, so sum of Neighboring variables = 1.

For the any point on the lattice: If the knight were to tread on it that implies, the knight has to enter it from a neighbor and then leave to a neighbor. 
That implies it would need atleast two neighboring 1s so to speak.
Or it would be a 0 then the neighbors could be anything.

2- for all i,j out of (1,8)
Sum(NeighborsofXi,j) >=  2*xi,j

That'it, thanks for the read ^^.






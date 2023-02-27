# mybots

This program was created using r/ludobots and pyrosim.

Running the program:

1. Navigate to GitHub Desktop or download a zip of the files in the branch morphology1

2. Open the zipped file or navigate to the folder directed (catherg/mybots) on your terminal

3. Confirm you are in a branch called "morphology1" on your terminal

4. Run the program with the command: "python3 search.py"


Randomization, Sensors, and Fitness Function:

  The fitness function uses the random parent weights produced, and makes a replication of the random weights produced and mutates these weights
in the children array. These children weights are then compared with the parent weights, to produce an optimal result, which is the largest value. 

  The colors were chosen based on the function rand.randint. This function was called to either produce a 1 or 0 when every cube was created in the function create_body. If the number turned out to be a 1, then the cube would be green, and if the number turned out to be 0, the cube would be blue.
  
  The random sensor placement was also done by the function rand.randint, correlated to how the colors were chosen as well. If the random number was 1 then the cube would have a sensor neuron, otherwise there would be no sensor neuron in that cube.

Creation of The Body:
I chose to completely randomize the creation of the body. I chose for the first cube always be positioned at 0,0 on the x and y axis. I also randomized the placement of all the other cubes so that they could be on either the x, y, and z axis. I always placed the joint in the middle of the cube, but when placing a new joint I took a random joint from the preexisting ones to work off.

<img src="https://user-images.githubusercontent.com/116319364/221629528-a11f489a-dd9d-4d8f-8d5f-2aabd23d1264.jpg" width="300" height="400">
Credit for the diagram goes to Karl Sims

Creation of The Brain:

<img src="https://user-images.githubusercontent.com/116319364/221629877-212c1f8d-d8ef-4717-88af-95945cbe35bb.jpg" width="300" height="400">
Credit for the diagram goes to Karl Sims

Body Mutation:
The Body mutates by by taking a random number of 0 or 1, and if the number turns out to be 1 then the body adds another cube at a random spot, almost like adding another leg.

Morphospace:
The movements that seem to be possible with this creature are primarily with jumping and "marching to the beat". If the creature had more support on the lower half of its body it would be able to move forward better and potentailly be more stable and jump higher. It seems like the more sensor neurons are concentrated in an area, the more movement that area has.

There are many brains which are possible based on the cubes that become sensor neurons. The brain and synpases are based off of the amount of sensor neurons the random function decides to generate. There could be a type of brain where everything has a synapse and can faciliate movement, and there can also be a type of brain with no synpases or movement. With what I have observed, it seems that there is a sensor that can affect a motor on the other side of the body, a sensor can definitly impact different parts of the body but to have a noticeable effect that depend on the sizing of the cubes.

Optimization Results/Observed Behavior:

The optimization results were that the creature jumped more, usually higher as well. And with this jumping the creature also started moving a bit.
  
Ex.
<img width="600" alt="A8_screenshot" src="https://user-images.githubusercontent.com/116319364/221630175-30ac4c45-940b-42ae-ac1a-9cf79a94d699.png">


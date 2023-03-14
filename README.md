# mybots

This program was created using r/ludobots and pyrosim.

Running the program:

1. Navigate to GitHub Desktop or download a zip of the files in the branch final1

2. Open the zipped file or navigate to the folder directed (catherg/mybots) on your terminal

3. Confirm you are in a branch called "final1" on your terminal

4. Run the program with the command: "python3 search.py"

5. The best performing body and brain is saved in this repository as experiment1_body(givenID), experiment1_brain(givenID), etc.

6. If needed, run the best performing body in each experiment using these files (delete the "experiment1_" tag in the name before you run it)
        - These files can be run in solution and parallelhillclimber


Randomization, Sensors, and Fitness Function:

  The fitness function uses the random parent weights produced, and makes a replication of the random weights produced and mutates these weights
in the children array. These children weights are then compared with the parent weights, to produce an optimal result, which is the largest value. 

  The colors were chosen based on the function rand.randint. This function was called to either produce a 1 or 0 when every cube was created in the function create_body. If the number turned out to be a 1, then the cube would be green, and if the number turned out to be 0, the cube would be blue.
  
  The random sensor placement was also done by the function rand.randint, correlated to how the colors were chosen as well. If the random number was 1 then the cube would have a sensor neuron, otherwise there would be no sensor neuron in that cube.

Creation of The Body:

I chose to completely randomize the creation of the body. I chose for the first cube always be positioned at 0,0 on the x and y axis. I also randomized the placement of all the other cubes so that they could be on either the x, y, and z axis. I always placed the joint in the middle of the cube, but when placing a new joint I took a random joint from the preexisting ones to work off.

<img src="https://user-images.githubusercontent.com/116319364/221641885-144c637e-0953-434d-890f-070659fdbc1c.jpg" width="500" height="400">
Credit for the diagram goes to Karl Sims

Creation of The Brain:

<img src="https://user-images.githubusercontent.com/116319364/221642016-710c990e-ed7f-4558-a42d-a227d7093e29.jpg" width="500" height="400">
Credit for the diagram goes to Karl Sims



Body Mutation:

The Body mutates by by taking a random number of 0 or 1, and if the number turns out to be 1 then the body adds another completely randomized cube at a random axis and cube onto the body.

Morphospace:

The movements that seem to be possible with this creature are primarily with jumping and "marching to the beat". If the creature had more support on the lower half of its body it would be able to move forward better and potentailly be more stable and jump higher. It seems like the more sensor neurons are concentrated in an area, the more movement that area has.

There are many brains which are possible based on the cubes that become sensor neurons. The brain and synpases are based off of the amount of sensor neurons the random function decides to generate. There could be a type of brain where everything has a synapse and can faciliate movement, and there can also be a type of brain with no synpases or movement. With what I have observed, it seems that there is a sensor that can affect a motor on the other side of the body, a sensor can definitly impact different parts of the body but to have a noticeable effect that depend on the sizing of the cubes.

Optimization Results/Observed Behavior:

The optimization results were that the creature moved and wiggled more. With the wiggling and the small jumps, the creature was able to travel further back compared to when was completely randomized.
  
Ex.
<img width="261" alt="experiment1_pic" src="https://user-images.githubusercontent.com/116319364/224860467-9a49f74a-09cd-4c0d-9f7d-2ddccf9d1211.png">


Fitness Curves:

Experiment 1 Fitness Curve:

This curve shows the results of the first experiment, where the number of joints was restricted to 15, meaning the creature could not be comprised of over 16 cubes. This experiment was run for 300 generations and the best fitness value of each generation was plotted.

<img width="800" alt="experiment 1" src="https://user-images.githubusercontent.com/116319364/224845913-8adf79f3-2738-4253-ab26-cead541e54d9.png">

Experiment 2 Fitness Curve:

This curve shows the results of the second experiment, where the number of joints was restricted to 20, meaning the creature could not be comprised of over 21 cubes. This experiment was run for 150 generations and the best fitness value of each generation was plotted.

<img width="800" alt="experiment 2" src="https://user-images.githubusercontent.com/116319364/224845951-ada73b27-7c82-40a4-b0e5-d887c09c840c.png">

Experiment 3 Fitness Curve:

This curve shows the results of the third experiment, where there was no restrictions on the number of cuves or joints that the creature could possess. This experiment was run for 100 generations and the best fitness value of each generation was plotted.

<img width="800" alt="experiment 3" src="https://user-images.githubusercontent.com/116319364/224845966-e8a1a313-ec0b-43e3-b9ee-d8ffbbf525f8.png">

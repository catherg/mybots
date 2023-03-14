# CS 396: Final Project (Science Option, 16pts)

This program was created using r/ludobots and pyrosim.

Running the program:

1. Navigate to GitHub Desktop or download a zip of the files in the branch final1

2. Open the zipped file or navigate to the folder directed (catherg/mybots) on your terminal

3. Confirm you are in a branch called "final1" on your terminal

4. Run the program with the command: "python3 search.py"

5. The best performing body and brain is saved in this repository as experiment1_body(givenID), experiment1_brain(givenID), etc.

6. If needed, run the best performing body in each experiment using these files (delete the "experiment1_" tag in the name before you run it)
        - These files can be run in solution and parallelhillclimber

Note about running the program: If there are issues with the fitness value being read, run it again and it should be read fine (this error occurs sometimes when running a large number of generations)

Experiment/How I tested it: 

The task of the creature is to march to the beat, meaning that they will be walking with small wiggles and jumps in between steps. As the generations continue, the creature will randomly mutate by a random cube being added to any axis, and the brain then adding this neuron. 
        
I will be conducting three experiments and determining under which experiment the creature performs the best in. The first experiment contains a population size of 10 and a total of 300 generations, in the first experiment the creature cannot spawn more than 15 cubes. The second experiment contains a population size of 10 and a total of 150 generations, and in this experiment the creature cannot spawn more than 20 cubes. The last experiment contains a population size of 10 over 100 generations, and in this experiment the creature can spawn as many cubes as it is able to.
        
After calculating the time it takes to produce one simulation(~30 seconds), it wasn't plausible for me to produce 50,000 simulations, so instead of doing a total of 500 generations over 10 seeds I made the constant of each experiment time. After experimenting with the time needed to run each simulation for the different experiments, I chose to have each experiment take 8 hours to run. Another constant in these experiments is the population size, which always stays at 10. Since I will only be doing three experiments, I used 3 seeds, one for each experiment.

I tested these experiments by making the body mutate (look at "Body and Brain Mutation" Section, line 64) randomly every generation. The control experiment in this case was experiment 1, which restricted the robot to have 16 joints. I did this by inserting this piece of code:
<img width="209" alt="control_experiment" src="https://user-images.githubusercontent.com/116319364/224863503-4de32fb3-1bda-4ec1-9c3a-5c40f039c278.png">

These two lines made it so that if the robot was at the largest size possible, it would completely skip over the mutation of the body and not change anything. I made this into my control experiment because I isolated the variable of interest which was the number of cubes.

The inspiration for this experiment came from and question I had about how robots of different sizes could complete certain tasks, and what the optimal size and mutation for the body would be to complete a simple task like walking or "marching to the beat".

/********* DRAW A PICTURE OF THIS EXPERIMENT

Hypothesis:

I believe that the first experiment with a restriction on 15 cubes will perform the task the best. This is because I believe 15 cubes is enough for the sensors and the brain to have optimal control when doing this task. Once the creature gets larger and gains more cubes. It would become too heavy and chaotic to march to the beat very well.


Randomization, Sensors, and Fitness Function:

  The fitness function uses the random parent weights produced, and makes a replication of the random weights produced and mutates these weights
in the children array. These children weights are then compared with the parent weights, to produce an optimal result, which is the largest value. 

  The colors were chosen based on the function rand.randint. This function was called to either produce a 1 or 0 when every cube was created in the function create_body. If the number turned out to be a 1, then the cube would be green, and if the number turned out to be 0, the cube would be blue.
  
  The random sensor placement was also done by the function rand.randint, correlated to how the colors were chosen as well. If the random number was 1 then the cube would have a sensor neuron, otherwise there would be no sensor neuron in that cube.

Creation of The Body:

I chose to completely randomize the creation of the body. I chose for the first cube always be positioned at 0,0 on the x and y axis. I also randomized the placement of all the other cubes so that they could be on either the x, y, and z axis. I always placed the joint in the middle of the cube, but when placing a new joint I took a random joint from the preexisting ones to work off.

<img src="https://user-images.githubusercontent.com/116319364/224866465-de44f1f3-fd98-4b50-8a33-85560598d993.jpg" width="500" height="400">

Credit for the diagram goes to Karl Sims

Creation of The Brain:

<img src="https://user-images.githubusercontent.com/116319364/224868684-113d2e00-5dc3-4223-bb8a-bd7b3dc509a9.jpg" width="500" height="300">



Credit for the diagram goes to Karl Sims


Body and Brain Mutation:

The Body mutates by by taking a random number of 0 or 1, and if the number turns out to be 1 then the body adds another completely randomized cube at a random axis and cube onto the body.

<img src="https://user-images.githubusercontent.com/116319364/224866129-f5f47402-1cab-439b-aa1c-d2110ef8786a.jpg" width="500" height="400">

Morphospace:

The movements that seem to be possible with this creature are primarily with jumping and "marching to the beat". If the creature had more support on the lower half of its body it would be able to move forward better and potentailly be more stable and jump higher. It seems like the more sensor neurons are concentrated in an area, the more movement that area has.

There are many brains which are possible based on the cubes that become sensor neurons. The brain and synpases are based off of the amount of sensor neurons the random function decides to generate. There could be a type of brain where everything has a synapse and can faciliate movement, and there can also be a type of brain with no synpases or movement. With what I have observed, it seems that there is a sensor that can affect a motor on the other side of the body, a sensor can definitly impact different parts of the body but to have a noticeable effect that depend on the sizing of the cubes.

Process of Selection:

<img src="https://user-images.githubusercontent.com/116319364/224873671-543bfc69-4206-4de2-af83-e3840eec80f6.jpg" width="530" height="600">

/**** explain process of selection ***/////

Optimization Results/Observed Behavior:

The optimization results were that the creature moved and wiggled more. With the wiggling and the small jumps, the creature was able to travel further back compared to when was completely randomized.
  
Ex.
<img width="261" alt="experiment1_pic" src="https://user-images.githubusercontent.com/116319364/224860467-9a49f74a-09cd-4c0d-9f7d-2ddccf9d1211.png">

(Picture was taken from the creature produced in experiment 1)


Fitness Curves:

Experiment 1 Fitness Curve:

This curve shows the results of the first experiment, where the number of joints was restricted to 15, meaning the creature could not be comprised of over 16 cubes. This experiment was run for 300 generations and the best fitness value of each generation was plotted.

<img width="550" alt="experiment 1" src="https://user-images.githubusercontent.com/116319364/224845913-8adf79f3-2738-4253-ab26-cead541e54d9.png">

Experiment 2 Fitness Curve:

This curve shows the results of the second experiment, where the number of joints was restricted to 20, meaning the creature could not be comprised of over 21 cubes. This experiment was run for 150 generations and the best fitness value of each generation was plotted.

<img width="550" alt="experiment 2" src="https://user-images.githubusercontent.com/116319364/224845951-ada73b27-7c82-40a4-b0e5-d887c09c840c.png">

Experiment 3 Fitness Curve:

This curve shows the results of the third experiment, where there was no restrictions on the number of cuves or joints that the creature could possess. This experiment was run for 100 generations and the best fitness value of each generation was plotted.

<img width="550" alt="experiment 3" src="https://user-images.githubusercontent.com/116319364/224845966-e8a1a313-ec0b-43e3-b9ee-d8ffbbf525f8.png">

Final Results:
/*** Write your final results ***/

Teaser Gif: https://youtu.be/vaGEQaG1vvg

2 Minute Video:

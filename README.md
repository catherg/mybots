# mybots

This program was created using r/ludobots and pyrosim.

Running the program:

1. Navigate to GitHub Desktop or download a zip of the files in the branch 3Dcreature

2. Open the zipped file or navigate to the folder directed (catherg/mybots) on your terminal

3. Confirm you are in a branch called "3Dcreature" on your terminal

4. Run the program with the command: "python3 search.py"


Colors, Randomization, Sensors, and Fitness Function:

  The fitness function uses the random parent weights produced, and makes a replication of the random weights produced and mutates these weights
in the children array. These children weights are then compared with the parent weights, to produce an optimal result. At the end after generations
are run, the fitness is the smallest value. 

  The colors were chosen based on the function rand.randint. This function was called to either produce a 1 or 0 when every cube was created in the function create_body. If the number turned out to be a 1, then the cube would be green, and if the number turned out to be 0, the cube would be blue.
  
The random sensor placement was also done by the function rand.randint, correlated to how the colors were chosen as well. If the random number was 1 then the cube would have a sensor neuron, otherwise there would be no sensor neuron in that cube.

I chose the general shape of a dog to randomize. The shape of a dog included a torso, 4 legs, and a head. I then randomized the positioning and ranges 
that the sizes of all these cubes could be.

Creation of The Body:

<img src="https://user-images.githubusercontent.com/116319364/219972065-47377102-4417-40ab-883f-358fbdbd8ca0.jpg" width="300" height="400">

Creation of The Brain:

<img src="https://user-images.githubusercontent.com/116319364/219972069-214e1e26-ca3a-4011-ac97-507f4bf83f58.jpg" width="300" height="400">

Morphospace:
The movements that seem to be possible with this creature are primarily in the legs. The dog could hop up occasionally, but the height of the jump depends on the sizing of the torso and the head. The legs can move forward and backward and right and left. If these legs were large enough to fully support the torso and head they would move the dog forward. The body shapes are randomized to where the legs could be either very thin and tall to very wide and short. The torso and head can also be extremely large or smaller, and either a rectangle or a square.

There are many brains which are possible based on the cubes that become sensor neurons. The brain and synpases are based off of the amount of sensor neurons the random function decides to generate. There could be a type of brain where everything has a synapse and can faciliate movement, and there can also be a type of brain with no synpases or movement. With what I have observed, it seems that there is a sensor that can affect a motor on the other side of the body, a sensor can definitly impact different parts of the body but to have a noticeable effect that depend on the sizing of the cubes.

Optimization Results/Observed Behavior:

  The optimization results were that the legs of the dog moved a bit. Many times, because the randomization the torso and head were too heavy for the legs, so the dog typically did not get very far. But when optimized, the dog seemed to marching and trying to move around. The observed behavior ended up being that after iterating through the population size and generations both set to 8, the dog would stay in place, but be moving its legs forward and back and hop a bit.
  
Ex.
<img width="301" alt="Screen Shot 2023-02-19 at 2 20 01 PM" src="https://user-images.githubusercontent.com/116319364/219973178-c1accca1-6f82-44e1-937b-1287eaa488e7.png">

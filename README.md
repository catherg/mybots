# mybots

Running the program:

1. Navigate to GitHub Desktop or download a zip of the files in the branch jointedsnake1

2. Open the zipped file or navigate to the folder directed (catherg/mybots) on your terminal

3. Confirm you are in a branch called "jointedsnake1" on your terminal

4. Run the program with the command: "python3 search.py"


Colors, Sensors, and Fitness Function:

  The fitness function uses the random parent weights produced, and makes a replication of the random weights produced and mutates these weights
in the children array. These children weights are then compared with the parent weights, and if the children weights are larger than the parent weights
then they replace the value in the parent array. At the end after generations are run and the final simulation is being produced, the fitness for the
final simulation is chosen by finding the largest fitness value in the whole parent array. 

  The colors were chosen based on the function rand.randint. This function was called to either produce a 1 or 0 when every cube was created in the function create_body. If the number turned out to be a 1, then the cube would be green, and if the number turned out to be 0, the cube would be blue.
  
  The random sensor placement was also done by the function rand.randint. There was first an empty sensor dictionary declared and then if the random
number was 1 then the cube created would have a sensor neuron and its information would be added to the sensor dictionary. If the number was 0 then
there would be no sensor neuron in that cube.


Optimization Results:

  The optimization results seemed to be that the ends of the snake were most impacted. With no optimization and evolution the snake seemed to just stay flat for longer and the ends didn't move. This then meant that the snake was not in a U-shape and didn't really rock back and forth like when it was optimized. The optimization changed how the snake moved and altered where the snake ended up in the simulation since it changed the snakes movement.



Observed Behavior:

  The observed behavior ended up being that after iterating through the population size and generations both set to ten, the snake would first go up in
the air and then either end of the snake would turn upward as well. And the snake would rock back and forth once both of its ends turned upward.

Ex.
<img width="576" alt="Screen Shot 2023-02-11 at 2 57 48 PM" src="https://user-images.githubusercontent.com/116319364/218281220-2ec1a398-50df-4b3d-b0ce-95db3e756090.png">

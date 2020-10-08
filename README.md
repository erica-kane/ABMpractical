# ABMpractical

## Introduction

This repo contains the appropriate files to run 2 models, a base model and an enhancement.

## Contents

This project contains two models and associated frameworks.
Both models require an [environment file](in.txt).

### Base model
- [agentframework.py](agentframework.py)

  Defines the Agent class that is used in the model.

- [model.py](model.py)

  Sets up and runs the model:
    
    1. Loads the environment.
    2. Scrapes the initial agent locations.
    3. Runs the model inside of a GUI.
    4. Writes to the store file.

### Enhanced model
- [enhancedframework.py](agentframework.py)

  Defines the Agent class and the Sheep and Pred subclasses that are used in the model.

- [enhancedmodel.py](model.py)

  Sets up and runs the model. Note that this doesn't run in a GUI.

## Running the model

### Base model

```
python model.py
```

When running this model, you should see a GUI window pop up, with a drop down menu, 'Model', allowing you to run the model.
This drop down may require you to go to another window then come back to it before it works.

After selecting 'Run Model' on the drop down menu, you should expect to see 20 agents plotted on a 300x300 'environment'.
The agents will be initialised randomly, causing them to change colour each turn. They will also move randomly, and when they reach the perimeters of the plot they will wrap round the other side. 
You should see changes in the environment around the path of the agents, as they take from (eat) and give back to (sick) the environment after each movement. At the end of the running proccess (which will run for 100 iterations) a file will be written called storefile, containing the sum of all the agents' stores (the amount they have taken from the environment by the last iteration). 

### Enhanced model

```
python enhancedmodel.py
```

When running this model, an animation should pop up and start running automatically (there is no GUI). 

You should expect to see 20 Sheep (white circles) and 10 Preds (black triangles). The Sheep should move randomly like the agents in the first model, 'eating' the environment as they move and adding to their store, but instead of being sick they stop when they're full (store 200). The Preds make a distance calculation between themsleves and each Sheep, moving towards the closest one until they land on the same spot. They will then eat the Sheep, taking the contents of its store into their own, and the Sheep dies. Both classes are plotted based on store size, so as the Sheep eat and the Preds hunt, the points should increase in size. 

To simulate a more realistic representation of reality, the agents in this model no longer wrap round the perimeter, but bounce off the edges. This is a closer representation to what would happen in an actual field with a physical perimeter. 

## License
This project is licensed under the [MIT License](LICENSE).

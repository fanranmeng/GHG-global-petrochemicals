# Greenhouse gas emissions from global petrochemical production 
This repository contains code and data relating to the petrochemical emissions model, principally related to the C-THRU project (https://www.c-thru.org/). This README describes how the model is structured. 


## Installation

### Windows

The instructions in this section instead install everything needed to run the code etc on Windows.

Prerequisites:
1. Download the Visual Studio build tools for Python 3 ([download](https://visualstudio.microsoft.com/thank-you-downloading-visual-studio/?sku=BuildTools&rel=16), [install instructions](https://drive.google.com/file/d/0B4GsMXCRaSSIOWpYQkstajlYZ0tPVkNQSElmTWh1dXFaYkJr/view?usp=sharing)).
   - Version 2017 recommended for compatibility with Python; if you already have used version 2019 and it works fine please update here.

2. Install [git for Windows](https://git-scm.com/download/win).



#### Installing Python

The simplest way is to install the necessary version of Python directly:
- [Python 3.9](https://www.python.org/downloads/release/python-39/)
- When installing, select the option to "add to PATH"
- If installing Python this way, you can use any terminal to run the commands below (e.g. Powershell, or git-bash).

Alternatively, if you are already using Conda, you can use it to get the correct version of Python.
- If using Conda, all the commands below should be in the "miniconda prompt" or "anaconda prompt"
- Create a Conda environment with the correct version of Python:
  ```shell
  conda create -n py39 python==3.9.*
  ```
  Don't "activate" the environment now.

Either way, we then need to [install Pipenv](https://pipenv.pypa.io/en/latest/#install-pipenv-today), which manages all the dependencies of the code to get the correct versions installed. The simplest way is to run `pip install pipenv`.



## Project structure

Pipeline - data_extraction -> data_processing -> data_combination -> analysis -> analysis_outputs

1. Data extraction\
Code for extracting data from ICIS, IHS, and LCA databases.

2. Data processing\
Code for transforming data into consistent units.

3. Data combination\
Code for assembling data sources\
  i. IHS material mass + LCA database conversion factors -> IHS material emissions\
  ii. IHS material emissions allocation -> IHS process emissions\
  iii. IHS process emissions + ICIS production -> ICIS emissions\
  
4. Data analysis\
Code for generating outputs\
  i. Compare emissions for the same product via different IHS processes\
  ii. Calculate emissions saving potential for plant or range of plants\
  iii. Create a map of petrochemical emissions as an inventory\
  iv. Codes for generating all figures in the paper\


# Contacts
lshc3@cam.ac.uk; f.meng@sheffield.ac.uk

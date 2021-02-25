# shopping-cart
Navigate to the shopping-cart repository from your local Git Hub Desktop client in the command line [ex: Git Bash, Command Prompt, etc.]. The below code is an example, so make sure it reflects your depository's unique address.

`cd ~/Desktop/GitHub/shopping-cart`


#Setting up the environment

The first time you run this app (and only the first time), you need to create a new environment and name it (e.g. my-shopping-env)

`conda create -n my-shopping-env python=3.8`


This code will also install Python 3.8 into this new environment. To navigate to this environment or return to it in the future, use the below code.

`conda activate my-shopping-env`


When activating the environment for the first time, you have to install the required packages listed in the requirements.txt file in the repository. (You only need to do this the first time you setup this environment, and this step is included in the event of a future expansion to the program that necessitates additional required packages.)

`pip install -r requirements.txt`


## Using the shopping cart
To run the shopping cart program, run the below code, and follow the in-game instructions.

`python shopping_cart.py`


Below is a guide to the acceptable user-given inputs in the program:
| Prompt | Acceptable Inputs |
| ----------- | ----------- |
| Please enter your product's unique ID: | Exact syntax of the store's item ID (e.g. 2, 12, 20) | 
| Please enter the number of pounds of {item} | Decimal number or integer |
| Please enter another unique product ID or enter 'done' to review your cart: | done, exact syntax of the store's IDs (e.g. 2, 12, 20) |
| Do you wish to checkout? | yes, no |
| Which change would you like to make? | add, remove |
| Please enter the unique ID of the item you want to remove from your cart: | Exact syntax of the store's  item ID (e.g. 2, 12, 20) |

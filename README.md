# Purchasing Houses using blockchain and streamlit

# Background

Our project aims to allow users to purchase / sell a house using blockchain technoledgey. With our program, people have the option to browse photos of the houses, and other important details like sqft, price, adress, and more. The streamlit userface allows for a simple UI for user to interact with. This program is running on a virutal serivce, allowing anyone to view it by using a web address. 

# Blockchain 

In the package, there is a crypto_wallet.py that is made up of basic blockcahin functions. This file contains all the functions, we inherit, in the main .py file. Using ganache, we are able to test the payment system. Becuase of this, the houses are priced according to how much a Ganache wallet holds.

# Main.py

Due to restrints of the test eviroments wallet, the prices of the houses are much lower than actual. Due to the limitations, we price the house in ETH and within the values we had in our test wallets. Otherwise, we'd price the houses in USD then convert to ETH value for transaction

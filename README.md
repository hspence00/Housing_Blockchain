# Purchasing Houses using blockchain and streamlit

# Background
Our Python project aims to make the process of buying and selling houses more efficient and secure by using blockchain technology. We have created a platform that allows users to list their properties for sale and browse available listings.
This is a basic demonstration on how blockchain technoledgey can be a payment solution for buying and selling homes. Using blockchain for payment gives the users more security, decentralization, and cost efficency. 
Once the conditions of the sale have been met, the platform automatically executes the transfer of ownership and funds on the blockchain.

##
Our project aims to allow users to purchase / sell a house using blockchain technoledgey. With our program, people have the option to browse photos of the houses, and other important details like sqft, price, adress, and more. The streamlit userface allows for a simple UI for user to interact with. This program is running on a virutal serivce, allowing anyone to view it by using a web address. 

# Blockchain 

In the package, there is a wallet.py that is made up of basic blockcahin functions. This file contains all the functions, we inherit, in the main .py file. Using ganache, we are able to test the payment system. Becuase of this, the houses are priced according to how much a Ganache wallet holds.

# housing_streamlit.py

This file is the main file for our repository. This is the file you will run, in the installation quide bellow. In this file, there are several imports required. Including streamlit and web3, etc. The streamlit website layout is in this file, including the housing database. The Housing database is a self made database using data from zillow. To add a house to the application, one would need to edit lines 58-122, follow the format. This file will also inherent functions from wallet.py, to use blockchain functions in the application. There is also a streamlit_authenticator that is used as a login page. Currently serves no function. Next upgrades will be to add a section page where a person can add their house to the application through the UI.

# Installation Guide
1. Clone repository onto local computer
2. This project requires python and multiple import installs
3. The import install includes:
   streamlit
   web3
   streamlit_authenticator
   yaml
4. Once all ther required libraries are installed, in your terminal, run ;  streamlit run housing_streamlit.py * Skip this step until step 9
5. A pop up should display prompting a local url and a network url. Copy and paste any of them into your browser to view and interact.
6. Next, download ganache. This is the blockchain test network app we use. 
7. After you set up a network, pressing "quick start", copy the mneomic phrase shown towards the top of the screen. 
8. Then go to the wallet.py, and edit line 13, the mneomic variable. Set it to your mneomic phrase.
9. After you set up the ganache, wallet, and import the proper libraries, run the application following step 4

This is the download link for ganache
https://trufflesuite.com/ganache/
# Imports
wallet.py

![Screenshot 2023-01-06 at 6.25.27 PM.png](https://github.com/hspence00/housing_blockchain/blob/main/ReadMe%20Images/Screenshot%202023-01-06%20at%206.25.27%20PM.png)


housing_streamlit.py

![Screenshot 2023-01-06 at 6.25.03 PM.png](https://github.com/hspence00/housing_blockchain/blob/main/ReadMe%20Images/Screenshot%202023-01-06%20at%206.25.03%20PM.png)

# Configuration

The yaml configuration file is used to store username and password data for login credentials. If an incorrect password is entered the user will receive an error message. This function is just a mock-up and only stores a handful of selected usernames for demo purposes. Plans for future advancement include the ability to store crypto wallet ID's along with the usernames.  

# wallet.py

This file does has 3 primary functions, create wallet, send transaction, and view balance. This is all done using the web3 import. We inherent this file into housing_streamlit.py to import those functions for the application. Currently, the wallet is connected to the Ganache test network. In order to use this project properly, you must download the Ganache application first. To configure your ganache wallet to the file, you must edit line 13 mneomic variable to the wallet you create on ganacge.

# Streamlit File

<img width="1440" alt="Screenshot 2023-01-04 at 6 39 32 PM" src="https://user-images.githubusercontent.com/18622578/211123050-fe90e657-b6a3-4dfe-a2d9-b1d9a4bcd75a.png">

Our housing_streamlit file creates a decentralized application (dApp) using Streamlit, where users can purchase and sell homes by selecting a home from the drop down feature.


<img width="323" alt="Screenshot 2023-01-04 at 6 40 36 PM" src="https://user-images.githubusercontent.com/18622578/211123348-cf7f2519-c3f7-4368-9ebe-67bbac02c9ae.png">


Images of the homes available in the database are listed. The app displays the contract address and amount of home. It also provides an efficient and secure payment method with a validated transaction hash.

<img width="328" alt="Screenshot 2023-01-04 at 7 02 29 PM" src="https://user-images.githubusercontent.com/18622578/211123266-9a062d9d-ea0d-4c23-91e2-067623af548c.png">


<img width="1197" alt="Screenshot 2023-01-04 at 7 02 48 PM" src="https://user-images.githubusercontent.com/18622578/211123394-501dcde2-d2ef-4754-b6d5-3a21ffed01ff.png">




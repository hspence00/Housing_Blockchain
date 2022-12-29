# Imports
import streamlit as st
from dataclasses import dataclass
from typing import Any, List
from web3 import Web3
from crypto_wallet import generate_account
from crypto_wallet import get_balance
from crypto_wallet import send_transaction
w3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:7545"))

# Create a database of the houses

housing_database = {
    "House 1": [
        "House 1",
        "0xaC8eB8B2ed5C4a0fC41a84Ee4950F417f67029F0",
        "19130 Cartwright Ct, Bend, OR 97702",
        100,
        "Images/house1.jpeg",
        "4,764 sqft",
        "4 Bed, 6 Bath",
    ],
    "House 2": [
        "House 2",
        "0x2422858F9C4480c2724A309D58Ffd7Ac8bF65396",
        "8641 Ruette Monte Carlo, La Jolla, CA 92037",
        200,
        "Images/house2.jpeg",
        "7,264 sqft",
        "5 Bed, 5 Bath",
    ],
    "House 3": [
        "House 3",
        "0x8fD00f170FDf3772C5ebdCD90bF257316c69BA45",
        "21376 N 110th Pl, Scottsdale, AZ 85255",
        250,
        "Images/house3.jpeg",
        "10,600 sqft",
        "5 Bed, 6 Bath",
    ],
}

# A list of houses
house = ["House 1", "House 2", "House 3"]

# Function to display housing data to streamlit
def get_house():
    
    db_list = list(housing_database.values())

    for number in range(len(house)):
        st.image(db_list[number][4], width=800)
        st.write("Name: ", db_list[number][0])
        st.write("Ethereum Account Address: ", db_list[number][1])
        st.write(db_list[number][2])
        st.write("Price ", db_list[number][3], "eth")
        st.write("Size ", db_list[number][5])
        st.write("Layout ", db_list[number][6])
        st.text(" \n")

# Create Header for Streamlit
st.markdown("# Houses For Sale")
st.markdown("## Select A House to Purchase")
st.text(" \n")

# Create Sidebar
st.sidebar.markdown("##  House Account Address and Ethernet Balance in Ether")

# Call the generate_account function from cyrpto_wallet.py
account = generate_account()

# Write the client's Ethereum account address to the sidebar
st.sidebar.write(account.address)

# Display balance of account adress on side bar
st.sidebar.write(get_balance(w3, account.address))

# Create a select box to chose a house
houses = st.sidebar.selectbox("Select a House", house)

st.sidebar.markdown("## House, Price, and Ethereum Address")

# Identify the houses
place = housing_database[houses][0]

# Write the name of the house in the sidebar
st.sidebar.write(place)

# Identify the price
price = housing_database[houses][3]

# Write the in the price of the house to sidebar
st.sidebar.write(price)

# Identify the houses Ethereum Address
house_address = housing_database[houses][2]

# Write the houses Ethereum Address to the sidebar
st.sidebar.write(house_address)

# Sidebar Streamlit
st.sidebar.markdown("## Total Wage in Ether")

# Create the transcation hash
if st.sidebar.button("Send Transaction"):

    transaction_hash = send_transaction(w3, account, house_address, price)

    # Markdown for the transaction hash
    st.sidebar.markdown("#### Validated Transaction Hash")

    # Write the returned transaction hash to the screen
    st.sidebar.write(transaction_hash)

    # Celebrate your successful payment
    st.balloons()

get_house()


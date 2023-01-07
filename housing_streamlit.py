# Imports
import streamlit as st
from dataclasses import dataclass
from typing import Any, List
from web3 import Web3
from wallet import generate_account
from wallet import get_balance
from wallet import send_transaction
w3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:7545"))

# Creating a simple login page.
import streamlit_authenticator as stauth
import yaml

hashed_passwords = stauth.Hasher(['123', '456']).generate()
with open('./config.yaml') as file:
    config = yaml.load(file, Loader=yaml.SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

name, authentication_status, username = authenticator.login('Login', 'main')

if authentication_status:
    authenticator.logout('Logout', 'main')
    st.write('Welcome')
    st.title('Some content')
elif authentication_status == False:
    st.error('Username/password is incorrect')
elif authentication_status == None:
    st.warning('Please enter username and password')

# Creat background photo
import base64
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"jpeg"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('background2.jpeg')

# Create a database of the houses

housing_database = {
    "House 1": [
        "House 1",
        "0xaC8eB8B2ed5C4a0fC41a84Ee4950F417f67029F0",
        "19130 Cartwright Ct, Bend, OR 97702",
        20,
        "Images/house1.jpeg",
        "4,764 sqft",
        "4 Bed, 6 Bath",
    ],
    "House 2": [
        "House 2",
        "0x2422858F9C4480c2724A309D58Ffd7Ac8bF65396",
        "8641 Ruette Monte Carlo, La Jolla, CA 92037",
        20,
        "Images/house2.jpeg",
        "7,264 sqft",
        "5 Bed, 5 Bath",
    ],
    "House 3": [
        "House 3",
        "0x8fD00f170FDf3772C5ebdCD90bF257316c69BA45",
        "21376 N 110th Pl, Scottsdale, AZ 85255",
        20,
        "Images/house3.jpeg",
        "10,600 sqft",
        "5 Bed, 6 Bath",
    ],
    "House 4": [
        "House 4",
        "0x1099C08D73BedF05026ea678D4B59087a8143d34",
        "5637 N 110th Pl, Scottsdale, AZ 85255",
        20,
        "Images/house4.jpg",
        "10,600 sqft",
        "5 Bed, 6 Bath",
    ],
    "House 5": [
        "House 5",
        "0x0fF7CECF9C980A26cA8C9269a1158C1E63b785DB",
        "4227 N Burnham Pl, Scottsdale, AZ 85255",
        20,
        "Images/house5.jpg",
        "8,600 sqft",
        "5 Bed, 6 Bath",
    ],
    "House 6": [
        "House 6",
        "0x04E537653B57753CfEbf4f03DC9144D22905259F",
        "1001 W Country Rd, Scottsdale, AZ 85255",
        20,
        "Images/house6.jpg",
        "9,600 sqft",
        "5 Bed, 6 Bath",
    ],
    "House 7": [
        "House 7",
        "0x3CE50A84bA63B1Ca28117E3c1Ff16dbd8E67FB02",
        "4227 N Burnham Pl, Scottsdale, AZ 85255",
        20,
        "Images/house7.jpg",
        "10,600 sqft",
        "5 Bed, 6 Bath",
    ]
}

# A list of houses
house = ["House 1", "House 2", "House 3", "House 4", "House 5", "House 6", "House 7"]

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

# generate_account function 
account = generate_account()

# Write Ethereum account address to sidebar
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
house_address = housing_database[houses][1]

# Write the houses Ethereum Address to the sidebar
st.sidebar.write(house_address)

# Sidebar Streamlit
st.sidebar.markdown("## Total Amount in Ether")

# Create the transcation hash
if st.sidebar.button("Send Transaction"):

    transaction_hash = send_transaction(w3, account, house_address, price)

    # Markdown for the transaction hash
    st.sidebar.markdown("## Validated Transaction Hash")

    # Write the returned transaction hash to the screen
    st.sidebar.write(transaction_hash)

get_house()


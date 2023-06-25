import streamlit as st
from faker import Faker

fake = Faker()

def generate_fake_data():
    st.subheader("Generated Information:")
    st.write("Name:", fake.name())
    st.write("Email:", fake.email())
    st.write("Address:", fake.street_address())
    st.write("City:", fake.city())
    st.write("State:", fake.state())
    st.write("Postal Code:", fake.postcode())
    st.write("Country:", fake.country())
    st.write("Credit Card Number:", fake.credit_card_number())
    st.write("Phone Number:", fake.phone_number())

# Streamlit App
st.title("Fake Data Generator")

# Generate button
if st.button("Generate"):
    generate_fake_data()
  

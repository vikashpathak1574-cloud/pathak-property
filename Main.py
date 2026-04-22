import streamlit as st

# Page Config
st.set_page_config(page_title="Pathak Property", layout="wide")

# HEADER
st.title("🏠 Pathak Property")
st.subheader("Buy | Sell | Rent Properties")

# HERO SECTION
st.markdown("## Find Your Dream Property in Indirapuram & Noida")
st.button("📞 Call Now: 8447156101")

st.write("---")

# ABOUT
st.markdown("## About Us")
st.write("""
Pathak Property is a trusted real estate service helping clients buy, sell, and rent properties in Indirapuram, Noida, and nearby areas.

We provide verified listings and best deals.
""")

st.write("---")

# PROPERTIES
st.markdown("## Featured Properties")

col1, col2, col3 = st.columns(3)

with col1:
    st.image("https://images.unsplash.com/photo-1560185127-6ed189bf02f4")
    st.subheader("2BHK Flat - Indirapuram")
    st.write("₹1 Cr | 1250 sqft")

with col2:
    st.image("https://images.unsplash.com/photo-1560448204-e02f11c3d0e2")
    st.subheader("1BHK Rent")
    st.write("₹15,000/month")

with col3:
    st.image("https://images.unsplash.com/photo-1572120360610-d971b9d7767c")
    st.subheader("3BHK Rent")
    st.write("₹22,000/month")

st.write("---")

# WHY CHOOSE US
st.markdown("## Why Choose Us")
st.write("""
✔ Verified Properties  
✔ Best Price Deals  
✔ Local Expertise  
✔ Fast Response  
✔ Trusted Service  
""")

st.write("---")

# CONTACT
st.markdown("## Contact Us")

name = st.text_input("Your Name")
phone = st.text_input("Phone Number")
msg = st.text_area("Requirement")

if st.button("Submit"):
    st.success("Thank you! We will contact you soon.")

st.write("---")

st.markdown("📞 Contact: 8447156101")
st.markdown("📍 Indirapuram | Noida | Ghaziabad")

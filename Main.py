import streamlit as st
import urllib.parse

# Page Config
st.set_page_config(page_title="Pathak Property", layout="wide")

# HEADER
st.title("🏠 Pathak Property")
st.subheader("Buy | Sell | Rent Properties")

# HERO
st.markdown("## Find Your Dream Property in Indirapuram & Noida")

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

# CONTACT FORM
st.markdown("## 📞 Contact Us")

name = st.text_input("Your Name")
phone = st.text_input("Phone Number")
msg = st.text_area("Requirement")

# WhatsApp Send Button
if st.button("Send via WhatsApp"):

    if name and phone and msg:
        text = f"New Property Lead:%0AName: {name}%0APhone: {phone}%0ARequirement: {msg}"
        
        encoded_text = urllib.parse.quote(text)

        whatsapp_url = f"https://wa.me/918447156101?text={encoded_text}"

        st.success("Click below to send message on WhatsApp 👇")

        st.markdown(f"[👉 Send Message Now]({whatsapp_url})")

    else:
        st.error("Please fill all details")

st.write("---")

st.markdown("📍 Indirapuram | Noida | Ghaziabad")

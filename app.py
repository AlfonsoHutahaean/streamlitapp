import streamlit as st

st.title("Aplikasi Streamlit Pertama Saya")
st.write("Halo! Ini adalah aplikasi web pertama saya menggunakan Streamlit.")
nama = st.text_input("Masukkan nama Anda:")
if nama:
    st.success(f"Halo, {nama}!")

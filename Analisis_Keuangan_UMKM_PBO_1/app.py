import streamlit as st

st.set_page_config(
    page_title="Money Tracker",
    page_icon="💰",
    layout="centered",
    initial_sidebar_state="expanded"
)

def load_css():
    try:
        with open("assets/style.css") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        pass 

load_css()

def main():
    st.title("💰 Money Tracker")
    st.write("Catat keuangan Warung dan Pribadi Anda dengan mudah dari HP.")
    st.info("Silakan buka menu di sebelah kiri 👈 untuk mulai menggunakan aplikasi.")

if __name__ == "__main__":
    main()

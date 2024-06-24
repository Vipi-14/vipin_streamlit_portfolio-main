import streamlit as st


def main():

    # --- Streamlit page configuration ---

    st.set_page_config(
        page_title="", 
        page_icon="🕹️", 
        layout="centered",
        initial_sidebar_state="collapsed",
        menu_items={
            "About": """"""
        }
        )
    
    # --- Title ---

    st.markdown("<h1 style='text-align: center;'><span style='background-color: #12c914'>🤖🕹️</span> <em>T.</em> <span style='background-color: #0074ba'>🎮🤖</span></h1>", unsafe_allow_html=True)

    st.divider()


    # --- Sidebar ---



if __name__ == "__main__":

    main()

import streamlit as st
from page1 import page1_content
from page2 import page2_content
from page2 import Insights_Generation
# from page2 import get_download_link
# from page2 import voice_output


# Main function to run the app
def main():
    # Initialize session state to store current page
    if 'current_page' not in st.session_state:
        st.session_state.current_page = "page1"

    # Display content based on the current page
    if st.session_state.current_page == "page1":
        # Display content for Page 1
        if "show_go_to_page2_button" not in st.session_state:
            st.session_state.show_go_to_page2_button = False
        if st.session_state.current_page == "page1":
    # Display content for Page 1
            page1_content()
    # Display the "Go to Page 2" button only when the "Suggest Chart" button is clicked
            if st.session_state.show_go_to_page2_button and st.button("Visualize"):
        # Change the current page to navigate to Page 2
               st.session_state.current_page = "page2"
        # if st.button("Go to Page 2"):
        #     # Change the current page to navigate to Page 2
        #     st.session_state.current_page = "page2"

    elif st.session_state.current_page == "page2":
        
        page2_content()
        Insights_Generation()

    
# Run the app
if __name__ == "__main__":
    main()
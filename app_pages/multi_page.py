import streamlit as st

class MultiPage:
    """
    Class for generating a streamlit browser with multiple pages
    """

    def __init__(self, app_name) -> None:
        """
        Init function. The -> None is an annotation that says that the function has no output 
        """
        self.pages = [] # empty list
        self.app_name = app_name

        st.set_page_config(
            page_title = self.app_name, # sets title of the tab
            page_icon = ":shark:" # sets favicon
        )

    def app_page(self, title, func) -> None:
        """
        adds the dictionary below into the pages list
        """
        self.pages.append({
            "title": title,
            "function": func
        })
    
    def run(self):
        """
        Run function
        sets heading using title method
        Adds a menu using the sidebar method
        Sets that menu to have a name of menu and to use radio buttons
        Options to select are pages
        Page options are given titles
        """
        st.title(self.app_name)
        page = st.sidebar.radio(
            'Menu',
            self.pages,
            format_func=lambda page: page['title']
        )
        page['function']()

import streamlit as st
from streamlit_option_menu import option_menu

import About,GetStarted,Home,Services

st.set_page_config(
    page_title ='QuickViewInsight',page_icon="🔍")

class MultiApp:
    def __init__(self):
        self.apps = []
    def add_app(self,title,function):
        self.apps.append({
            "title": title,
            "function": function
        })
    def run():

        with st.sidebar:
            app = option_menu(
                menu_title="Main Menu",
                options = ['Home','About','Services','GetStarted'],
                icons = ['house-fill','info-circle','list','play'],
                default_index =0,
                styles = {"container" : {"padding": "5!important","background-color":"black"},
                "nav-link": {"color":"white","font-size":"20px","text-align":"left","margin":"0px","--hover-color":"blue"},
                "icon" : {"color": "white","font-size":"23px"},
                "nav-link_selected":{"background-color": "#02ab21"},}

            )

        if app=='Home':
            Home.app()
        if app=='About':
            About.app()
        if app=='Services':
            Services.app()
        if app=='GetStarted':
            GetStarted.app()

    run()
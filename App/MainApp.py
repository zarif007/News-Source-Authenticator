import re
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.label import MDLabel,MDIcon
from kivymd.uix.button import MDCustomRoundIconButton, MDRectangleFlatButton,MDRoundFlatButton,MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivy.uix.image import Image
from kivy.lang import Builder,BuilderException
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.list import OneLineListItem
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from real_newslist import lis
import time


link_helper="""
MDTextField:
    hint_text : "Enter URL"
    helper_text : "Please Enter URL"
    icon_right:"link"
    pos_hint :{'center_x':0.5 , 'center_y':0.45}
    size_hint_x:None
    width:500
"""

link1_helper="""
MDTextField:
    hint_text : "Enter Image/Image URL"
    helper_text : "Please Enter URL"
    icon_right:"image"
    pos_hint :{'center_x':0.5 , 'center_y':0.32}
    size_hint_x:None
    width:500
"""

link2_helper="""
MDTextField:
    hint_text : "Enter Text"
    helper_text : "Please Enter Text"
    icon_right:"text"
    pos_hint :{'center_x':0.5 , 'center_y':0.21}
    size_hint_x:None
    width:500
"""

nav_helper="""
Screen:
    NavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: 'Some Authentic News Sources'
                        left_action_items: [["menu",lambda x: nav_drawer.toggle_nav_drawer()]]
                        elevation:10
                    
        MDNavigationDrawer:
            id: nav_drawer
            BoxLayout:
                orientation:'vertical'
                spacing : '8dp'
                padding : '8dp'

                # MDLabel:
                #     text:'Bangla News Portals'
                #     font_style : 'H5'
                #     size_hint_y:None
                #     height: self.texture_size[1]
               
                ScrollView:
                    MDList:
                        OneLineListItem:
                            text:'Bangla News Portals'
                            font_style : 'Subtitle1'
                        OneLineListItem:
                            text:'https://www.atnbangla.tv/'
                            font_style : 'Button'
                        OneLineListItem:
                            text:'https://www.jugantor.com/'
                            font_style : 'Button'
                        OneLineListItem:
                            text:'https://www.prothomalo.com/'
                            font_style : 'Button'
                        OneLineListItem:
                            text:'https://bangla.dhakatribune.com/'
                            font_style : 'Button'
                        OneLineListItem:
                            text:'https://samakal.com/'
                            font_style : 'Button'

                        OneLineListItem:
                            text:' '
                            font_style : 'Subtitle1'

                        OneLineListItem:
                            text:'English News Portals'
                            font_style : 'Subtitle1'
                        OneLineListItem:
                            text:'https://www.dhakatribune.com/'
                            font_style : 'Button'
                        OneLineListItem:
                            text:'https://www.thedailystar.net/'
                            font_style : 'Button'
                        OneLineListItem:
                            text:'https://www.daily-sun.com/'
                            font_style : 'Button'
                        OneLineListItem:
                            text:'https://thefinancialexpress.com.bd/'
                            font_style : 'Button'
                        OneLineListItem:
                            text:'https://thebangladeshtoday.com/'
                            font_style : 'Button'
                        
"""


class NSA(MDApp):
    def build(self):
        screen=Screen()
        hlp=Builder.load_string(nav_helper)
        #label=MDLabel(text='News Source Authenticator' ,  halign='center', theme_text_color='Error' , font_style='H6')
        button=MDRectangleFlatButton(text='Check', pos_hint ={'center_x':0.5 , 'center_y':0.39} , on_release=self.check_source)
        buttonl1=MDRectangleFlatButton(text='Check', pos_hint ={'center_x':0.5 , 'center_y':0.26} , on_release=self.check_image)
        buttonl2=MDRectangleFlatButton(text='Check', pos_hint ={'center_x':0.5 , 'center_y':0.15} , on_release=self.check_text)
        button1=MDRoundFlatButton(text='Change Mode', pos_hint ={'center_x':0.8 , 'center_y':0.95} , on_release=self.change_colour)
        img = Image(source='Add a heading (1).png')
        self.link=Builder.load_string(link_helper)
        self.link1=Builder.load_string(link1_helper)
        self.link2=Builder.load_string(link2_helper)
        screen.add_widget(self.link)
        screen.add_widget(self.link1)
        screen.add_widget(self.link2)
        screen.add_widget(button)
        screen.add_widget(button1)
        screen.add_widget(buttonl1)
        screen.add_widget(buttonl2)
        screen.add_widget(img)
        screen.add_widget(hlp)
        return screen

    countColor = 0
    def change_colour(self,obj):
        self.countColor = self.countColor+1
        if(self.countColor%2 != 0):
            self.theme_cls.theme_style = "Dark"
        else:
            self.theme_cls.theme_style = "Light"
           
        
    fakeList = []
    fakeCounter = 0
    def check_source(self, obj):
        Link = str(self.link.text)
        Link_size = len(Link)
        final_source = ""
        hCounter = 0
        for i in range (0, Link_size):
            if(hCounter < 3):
                final_source = final_source + Link[i]
                if(Link[i]=='/'):
                    hCounter+=1
            else:
                break

        print(final_source)
        count=0
        for i in range (len(lis)):
            hlink = lis[i]
            if(final_source == hlink):
                count+=1
        
        ln=len(f)-1

        close_button=MDFlatButton(text='close', on_release=self.colse_dialog)
        if(count != 0):
            self.dialog = MDDialog(title='REAL NEWS' , text="The news source " + final_source[8:ln] + "  is legit and there is high chance of being 
                                                       this news true.", size_hint=(0.7,2),buttons=[close_button])
            self.dialog.open()
        else:
            self.fakeList.append(final_source[8:ln])
            print(self.fakeList[self.fakeCounter])
            self.fakeCounter = +1
            self.dialog = MDDialog(title='FAKE NEWS' ,  text="The news source " + final_source[8:ln] + "  is not legit and there is high chance of being 
                                                        this news fake.", size_hint=(0.7,2),buttons=[close_button])
            self.dialog.open()

    def colse_dialog(self,obj):
        self.dialog.dismiss()


    def check_text(self, obj):
        s=self.link2.text 
        options = webdriver.ChromeOptions() 
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        driver = webdriver.Chrome(options=options, executable_path=r'F:\chromedriver.exe')
        driver.get("https://google.com/")

        search = driver.find_element_by_name("q")
        search.send_keys(s)
        search.send_keys(Keys.RETURN)
        time.sleep(10)

    def check_image(self, obj):
        s=self.link1.text 
        options = webdriver.ChromeOptions() 
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        driver = webdriver.Chrome(options=options, executable_path=r'F:\chromedriver.exe')
        driver.get("https://google.com/")

        search = driver.find_element_by_name("q")
        search.send_keys(s)
        search.send_keys(Keys.RETURN)
        time.sleep(10)


NSA().run()


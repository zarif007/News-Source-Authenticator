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

    c=0
    def change_colour(self,obj):
        self.c=self.c+1
        if(self.c%2!=0):
            self.theme_cls.theme_style="Dark"
        else:
            self.theme_cls.theme_style="Light"
            
    fakeList=[]
    fc=0

    def check_source(self,obj):
        lis=['https://www.atnbangla.tv/','https://www.dhakatribune.com/','https://www.prothomalo.com/','https://bangla.dhakatribune.com/' ,
        'https://samakal.com/','https://www.jugantor.com/' 'https://www.dailyinqilab.com/''https://www.dailynayadiganta.com/','https://www.kalerkantho.com/',
        'https://www.bhorerkagoj.com/','https://www.bangla.24livenewspaper.com/',
        'https://www.dailyjanakantha.com/','https://www.24livenewspaper.com/',
        'https://www.bd-journal.com/','https://www.manobkantha.com.bd/',
        'https://www.dailyjagaran.com/','https://epaper.alokitobangladesh.com/',
        'https://ebhorerkagoj.com/2020/09/01/','https://epaper.dainikamadershomoy.com/',
        'https://epaper.manobkantha.com.bd/','https://epaper.ittefaq.com.bd/','https://epaper.shomoyeralo.com/',
        'https://epaper.manobkantha.com.bd/','https://banglavision.tv/','https://www.channelionline.com/'
        'https://www.somoynews.tv/','https://www.deshrupantor.com/','https://www.dailyjagaran.com/',
        'https://www.jamuna.tv/','https://www.ekushey-tv.com/','https://unb.com.bd/',
        'https://www.banglatribune.com/','https://www.jagonews24.com/',
        'https://www.banglanews24.com/','https://www.24livenewspaper.com/',
        'https://www.priyo.com/','https://banglavision.tv/','https://www.channel24bd.tv/','https://www.ekushey-tv.com/',
        'https://www.jamuna.tv/','https://maasranga.tv/','https://www.ntvbd.com/','https://www.rtvonline.com/','https://www.somoynews.tv/',
        'https://www.aajkaal.in/','https://www.anandabazar.com/','https://bartamanpatrika.com/',
        'https://www.bbc.com/bengali/','https://www.dw.com/bn/','https://www3.nhk.or.jp/nhkworld/bn/','https://parstoday.com/bn','https://www.voabangla.com/',
        'https://www.thedailystar.net/','https://www.newagebd.net/','https://www.daily-sun.com/','https://thebangladeshtoday.com/','https://thefinancialexpress.com.bd/',]

    
    
        s=str(self.link.text)
        z=len(s)
        f=""
        hc=0

        for i in range (0,z):
            if(hc<3):
                f=f+s[i]
                if(s[i]=='/'):
                    hc+=1
            else:
                break


        print(f)
        count=0
        for i in range (len(lis)):
            h=lis[i]
            if(f==h):
                count+=1
        

        ln=len(f)-1

        close_button=MDFlatButton(text='close' , on_release=self.colse_dialog)
        if(count!=0):
            self.dialog=MDDialog(title='REAL NEWS' , text="The news source "+f[8:ln]+"  is legit and there is high chance of being this news true.",size_hint=(0.7,2),buttons=[close_button])
            self.dialog.open()
        else:
            self.fakeList.append(f[8:ln])
            print(self.fakeList[self.fc])
            self.fc=+1
            self.dialog=MDDialog(title='FAKE NEWS' ,  text="The news source "+f[8:ln]+"  is not legit and there is high chance of being this news fake.",size_hint=(0.7,2),buttons=[close_button])
            self.dialog.open()

    def colse_dialog(self,obj):
        self.dialog.dismiss()


    def check_text(self,obj):
        s=self.link2.text 
        options = webdriver.ChromeOptions() 
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        driver = webdriver.Chrome(options=options, executable_path=r'F:\chromedriver.exe')
        driver.get("https://google.com/")

        search = driver.find_element_by_name("q")
        search.send_keys(s)
        search.send_keys(Keys.RETURN)
        time.sleep(10)

    def check_image(self,obj):
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


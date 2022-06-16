import os
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout



class Grid_LayoutApp(App):


	def build(self):


		layout = GridLayout(cols = 2)


		layout.add_widget(Button(text ='Call'))
		layout.add_widget(Button(text ='time & date'))

		# 2nd row
		layout.add_widget(Button(text ='message'))
		layout.add_widget(Button(text ='location'))

		# 3rd row
		layout.add_widget(Button(text ='face detection'))
		layout.add_widget(Button(text ='currency detection'))



		# returning the layout
		return layout

# creating object of the App class
root = Grid_LayoutApp()

# run the App
root.build()
root.run()
import speech.py

speech.record_audio()
speech.respond()
os.system("python speech.py ")
from ._anvil_designer import Form1Template
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files

import anvil.server
import anvil.server

class Form1(Form1Template):
  

  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.

  def file_loader_1_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    
    self.image_1.source= file

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""

    # Call the google colab function and pass it the iris measurements
    namesdict=app_files.names_txt
    kn=app_files.modelkn1_pkl
    kn2=app_files.modelkn2_pkl
    kn3=app_files.modelkn3_pkl
    kn4=app_files.modelkn4_pkl
    lr1=app_files.modellr1_pkl
    lr2=app_files.modellr2_pkl
    lr3=app_files.modellr3_pkl
    svm1=app_files.modelsvm1_pkl
    svm2=app_files.modelsvm2_pkl
    svm4=app_files.modelsvm4_pkl

    pc=app_files.modelpc_pkl
    person = anvil.server.call('predict_person', self.image_1.source,namesdict,kn,kn2,kn3,kn4,lr1,lr2,lr3,svm1,svm2,svm4,pc)
    # If a category is returned set our species 
    if person:
      self.Result.visible = True
      self.Result.text = person
      
      
      
      
    pass





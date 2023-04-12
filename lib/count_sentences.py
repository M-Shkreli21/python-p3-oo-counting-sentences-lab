#!/usr/bin/env python3

class MyString:
  
  def __init__(self, value=""):
        self._value = value
        
  def get_value(self):
        return self._value
      
  def set_value(self, strVal):
        if (type(strVal) == str):
              self._value = strVal
        else:
              print("The value must be a string.")
              
  value = property(get_value, set_value)
  
  def is_sentence(self):
        return self.value.endswith(".")
      
  def is_question(self):
        return self.value.endswith("?")
  
  def is_exclamation(self):
        return self.value.endswith("!")
  
  def count_sentences(self):
        value = self.value
        for gmr in ['!', '?']:
              value = value.replace(gmr, '.')
              
        sentence_list = [sentence for sentence in value.split('.') if sentence]
        
        return len(sentence_list)
      

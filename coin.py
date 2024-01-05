import random

class Coin:
	def __init__(self,rare = False,clean = True,head = True,**kwargs):
		self.is_rare = rare
		self.is_clean = clean
		self.head = head

		if self.is_rare:
			self.value = self.orignal_value *1.25
		else:
			self.value = self.orignal_value

		if self.is_clean:
			self.colour = self.clean_colour
		else:
			self.colour = self.rusty_colour	

	def rust(self):
		self.colour = self.rusty_colour

	
	def clean(self):
		self.colour = self.clean_colour

	
	def __del__(self):
		print("Coin Spent!!!")
	
	def flip(self):
		heads_option = [True,False]
		choice = random.choice(heads_option)
		self.head = choice

class Pound(Coin):
	def __init__(self):
		data = {
		"orignal_value":100
		"clean_colour":'Gold'
		"rusty_colour":'Greenish'
		"num_edges":1
		"diameter":22.5
		"thickness":3.15
		"mass":9.5
		}
	super().__init__(**data)	

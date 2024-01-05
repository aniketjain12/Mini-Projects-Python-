orignal = input("Please enter a sentence: ".strip().lower())

words = orignal.split()
new_words = []

for word in words:
	if word[0] in "aeiou":
		new_word = word + "yay"
		new_words.append(new_word)

	else:
	    vow_pos = 0
	    for letter in word: 
	        if letter != "aeiou":
	            vow_pos += 1
	        else:
	            break
	        cons = word[:vow_pos]
	        the_rest = word[vow_pos:]
	        new_word = the_rest + cons + "ay" 
	        new_words.append(new_word)

output = " ".join(new_words)
print(output)	     

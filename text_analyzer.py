text=(input("Please type a text of your liking: "))
letters=[]

text=text.lower()

letters.append(input("Choose a letter: ").lower())
letters.append(input("choose another letter: ").lower())
letters.append(input("choose one more letter: ").lower())

print("\n")
print("times your chosen letters repeat: ")
letters_amount1=text.count(letters[0])
letters_amount2=text.count(letters[1])
letters_amount3=text.count(letters[2])

print(f"We have found the letter: '{letters[0]}' {letters_amount1} times in your text")
print(f"We have found the letter: '{letters[1]}' {letters_amount2} times in your text")
print(f"we have found the letter: '{letters[2]}' {letters_amount3} times in your text")

print("\n")
print("words amount: ")
words=text.split()
print(f"we have found {len(words)} words in your text")

print("\n")
print("first and last letter: ")
first_letter=text[0]
last_letter=text[-1]
print(f"The first letter is: '{first_letter}' and the last one is: '{last_letter}'")

print("\n")
print("Reversed text: ")
words.reverse()
reversed_text= ' '.join(words)
print(f"This is how your text looks when is reversed: '{reversed_text}'")
print("\n")
print("LOOKING FOR THE WORD 'PYTHON': ")
seek_python= 'python' in text
dic={True:"is",False:"is not"}
print(f"The word 'python' {dic[seek_python]} in your text")

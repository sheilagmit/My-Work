# Programme to input a string and output every second letter in reverse order.
# Author: Sheila Bambrick
# I used https://stackoverflow.com/ to help write the programme.

# First, output the sentence in reverse order
txt = "The quick brown fox jumps over the lazy dog." [::-1]
print(txt)

# Second, use the output from step 1 and print every second letter.
sentence = ".god yzal eht revo spmuj xof nworb kciuq ehT"
print(sentence[::2])


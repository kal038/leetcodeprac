This is so easy...
Sliding window approach
expand the window by 1 until there's a duplicate then contract the window
keep a running max count at every step the way
How to check duplicates you may ask?
chars = [0,0,0,0,0,0,...,0] 128 times representing the 128 characters in the unicode
increment by 1 everytime you see the character at your right pointer
if it reaches 2, contract window
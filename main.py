#TODO: Create a letter using starting_letter.txt
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

textlist = open("./Input/Letters/starting_letter.txt").read()
print(textlist)

namelist = open("./Input/Names/invited_names.txt").readlines()

for name in namelist:
    stripname = name.strip()
    letter = textlist.replace("[name]", stripname)
    finalletter = open(f"./Output/ReadyToSend/letter for {stripname}.txt", mode="w").write(letter)
    print(letter)


    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
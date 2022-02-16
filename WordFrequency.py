#Write a program that reads the contents of a text file. The program should create a dictio-nary 
#in which the keys are the individual words found in the file and the values are the number of times
#each word appears. For example, if the word “the” appears 128 times, the dictionary would contain an 
#element with 'the' as the key and 128 as the value. The program should display the frequency of each word
infile = open("AI.txt", "r")

word_frequency = {}

for line in infile:
    line = line.strip()
    line = line.lower()
    line = line.split(" ")
    
    for word in line:
        word = word.strip('(')
        word = word.strip(')')
        word = word.strip('"')
        word = word.strip('")')
        word = word.strip("'")
        word = word.strip(';')
        word = word.strip('')
        word = word.strip('"),')
        word = word.strip('.')
        
        if word in word_frequency:
            word_frequency[word] = word_frequency[word] + 1
        else:
            word_frequency[word] = 1

print(word_frequency)

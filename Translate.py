import pandas as pd
from datetime import datetime
# Open the file in read mode
start_time = datetime.now()
text = open("t8.shakespeare.txt", "r")
org_text = open("t8.shakespeare.txt", "r").read()
  
# Create an empty dictionary 
d = dict() 
  
for line in text: 
    # Remove the leading spaces and newline character 
    line = line.strip() 
  
    # Convert the characters in line to  
    # lowercase to avoid case mismatch 
    line = line.lower() 
  
    # Split the line into words 
    words = line.split(" ") 
  
    # Iterate over each word in line 
    for word in words: 
        # Check if the word is already in dictionary 
        if word in d: 
            # Increment count of word by 1 
            d[word] = d[word] + 1
        else: 
            # Add the word to dictionary with count 1 
            d[word] = 1
  
# Print the contents of dictionary 
l1=[]
for key in list(d.keys()): 
    # print(key, ":", d[key]) 
    l1.append(key)
      

find_word = open('find_words.txt').read().split()

match_word = [i for i in l1 if i in find_word]

header_list = ["English", "French"]
frenc_dic = pd.read_csv('french_dictionary.csv', names=header_list)

conve_list = []

for i in range(0 ,len(match_word)):
    for j in range(0, len(frenc_dic)):
        if(match_word[i] == frenc_dic['English'][j]):
            conve_list.append(frenc_dic['French'][j])


copy_text = org_text.lower()

copy_text.replace(match_word[i], conve_list[i])
for i in range(0, len(match_word)):
    copy_text = copy_text.replace(match_word[i], conve_list[i])

out_file = open("output_file.txt", "w")
out_file.write(copy_text)
out_file.close()

unique_word = match_word

frq_each_word = []

for i in range(0, len(match_word)):
    for key in list(d.keys()):
        if(match_word[i] == key):
            frq_each_word.append("{'"+key+"':'"+str(d[key])+"'}")


end_time = datetime.now()

out_file_uniq_word = open("Unique_words.txt", "w")
out_file_uniq_word.write("Unique list of words = "+str(unique_word))
out_file_uniq_word.close()

out_file_frq = open("frequency_each_word.txt", "w")
out_file_frq.write(str(frq_each_word))
out_file_frq.close()

out_file_timetaken = open("Time_taken.txt", "w")
out_file_timetaken.write(str(end_time - start_time))
out_file_timetaken.close()
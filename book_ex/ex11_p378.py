s = ["There","are","no", "miracles","in","this","world"]

for num in map(len,filter(lambda s: 'a' in s,s)):
    print(num)
    
print([len(x) for x in s if 'a' in x])
#Print the lengths of all the words in the sentence that contain the letter ‘a’

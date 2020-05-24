import spacy
from collections import Counter

nlp = spacy.load('en_core_web_sm')

resume_file = 'SampleResume.txt'
resume_file_text = open(resume_file).read()
resume_doc = nlp(resume_file_text)

job_file = open('JobKeywords.txt', 'r') 
job_file_lines = job_file.readlines() 

resWords = [token.lemma_ for token in resume_doc if token.is_alpha and not token.is_stop]
resWord_freq = Counter(resWords)
resWords_common = resWord_freq.most_common(10)

print(resWords_common)

match = False
for resWord in resWords_common:
    for line in job_file_lines:
        line = line.split(" ")
        if resWord[0] == line[0] and resWord[1] >= int(line[1]):
            print("Match!")
            match = True

if not match:
    print("Not a match.")
                
    

import spacy
nlp = spacy.load('en_core_web_sm')

while 1==1:
    resume = input('Resume: ')
    resume_doc = nlp(resume)

    job = input('Job Description: ')
    #job = "hello"
    job_doc = nlp(job)

    resKeywords = []
    jobKeywords = []
    matchKeywords = []

    for resToken in resume_doc:
        if resToken.is_alpha and not resToken.is_stop:
            resKeywords.append(resToken.lemma_)

    for jobToken in job_doc:
        if jobToken.is_alpha and not jobToken.is_stop:
            jobKeywords.append(jobToken.lemma_)

    matchKeywords = set(resKeywords).intersection(jobKeywords)

    #print(resKeywords)
    #print(jobKeywords)
    #print(matchKeywords)

    print("Total matches: " + str(len(matchKeywords)))

    print ( len(jobKeywords) )
    print ('Score: ' + str(len(matchKeywords)/len(jobKeywords)*100) + '%')



    y = input("Again? Y/N  ")
    if (y == 'n'):
        break


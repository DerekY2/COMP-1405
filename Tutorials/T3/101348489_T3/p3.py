print("Please write a paragraph and hit enter when you're finished.:")
paragraph = input()
wordCount = len(paragraph.split())
sentences = paragraph.split(".")

print("Total number of words = " + str(wordCount))
print("Total number of sentences = " + str(len(sentences)-1))

print("Capitalized sentences are:")

for j in range (len(sentences)):
    tempSentence = sentences[j]
    if tempSentence[0] == " ":
        tempSentence = tempSentence.strip()
    print(tempSentence[0].upper() + tempSentence[1:].lower() +".")

    if sentences[j+1]=="":
        break
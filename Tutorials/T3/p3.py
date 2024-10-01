paragraph = input("Please write a paragraph and hit enter when you're finished\n")
words = paragraph.split()
sentences = paragraph.split(".")
wordCount = len(words)
sentenceCount = len(sentences)

print(f"Total # of words = {wordCount}\nTotal # of sentences =  {sentenceCount}\nCapitalized sentences are:")
for x in range(sentenceCount):
  if sentences[x]:
    print(f"{sentences[x].strip().capitalize()}.")
    #print(f"{sentences[x].strip()[0].upper()}{sentences[x].strip()[1:]}.")
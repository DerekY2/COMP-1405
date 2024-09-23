paragraph = input("Please write a paragraph and hit enter when you're finished\n")
words = paragraph.split()
sentences = paragraph.split(".")
wordCount = len(words)
sentenceCount = len(sentences)
print(f"Total # of words = {wordCount}")
print(f"Total # of sentences =  {sentenceCount}\n")

print("Capitalized sentences are:")
for x in range(sentenceCount):
  if sentences[x]:
    print(f"{sentences[x].strip().capitalize()}.")         ## or use upper() on the first letter only
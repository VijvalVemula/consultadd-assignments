"""
1.Read the doc.txt file using Python File handling concept and
return only the even length string from the file. Consider the
content of doc.txt as given below:
Hello I am a file
Where you need to return the data string which is of even length.
Make sure you return the content in The same link as it is present.
"""

with open("doc.txt", mode ="r") as file_handle:
    lines = file_handle.readlines()


results = list()

for line in lines:
    words = line.strip().split(" ")
    even_words = [word for word in words if len(word) % 2 == 0]
    results.append(" ".join(even_words))

print("\n".join(results))

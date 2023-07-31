message = input("Enter Your Message : ")
sep = message.split(' ')


emoji = {
    ":)": "☺",
    ":(": "😥"
}
output = ""
for word in sep:
    output += emoji.get(word,word) + " "
print(output)
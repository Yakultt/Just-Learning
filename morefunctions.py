#Messages: Make a list containing a series of short text messages. 
# Pass the list to a function called show_messages(), w
#which prints each text message.

#8-10. Sending Messages: Start with a copy of your program from Exercise 
# 8-9. Write a function called send_messages() that prints each text message and
# moves each message to a new list called sent_messages as it’s printed. 
# After calling the function, print both of your lists to make sure the messages were moved correctly.

#8-11. Archived Messages: Start with your work from Exercise 8-10. Call the function 
# send_messages() with a copy of the list of messages. After calling the function, 
# print both of your lists to show that the original list has retained its messages.

message = ["lol", "hello", "lmfao", "ttyl"]
sent_message = []
def show_messages(messages):
    for message in messages:
        print(f"here is your text message {message}")



def send_messages(messages, sent):
    while messages:
        current = messages.pop()
        print(f"currenly sending the message {current}")
        sent.append(current)
    
    print(f"here are your sent messages")
    for i in sent:
        print(f"\t{i}")

#send_messages(message, sent_message)
#print(message)
#print(sent_message)
send_messages(message[:], sent_message)
print(message)
print(sent_message)
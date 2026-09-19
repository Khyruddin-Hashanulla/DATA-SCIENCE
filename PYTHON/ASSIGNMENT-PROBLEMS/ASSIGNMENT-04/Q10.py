"""
Q10. Mini Project - OOP Chat Room
Let's create a Chat System using OOPs concepts. We have to create classes:
- User
- Message
- ChatRoom
And we have to implement the following functionalities:
1. User can send a message to the chat room.
2. User can view all messages in the chat room.
3. User can join and leave the chat room.
"""

# -----------------------------
# Message class
# -----------------------------

class Message:
    message_counter = 1   # simple counter
    def __init__(self, sender, content):
        self.sender = sender
        self.content = content
        self.id = Message.message_counter
        Message.message_counter += 1

    def __str__(self):
        return f"Message ID: {self.id}, Sender: {self.sender.username}, Content: {self.content}"

# -----------------------------
# User class
# -----------------------------

class User:
    def __init__(self, username):
        self.username = username
        self.chat_room = None

    def join_chat_room(self, chat_room):
        if self.chat_room is not None:
            print(f"{self.username} is already in a chat room.")
            return
        self.chat_room = chat_room
        chat_room.add_user(self)
        print(f"{self.username} joined the chat room.")

    def leave_chat_room(self):
        if self.chat_room is None:
            print(f"{self.username} is not in any chat room.")
            return
        self.chat_room.remove_user(self)
        print(f"{self.username} left the chat room.")
        self.chat_room = None

    def send_message(self, content):
        if self.chat_room is None:
            print(f"{self.username} is not in any chat room. Cannot send message.")
            return
        message = Message(self, content)
        self.chat_room.add_message(message)

# -----------------------------
# ChatRoom class
# -----------------------------

class ChatRoom:
    def __init__(self):
        self.users = []
        self.messages = []

    def add_user(self, user):
        if user not in self.users:
            self.users.append(user)

    def remove_user(self, user):
        if user in self.users:
            self.users.remove(user)

    def add_message(self, message):
        self.messages.append(message)

    def view_messages(self):
        if not self.messages:
            print("No messages in the chat room.")
            return
        for message in self.messages:
            print(message)
# -----------------------------
# Example usage
# -----------------------------

if __name__ == "__main__":
    chat_room = ChatRoom()

    user1 = User("Alice")
    user2 = User("Bob")

    user1.join_chat_room(chat_room)
    user1.send_message("Hello everyone!")
    user2.join_chat_room(chat_room)
    user2.send_message("Hi Alice!")
    user1.send_message("How are you, Bob?")
    chat_room.view_messages()

    user1.leave_chat_room()

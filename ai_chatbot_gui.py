
import tkinter as tk

def get_response(user_input):
    user_input = user_input.lower()
    if "hello" in user_input:
        return "Hi! How can I help you today?"
    elif "project" in user_input:
        return "This is a basic AI chatbot built with Python and Tkinter."
    elif "bye" in user_input:
        return "Goodbye! Have a great day!"
    else:
        return "I'm still learning. Can you try saying that differently?"

def send_message():
    user_input = entry.get()
    chat_log.insert(tk.END, f"You: {user_input}")
    response = get_response(user_input)
    chat_log.insert(tk.END, f"Bot: {response}")
    entry.delete(0, tk.END)

root = tk.Tk()
root.title("AI Chatbot")

chat_log = tk.Listbox(root, height=20, width=50)
chat_log.pack(padx=10, pady=10)

entry = tk.Entry(root, width=40)
entry.pack(side=tk.LEFT, padx=(10, 0), pady=(0, 10))

send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack(side=tk.RIGHT, padx=(0, 10), pady=(0, 10))

root

import json
import tkinter as tk
from tkinter import scrolledtext

# Load the dataset
def load_dataset(file_path):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return {"dialogues": []}
    except json.JSONDecodeError:
        print(f"Error: File '{file_path}' is not a valid JSON file.")
        return {"dialogues": []}

# Get the chatbot's response
def get_response(user_input, dataset):
    for dialogue in dataset['dialogues']:
        if user_input.lower() in dialogue['user_input'].lower():
            return dialogue['bot_reply']
    return "I'm sorry, I don't have an answer for that. Please consult a doctor for further assistance."

# Send message function
def send_message():
    user_input = user_entry.get()
    if user_input.strip() == "":
        return
    
    chat_display.config(state=tk.NORMAL)
    chat_display.insert(tk.END, f"You: {user_input}\n")
    
    # Get the bot's response
    response = get_response(user_input, dataset)
    chat_display.insert(tk.END, f"DoctorBot: {response}\n\n")
    chat_display.config(state=tk.DISABLED)
    
    # Clear the user input
    user_entry.delete(0, tk.END)

# GUI Setup
root = tk.Tk()
root.title("DoctorBot - Healthcare Chatbot")
root.geometry("500x600")

# Chat display area
chat_display = scrolledtext.ScrolledText(root, wrap=tk.WORD, state=tk.DISABLED)
chat_display.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

# User input area
user_entry = tk.Entry(root, width=60)
user_entry.pack(pady=5, padx=10, fill=tk.X)

# Send button
send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack(pady=5)

# Load the dataset
dataset_path = r"E:\alpha_scan\chatbot\chats.json"
dataset = load_dataset(dataset_path)

# Start the GUI event loop
root.mainloop()

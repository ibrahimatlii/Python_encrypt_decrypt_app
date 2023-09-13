from tkinter import *
from cryptography.fernet import Fernet


window=Tk()
window.title("Secret Notes App")
window.minsize(500,300)


key = Fernet.generate_key()
fernet = Fernet(key)
def encrypt_message():
    message = encrypted_entry.get()


    encMessage = fernet.encrypt(message.encode())

    decrypted_entry.insert(1.0,encMessage)

    return encMessage

def decrypt_message():
    message=encrypt_message()
    print("encryoted  message :::::::: ",message)


    decMessage = fernet.decrypt(message).decode()

    print("decrypted message  ::::::: ", decMessage)
    label_result.config(text=decMessage)

img=PhotoImage(file="top_secret.png")
img_label = Label(image=img)
img_label.pack()


encrypt_label=Label(text="Enter your message for encrypt")
encrypt_label.pack()

encrypted_entry=Entry()
encrypted_entry.pack()

decrypt_label=Label(text="your encrypted message")
decrypt_label.pack()

decrypted_entry=Text(width=20,height=7)
decrypted_entry.pack()



master_label=Label(text="Enter your encrypted message for decrypt")
master_label.pack(pady=5)
master_entry=Entry()
master_entry.pack()
label_result=Label(text="--")
label_result.pack()

save_button=Button(text="Encrypt",command=encrypt_message)
save_button.pack(pady=5)

decrypt_button=Button(text="Decrypt", command=decrypt_message)
decrypt_button.pack()

window.mainloop()





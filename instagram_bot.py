
from instagrapi import Client
import time

USERNAME = "dazitzy"  # Ganti dengan username Instagram Anda
PASSWORD = "GzAlfz252"  # Ganti dengan password Instagram Anda

def login_to_instagram():
    cl = Client()
    cl.login(USERNAME, PASSWORD)
    print("Login berhasil!")
    return cl

def check_and_respond_to_messages(cl):
    try:
        inbox = cl.direct_threads(amount=10)
        for thread in inbox:
            if thread.messages and not thread.messages[0].seen:
                user_id = thread.messages[0].user_id
                message = thread.messages[0].text
                print(f"Pesan dari {user_id}: {message}")

                response = "Halo! Ini adalah pesan otomatis dari bot Instagram."
                cl.direct_send(response, thread_id=thread.id)
                print(f"Balasan dikirim ke {user_id}.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

def main():
    cl = login_to_instagram()
    print("Bot berjalan, menunggu pesan baru...")
    while True:
        check_and_respond_to_messages(cl)
        time.sleep(10)

if __name__ == "__main__":
    main()

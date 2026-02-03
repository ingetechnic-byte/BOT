import time

def start_bot():
    while True:
        print("Бот работает...")
        time.sleep(5)

if __name__ == '__main__':
    try:
        start_bot()
    except KeyboardInterrupt:
        print("\nБот остановлен пользователем.")

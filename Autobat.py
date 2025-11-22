import time

def autobat():
    print("========================")
    print("   AutoBat Launcher")
    print("========================")
    print("1. YouTube Auto Uploader")
    print("2. Video Downloader (coming soon)")
    print("3. TikTok/Instagram Poster (coming soon)")
    print("4. Exit")
    print("========================")

    choice = input("Select an option: ")

    if choice == "1":
        print("YouTube uploader is not installed yet.")
        print("We will add it next.")
    elif choice == "2":
        print("Downloading not installed yet.")
    elif choice == "3":
        print("Social posting not installed yet.")
    else:
        print("Goodbye!")

if __name__ == "__main__":
    autobat()

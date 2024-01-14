import os

if __name__ == '__main__':
    print("This interface allows you to ping any destition. Try to insert 127.0.0.1")
    x = input("Insert here an IP address:\t")

    bashCommand = f"ping -c 1 {x}"
    response = os.system(bashCommand)
    print(response)

import keyboard
import os

if __name__ == "__main__":
    print("open setup.txt to change keybindings\n default:\n +death num 1\n -death num 2")

    exit = False

    setup_path = "setup.txt"
    if os.path.exists(setup_path):
        with open(setup_path, "r+") as s:
            k1 = s.readline().strip()
            k2 = s.readline().strip()
    else:
        with open(setup_path, "w") as s:
            k1 = "num 1"
            k2 = "num 2"
            s.write(k1 + "\n")
            s.write(k2 + "\n")


    file_path = "counter.txt"
    if os.path.exists(file_path):
            with open(file_path, "r+") as f:
                counter = int(f.read())
    else:
        counter = 0
        with open(file_path, "w") as f:
            f.write(str(counter))
    while True:
        if not exit:
            if keyboard.is_pressed(k1):
                counter += 1
                print(str(counter))
                exit = True
            if keyboard.is_pressed(k2):
                counter -= 1
                print(str(counter))
                exit = True
        else:
            if not keyboard.is_pressed(k1) and not keyboard.is_pressed(k2):
                with open(file_path, "w") as f:
                    f.write(str(counter))
                exit = False
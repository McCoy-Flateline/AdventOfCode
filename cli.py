# AdventOfCode/cli.py

import cmd
import os


class cli(cmd.Cmd):
    intro = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡤⢤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣠⠴⠶⢤⡞⢡⡚⣦⠹⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢰⣃⠀⠀⠈⠁⠀⠉⠁⢺⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⢯⣄⡀⠀⠀⠀⠀⢀⡞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠉⠓⠦⠤⣤⣤⠞⠀⠀⢀⣴⠒⢦⣴⣖⢲⡀⠀⠀⠀⠀⣠⣴⠾⠿⠷⣶⣄⠀⣀⣠⣤⣴⣶⣶⣶⣦⣤⣤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠈⠳⠼⣰⠃⠀⠀⠀⣼⡟⠁⠀⣀⣀⠀⠙⢿⠟⠋⠉⠀⠀⠀⠀⠀⠀⠉⠉⠛⠿⣶⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠓⣦⣄⣠⣶⣿⣛⠛⠿⣾⣿⠀⢠⣾⠋⣹⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⣷⣄⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣴⡶⠿⠟⠛⠛⠛⠛⠛⠛⠿⢷⣾⣿⣷⡀⠻⠾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣷⣄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣾⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⢿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⢷⣦⡀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠿⣶⣶⣤⡀⠀⠀⠀⠀⢀⣤⡶⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣆⠙⣿⡄
⠀⠀⠀⠀⠀⠀⠀⣠⣾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣷⡀⠀⢷⡄⠸⣯⣀⣼⡷⠒⢉⣉⡙⢢⡀⠀⠀⠀⠀⠀⢸⣿⡀⢸⣿
⠀⠀⠀⠀⠀⠀⢠⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⢄⡾⠐⠒⢆⠀⠀⣿⡇⠀⢸⡇⠀⠈⢉⡟⠀⠀⠀⢹⡟⠃⢧⣴⠶⢶⡄⠀⠀⣿⣇⣼⡟
⠀⠀⣠⣴⡶⠶⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⡿⢃⡾⠁⠀⠀⢸⠃⠀⣿⡇⠀⣸⡇⠀⠀⣼⠀⠀⠀⢠⡾⠁⠀⢸⣿⣤⣼⠗⠀⠀⣿⣿⠛⠀
⢀⣾⠟⠁⠀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠀⠀⢿⠇⡼⠁⠀⠀⢀⡜⠀⢀⣿⠃⠀⠉⠀⠀⠀⢧⠀⠠⡶⣿⠁⠀⢠⠇⠀⠉⠁⠀⠀⠀⣿⡏⠀⠀
⢸⣿⠀⢠⡞⠉⢹⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⠾⢿⣠⣷⡄⠀⠁⠳⠤⠖⠋⠀⠀⣸⡟⠀⠀⠀⠀⠀⠀⠘⣄⡀⠀⠛⢀⡴⠋⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀
⢸⣿⡀⠈⠻⣦⣼⠀⠀⠀⠀⠀⠀⠀⢀⣤⣴⡶⠶⠆⠀⢠⣤⡾⠋⠀⣿⠀⠀⠀⠀⠀⠀⠀⢠⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⡅⠀⠀
⠀⠻⣿⣦⣄⣀⣰⡀⠀⠀⠀⠀⠀⠀⣸⠯⢄⡀⠀⠀⠀⢸⣇⠀⠀⠀⣸⡇⠀⠀⠀⠀⠀⢠⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⠃⠀⠀
⠀⠀⠀⠉⠙⠛⣿⣇⠀⠀⠀⠀⢀⠎⠀⠀⠀⠈⣆⠀⠀⠀⠻⣦⣄⣴⠟⠀⠀⠀⠀⠀⣰⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡄⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⡿⠋⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠸⣿⣆⠀⠀⠀⠘⡄⠀⠀⠀⢀⡞⠀⠀⠀⠀⠀⠉⠀⠀⢀⣀⣤⣴⣾⣿⣧⣄⠀⢀⣠⣴⣶⣶⣶⣤⡶⠋⠉⠀⠀⢀⣀⣀⣠⣤⣶⣾⠿⠋⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠘⢿⣦⡀⠀⠀⠈⠒⠤⠔⠋⠀⠀⠀⠀⠀⠀⣠⣴⡾⠟⠋⠉⠀⠀⠀⠛⣹⣷⣿⠟⠒⠀⠀⠀⠉⢻⣷⣶⣾⠿⠿⠿⠛⠛⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⢿⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠾⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⣹⣿⣿⣄⣀⠀⠀⠀⠀⢀⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠿⣷⣶⣶⣤⣤⣶⡦⠀⠁⠀⠀⠀⠀⠀⣀⣀⣀⣤⣴⡾⠟⠁⠙⠿⣷⣶⣤⣴⣾⠿⠛⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⣽⡿⠁⠀⣤⣤⣶⡶⠾⠿⠟⢻⠛⠉⠁⠀⠀⠀⠀⠀⠀⠈⠉⠙⣿⡆⠀⠈⢿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⠟⠁⠀⢸⣟⡁⠀⠀⠀⠀⣰⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠈⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣶⣿⡏⠀⠀⠀⠸⣿⣤⣶⣀⣤⣾⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣧⣄⣀⣤⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣇⣿⡇⠀⠀⠀⠀⣾⣿⠛⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣍⠛⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⣿⡇⠀⠀⠀⠀⠉⣿⣆⠀⠀⠀⠀⠀⠀⠀⢴⣶⣶⠆⠀⠀⠀⠀⠀⠀⣈⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⡿⠀⠀⠀⠀⠀⠀⣸⣿⡄⠀⠀⠀⠀⠀⠀⢸⣟⢿⣿⣦⠀⠀⢠⣄⣠⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣥⣤⣶⣀⣠⣶⣴⡿⢻⣷⣄⣴⣆⣀⣆⣠⣿⡇⠈⠻⣿⣵⣶⡿⠿⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⢉⡉⠉⠉⠉⠉⠀⠀⠈⠉⢉⣉⣉⡉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                        
                        Welcome to the cli"""
    prompt = "ʕっ•ᴥ•ʔっ "

    def do_exit(self, arg):
        "Closes the program"
        print("Shutting down... \nʕ•ܫ•ʔっ")
        return True

    def do_clear(self, arg):
        "Clears the terminal screen"
        os.system("cls" if os.name == "nt" else "clear")

    def do_ls(slef, arg):
        "list files in current directory"
        os.system("dir" if os.name == "nt" else "ls")

    def postcmd(self, stop: bool, line: str) -> bool:
        print()
        return super().postcmd(stop, line)


if __name__ == "__main__":
    cli().cmdloop()

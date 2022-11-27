import cmd

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    
    def do_EOF(self, line):
        return True
    
    
    def do_quit(self, line):
        "Exit"
        return True
    
    def emptyline(self):
         pass

if __name__ == '__main__':
    hbnbcmd = HBNBCommand()
    hbnbcmd.cmdloop()
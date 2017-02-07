#!/usr/bin/python
import sys
from src.app import App
from command_line_parser.option_parser import CommandLineOptionParser
from command_line_parser.options import FileOption

def main():
    """The main function of the application."""
    option = FileOption()
    options = [option]
    arg_parser = CommandLineOptionParser(options, "", "")
    arg_parser.parseArguments(sys.argv)
    app = App(arg_parser.file, None)
    app.run()

if __name__ == '__main__':
    main()

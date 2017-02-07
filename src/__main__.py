#!/usr/bin/python
import sys
import os
from src.app import App
from command_line_parser.option_parser import CommandLineOptionParser
from command_line_parser.options import FileOption, OutputOption

def main():
    """The main function of the application."""
    file_option = FileOption()
    output_option = OutputOption()
    options = [file_option, output_option]
    arg_parser = CommandLineOptionParser(options, "", "")
    arg_parser.parseArguments(sys.argv)
    if arg_parser.output:
        base_path = arg_parser.output
    else:
        base_path = os.getcwd()
    app = App(arg_parser.file, base_path)
    app.run()

if __name__ == '__main__':
    main()

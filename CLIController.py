import argparse
from convTools import ConvTools
import os

class CLIController:

    def fileconvert_main_menu(self, input_file, output_file):
        try:
            with open(input_file, 'r') as input_file_obj, open(output_file, 'w') as output_file_obj:
                for line in input_file_obj:
                    output_file_obj.write(line.upper())
            print(f"Conversion successful. Output written to {output_file}")
        except FileNotFoundError:
            print("Input file not found.")
        except PermissionError:
            print("Permission error: Unable to read or write to the file.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")

    def main(self):
        #Main is the entry point for the CLI. 
        #Parser creates an argument parser object from the Argparse module. Simplifies parsing command line arguments.
        parser = argparse.ArgumentParser(description="Convert a file to reST, Markdown, or both.")
        #Add positional arguments:
        parser.add_argument("input_file", help="Path to the input text file")
        parser.add_argument("-rest", help="Convert to reST", action='store_true')
        parser.add_argument("-markdown", help="Convert to MarkDown", action='store_true')
        parser.add_argument("-both", help="Convert to both reST and Markdown", action='store_true', required=False)
        #Parse CLI arguments provided by user. args will contain positional argument attributes:
        args = parser.parse_args()
        #Convert relative file path provided by user to absolute path:
        input_file = os.path.abspath(args.input_file)
        #Read input file:
        with open(input_file, 'r') as input_file_obj:
            yaml_content = input_file_obj.read()
        #Call conversion tool functions:
        if args.both:
            ConvTools.rest_writer(input_file, yaml_content)
            ConvTools.markdown_writer(input_file, yaml_content)
        elif args.rest:
            ConvTools.rest_writer(input_file, yaml_content)
        elif args.markdown:
            ConvTools.markdown_writer(input_file, yaml_content)
        else:
            print("Didn't go through user choice markdown, rest, or both")

if __name__ == "__main__":
    controller = CLIController()
    controller.main()

import os
import markdown
import yaml

class ConvTools:

    @staticmethod
    def rest_writer(input_file, yaml_doc):
        # If yaml input file is well-formed, load its content into a dictionary:
        data = yaml.safe_load(yaml_doc)
        #initialize reST document:
        rest_doc = ""
        #interate over key, value pairs:
        for title, body in data.items():
            #Append section title and line of ='s. Number of ='s depends on length of the corresponding body:
            rest_doc += f"{title}\n{'=' * len(body)}\n\n"
            #Append body of the section:
            rest_doc += f"{body}\n\n"

        #create output file name from input file name, replacing the extension name:
        default_op_file = os.path.splitext(os.path.basename(input_file))[0] + ".rst"
        #Open output file for writing and write:
        with open(default_op_file, 'w') as output_file_obj:
            output_file_obj.write(rest_doc)

    @staticmethod
    def markdown_writer(input_file, yaml_doc):
        data = yaml.safe_load(yaml_doc)
        markdown_doc = ""
        #interate over key, value pairs:
        for title, body in data.items():
            #Append a line to markdown_doc with a bullet point, bold line, and content:
            markdown_doc += f"- **{title}**: {body}\n"

        default_op_file = os.path.splitext(os.path.basename(input_file))[0] + ".md"
        with open(default_op_file, 'w') as output_file_obj:
            output_file_obj.write(markdown_doc)

if __name__ == "__main__":
    pass

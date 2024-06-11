import os
from docx_modifier import modify_docx

def process_all_files(directory, file_extension=".docx"):
    for filename in os.listdir(directory):
        if filename.endswith(file_extension):
            file_path = os.path.join(directory, filename)
            modify_docx(file_path)
if __name__ == "__main__":
    directory = "C:\Games"
    process_all_files(directory)

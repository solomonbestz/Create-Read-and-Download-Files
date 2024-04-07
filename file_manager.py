import os

# Get the file path
FILE_PATH = os.path.abspath(__file__)
# Get the base file path
BASE_DIR = os.path.dirname(FILE_PATH)


if __name__=='__main__':
    email_txt = os.path.join(BASE_DIR, "template", 'email.txt')

    content = ""

    with open(email_txt, 'r') as f:
        content = f.read()


    print(content.format(name='solomon'))
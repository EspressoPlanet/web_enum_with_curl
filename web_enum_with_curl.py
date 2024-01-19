import os
import subprocess
import re
import sys

file_name = input("Enter a file name:   ") + ".txt"
out_file = open(os.path.join('WRITE OUTPUT DIRECTORY HERE', file_name), 'w+')

def curl_proc(lines):
    try:
        for i in lines:
            command = f"curl -I -s -m 5 {i.rstrip()} | head -n 1"
            result = subprocess.run(command, shell=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            pattern = r'HTTP/1.1 (\d{3})'
            match = re.search(pattern, result.stdout)
            if match:
                http_code = match.group(1)
                write_output(http_code + " ~~~ " + i.rstrip())
                print(http_code + " ~~~ " + i.rstrip())
        out_file.close();
    except Exception as e:
        print(f"An error occured: {e}")

def write_output(input):
    out_file.write(input + "\n")

def main():
    file_path = sys.argv[1]
    with open(file_path, 'r') as file:
        lines = file.readlines()
    curl_proc(lines)

if __name__=="__main__":
    main()
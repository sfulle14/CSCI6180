"""
source used to lean whisper: https://nicobytes.com/blog/en/how-to-use-whisper/
created: 10/11/24
Author: Steven Fuller
"""

import os
import certifi

# getting ssl cert
os.environ['SSL_CERT_FILE'] = certifi.where()

import whisper
from whisper.utils import get_writer

# input and output directories
input_directory = 'Videos/'
output_directory_1 = 'Transcrips_txt/' 
output_directory_2 = 'Transcrips_tsv/' 

# create the directory
os.makedirs(output_directory_1, exist_ok=True)  
os.makedirs(output_directory_2, exist_ok=True)  

# get the number of files in the folder
num_files = len([f for f in os.listdir(input_directory) if os.path.isfile(os.path.join(input_directory, f))])
counter = 1


# speech to text model
model = whisper.load_model("base")





# create the files for each transcript
for filename in os.listdir(input_directory):
    t = open(os.path.join(output_directory_1, os.path.splitext(filename)[0] + '.txt'), "w")
    t.close()
    t = open(os.path.join(output_directory_2, os.path.splitext(filename)[0] + '.tsv'), "w")
    t.close()
 
# iterate over files in input directory and transcribe each
for filename in os.listdir(input_directory):
    # opens video
    f = os.path.join(input_directory, filename)

    print(f"Transcribing file {counter} of {num_files}")
    
    # transcribes video
    result = model.transcribe(f)

    # opens transcript file
    file = os.path.join(output_directory_1, os.path.splitext(filename)[0] + '.txt')
    file2 = os.path.join(output_directory_2, os.path.splitext(filename)[0] + '.tsv')

    # way to keep track of what files have been transcribed
    print(file)
    

    # writes transcript to txt file
    writer = get_writer("txt", output_directory_1)
    writer(result, file)

    # writes transcript to tsv file
    writer = get_writer("tsv", output_directory_2)
    writer(result, file2)

    counter +=1


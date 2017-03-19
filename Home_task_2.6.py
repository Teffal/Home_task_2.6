import os
import subprocess
from multiprocessing import Process

def create_dir(output_dir):
    if not os.path.exists(output_dir): os.makedirs(output_dir)

def get_list_files(input_dir):
    list_files = []
    [list_files.append(file) for file in os.listdir(input_dir)]
    return list_files

def resize_images(file, output_size, input_dir, output_dir):
    subprocess.Popen(r"convert.exe {} -resize {} {}".format(os.path.join(input_dir, file),
                                                            output_size,
                                                            os.path.join(output_dir, file)))

if __name__ == "__main__":
    input_dir = "Source"
    output_dir = "Result"
    create_dir(output_dir)
    for file in get_list_files(input_dir):
        p = Process(target=resize_images, args=(file, 200, input_dir, output_dir))
        p.start()
        p.join()

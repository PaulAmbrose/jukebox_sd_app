#"""Tool for managing music on SD cards"""
#github address

#Run loop to select file corresponding to the random number
#Check file will fit on remaining SD card space
#If it will transfer it, if not quit

import os, os.path
import random
import sys
import shutil


def get_size(start_path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size

def get_number_source_files(source):
    
    total_number_files = len([name for name in os.listdir(source) if os.path.isfile(os.path.join(source, name))])
    return total_number_files

def main_menu():
    print("Welcome to Paul's SD Card Jukebox Generator\n")
    source = input("Please enter the source directory for your music store:  ") + "/"
    destination = input("Please enter the destination directory of your SD card:  ") + "/"
    counter = 0
    while counter < 5:
    #while  True:
        total, used, free = shutil.disk_usage(destination)
        get_dest_capacity = total
        get_dest_files = used
        calc_dest_space = (get_dest_capacity - get_dest_files)
        random_file = random.choice(os.listdir(source))
        random_file_size = get_size(random_file)
        if random_file_size < calc_dest_space:
            source_file = source + random_file
            print(source_file)
            print(destination)
            try:
                shutil.copytree(source_file, destination + random_file +"/")
                counter = counter +1
            except:
                pass
        else:
            break
    print("Random File Transfer Complete")
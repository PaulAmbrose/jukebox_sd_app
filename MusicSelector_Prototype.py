#"""Tool for managing music on SD cards"""

import os, os.path
import random
import sys
import shutil
import logging
import time

def get_number_source_files(source):
    
    total_number_files = len([name for name in os.listdir(source) if os.path.isfile(os.path.join(source, name))])
    return total_number_files

def main_menu():
    print("Welcome to Paul's SD Card Jukebox Generator\n")
    source = input("Please enter the source directory for your music store:  ") + "/"
    destination = input("Please enter the destination directory of your SD card:  ") + "/"
    percentage_fill = input("Please enter the % (as int e.g.10 for 10%) of remaining space on your card you wish to fill:  ")
 
    while  True:
        total, used, free = shutil.disk_usage(destination)
        get_dest_capacity = (total * (int(percentage_fill)/100))
        random_file = random.choice(os.listdir(source))
        random_file_size = os.path.getsize(source + random_file)
        if random_file_size < (get_dest_capacity - used):
            source_file = source + random_file
            try:
                shutil.copytree(source_file, destination + random_file +"/")
                files_added = (files_added + random_file_size)
            except:
                pass
        else:
            break
    print("Random File Transfer Complete")

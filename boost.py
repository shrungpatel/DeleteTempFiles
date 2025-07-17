import os
import psutil
import time
import shutil

TEMP_USAGE_THRESHOLD_MB = 100
CHECK_INTERVAL = 600 # 10 minutes

def clear_temp_files(temp_dir):
    """Clear files in the temporary directory"""
    #temp_dir = os.environ.get('TEMP', 'C:\\Windows\\Temp')
    temp_files = os.listdir(temp_dir)
    #old += get_temp_memory_usage(temp_dir)
    for temp_file in temp_files:
        file_path = os.path.join(temp_dir, temp_file)
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)
                #print('Removed file')
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
                #print('Removed dir')
        except Exception as e:
            continue
            #print('Couldn\'t remove')
    #new += get_temp_memory_usage(temp_dir)

def get_temp_memory_usage(temp_dir):
    """Get current temporary memory usage"""
    temp_files = os.listdir(temp_dir)
    temp_usage = 0

    # size of all files in the temporary directory
    for temp_file in temp_files:
        file_path = os.path.join(temp_dir, temp_file)
        if os.path.isfile(file_path):
            temp_usage += os.path.getsize(file_path)

    return temp_usage / (1024 * 1024)  # convert to MB

def boost_performance_sometimes():
    """Check the memory usage and clear temp files if necessary.
       Keeps running in the background."""
    while True:
        #temp_usage = get_temp_memory_usage()
        #print(f"Temporary memory usage before clearing: {temp_usage:.2f} MB")
        if get_temp_memory_usage() >= TEMP_USAGE_THRESHOLD_MB:
            clear_temp_files()
            #temp_usage = get_temp_memory_usage()
            #print(f"Temporary memory usage after clearing: {temp_usage:.2f} MB")
        time.sleep(CHECK_INTERVAL)
    
if __name__ == "__main__":
    temp_dirs = ['C:\\Windows\\Temp', os.environ.get('TEMP', 'C:\\Windows\\Temp')]
    [clear_temp_files(temp_dir) for temp_dir in temp_dirs]
    #print('Deleted', old - new, 'MB')
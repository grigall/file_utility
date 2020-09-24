path = None

def run_program(path):
    import os
    
    class FileFolder:
        def __init__(self, name, path, contents, sub_dir):
            self.name = name
            self.path = path
            self.contents = contents
            self.sub_dir = sub_dir
    
    def scan_dir(path):
        file_list = []

        with os.scandir(path) as files:
            for i in files:
                file_list.append(i.name)

        file_list.sort()
        return file_list

    def parse_dir(file_list):
        sub_dir = [] #local list for sub-directories
        file_types = [] #local list for unique file types
        files = [] #list for files in the current folder

        #Find sub-directories
        for i in file_list:
            if r"." not in i:
                sub_dir.append(i)
            elif r"." in i:
                file_types.append(i[i.find("."):])
                files.append(i)

        sub_dir.sort()

        return sub_dir, files, list(set(file_types)) #Provides list of sub-directories and unique file types for later iteration

    def sub_dir_search(sub_dir_list):
        if len(sub_dir_list) != 0:
            for i in sub_directories:
                new_folder = FileFolder(i, path + '\\' + i, None, None)
                new_folder.contents = scan_dir(new_folder.path)
                master_list.append(new_folder)
        else:
            pass
    
    #Global variable for debugging
    global master_list
    master_list = []
    
    #Initial directory scan
    initial_scan = scan_dir(path)
    
    #Initiates master list
    if len(initial_scan) > 0:
        #Initial directory parse
        sub_directories, files, file_types = parse_dir(initial_scan)
        
        if len(files) > 0 and len(sub_directories) > 0:
            new_folder = FileFolder(path[3:], path, None, sub_directories)
            new_folder.contents = files
            master_list.append(new_folder)
        elif len(files) > 0 and len(sub_directories) == 0:
            new_folder = FileFolder(path[3:], path, None, None)
            new_folder.contents = files
            master_list.append(new_folder)
        else: #If files is equal to zero, this will pass to the sub-dir check
            pass 
    
        if len(sub_directories) > 0:
            sub_dir_search(sub_directories)
        
    else:
        input("This folder contains no files or sub-folders. Press enter to continue...")
        pass
    

    
    
    
    return sub_directories, files, file_types
import os

def createFile(filename):
    open(filename, 'w')
    print("[+] Generated file "+filename)

def createDirectory(path, foldername):
    os.mkdir(path + foldername + "/")
    print("[+] Generated directory "+ foldername)
    

def generate(folder, task):
    inPath =  f"C:/Users/{os.getlogin()}/Documents/"
    path = f"C:/Users/{os.getlogin()}/Documents/Work-index/"
    folder = "/" + folder
    task = "/" + task
    
    if not os.path.isdir(path):
        createDirectory(inPath, "Work-index")
        
    if os.path.isdir(path + folder):
        os.chdir(path + folder)
        
    else:
        createDirectory(path, folder)
        os.chdir(path + folder)

    if os.path.isdir(path + folder + task):
        print("[!] task code already exists!")
        
    else:
        createDirectory(path + folder, task)
        os.chdir(path + folder + task)
        createDirectory(path + folder + task, '/attachments')
        createFile('description.txt')
        createFile('branches.txt')
        createFile('report.txt')
        
def generate_only_folders(folder):
    inPath =  f"C:/Users/{os.getlogin()}/Documents/"
    path = f"C:/Users/{os.getlogin()}/Documents/Work-index/"
    folder = "/" + folder
    
    if not os.path.isdir(path):
        createDirectory(inPath, "Work-index")
        
    if os.path.isdir(path + folder):
        os.chdir(path + folder)
        
    else:
        createDirectory(path,folder)
        os.chdir(path + folder)
        createFile('readme.txt')
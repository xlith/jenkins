# Create a file and write system information to it
import platform
import os

def create_dir(dirname):
    if not os.path.exists(dirname):
        os.makedirs(dirname)


def create_file(dirname, filename):
    with open(os.path.join(dirname, filename), 'w') as f:
        f.write("System information\n")
        f.write("===================\n")
        f.write("\n")
        f.write("Platform: " + platform.platform() + "\n")
        f.write("\n")
        f.write("Version: " + platform.version() + "\n")
        f.write("\n")
        f.write("Machine: " + platform.machine() + "\n")
        f.write("\n")
        f.write("Processor: " + platform.processor() + "\n")
        f.write("\n")
        f.write("Python version: " + platform.python_version() + "\n")
        f.write("\n")
        f.write("System: " + platform.system() + "\n")
        f.write("\n")
        f.write("Architecture: " + platform.architecture()[0] + "\n")
        f.write("\n")
        f.write("Platform: " + platform.platform() + "\n")
        f.write("\n")
        f.write("Version: " + platform.version() + "\n")
        f.write("\n")
        f.write("Machine: " + platform.machine() + "\n")
        f.write("\n")
        f.write("Processor: " + platform.processor() + "\n")
        f.write("\n")
        f.write("Python version: " + platform.python_version() + "\n")
        f.write("\n")
        f.write("System: " + platform.system() + "\n")
        f.write("\n")
        f.write("Architecture: " + platform.architecture()[0] + "\n")
        f.write("\n")
        f.write("Platform: " + platform.platform() + "\n")
        f.write("\n")
        f.write("Version: " + platform.version() + "\n")
        f.write("\n")


create_dir("build")
create_file("build", "build_info.txt")

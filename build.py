# Create a file and write system information to it
import platform
import datetime

def version():
    ct = datetime.datetime.now()
    with open("version.txt", "w") as v:
        v.write(ct)
        v.write("\n")

def create_file(filename):
    with open(filename, 'w') as f:
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

version()
create_file("build_info.txt")

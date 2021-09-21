import SnapCore
from SnapCore import SnapFile
from SnapCore import SnapData

FILE = "src/Main.sb"
PROJECT_NAME = "Test"

def main():
    sf = SnapFile(FILE)    
    sd = SnapData(sf)
    

if __name__ == "__main__": 
    main()

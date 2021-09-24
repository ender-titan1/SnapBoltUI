import SnapCore
from SnapCore import SnapFile
from SnapCore import SnapData
from Webpage import Webpage, Html, HtmlTagConverter

FILE = "src/Main.sb"
PROJECT_NAME = "Test"

def main():
    sf = SnapFile(FILE)    
    sd = SnapData(sf)

    sd.main.generate_children()

    print(sd.main.context.children)

    """page = Webpage()
    for tag in sd.tags:
        page.html.tags["root"].append(Html(
            HtmlTagConverter[tag.content],
            Webpage.gen_random_class()
        ))

    print(page.html.tags)"""

    

if __name__ == "__main__": 
    main()

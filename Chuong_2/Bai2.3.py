import xml.dom.minidom

def main():
    doc = xml.dom.minidom.parse("c:/Users/ADMIN/OneDrive/Máy tính/Python/Chuong_2/sample.xml")
    print(doc.nodeName)
    print(doc.firstChild.tagName)
if __name__=="__main__":
    main()
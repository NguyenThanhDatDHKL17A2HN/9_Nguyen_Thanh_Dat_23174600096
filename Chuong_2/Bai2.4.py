import xml.dom.minidom

doc = xml.dom.minidom.parse("sample.xml")
staffs = doc.getElementsByTagName("staff")

for staff in staffs:
    name = staff.getElementsByTagName("name")[0].firstChild.data
    salary = staff.getElementsByTagName("salary")[0].firstChild.data
    print(f"Name: {name}")
    print(f"Salary: {salary}")
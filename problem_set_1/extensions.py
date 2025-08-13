"""
.gif image/gif
.jpg image/jpeg
.jpeg image/jpeg
.png image/png
.pdf  application/pdf
.txt text/plain
.zip application/zip
application/octet-stream
"""

def main():
    file_name=input("File name: ").strip().lower()
    extension(file_name)

def extension(file):
    extension_name = file.split('.')[1]
    match extension_name:
        case "jpg" | "jpeg":
            print("image/jpeg")
        case "gif" | "png":
            print("image/", extension_name, sep="")
        case "pdf" | "zip":
            print("application/", extension_name, sep="")
        case "txt":
            print("text/plain")
        case _:
            print("application/octet-stream")

main()
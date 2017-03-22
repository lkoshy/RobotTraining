def read_file(path, binary=False):
    mode = 'r' if not binary else 'rb'
    with open(path, mode) as file:
        return file.read()# return bytes in Py 3


def write_file(path, content, binary=False):
    mode = 'w' if not binary else 'wb'
    with open(path, mode) as file:
        file.write(content)
        # l.f char is not converted to c.r in write binary mode


def read_open_file(file):
    return file.read()


def write_open_file(file, content):
    file.write(content)




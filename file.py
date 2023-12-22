import codecs
def write_file(file:str, data, encoding:str='latin-1')->str:
    file = codecs.open(filename=file, encoding=encoding,mode='w')
    file.write(data)
    file.close()
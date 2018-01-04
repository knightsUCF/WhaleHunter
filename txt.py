


class TXT():


    def write(self, file, data):
        f = open(file,'w')
        f.write(data)
        f.close()



    def read(self, file):
        f = open(file,'r')
        data = f.read()
        return data


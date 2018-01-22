import datetime

now = datetime.datetime.now()



class TXT():


    def write(self, file, text):
        f = open(file,'w')
        current_time = str(now.strftime("%Y-%m-%d %H:%M"))
        write_info = current_time + ' -- ' + text
        f.write(write_info)
        f.close()



    def write_next_line(self, file, text):
        f = open(file, 'a')
        f.write('\n\n')
        current_time = str(now.strftime("%Y-%m-%d %H:%M"))
        write_info = current_time + ' -- ' + text
        f.write(write_info)
        f.close()



    def read(self, file):
        f = open(file,'r')
        data = f.read()
        return data


from ftplib import FTP
ftp=FTP('server.ip')
ftp.login('username','password')
ftp.cwd("path for your projecy")
filename='a.txt'
myfile=open(filename,'wb')
ftp.retrbinary('RETR ' + filename, myfile.write, 1024) 
ftp.quit()
myfile.close()
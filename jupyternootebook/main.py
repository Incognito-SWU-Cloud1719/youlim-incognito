import subprocess
import os

os.system('sudo ufw allow 21')
subprocess.call('git clone https://github.com/nikdubois/vsftpd-2.3.4-infected.git', shell = True)
os.system('sudo apt-get install build-essential')
os.system('sudo rm vsftpd-2.3.4-infected/Makefile')
os.system('mv Makefile vsftpd-2.3.4-infected/')
os.system('sudo chmod 777 vsftpd-2.3.4-infected/vsf_findlibs.sh')
os.system('ls')
os.chdir('vsftpd-2.3.4-infected')
os.system('ls')
os.system('make')
os.system('ls -lha vsftpd')
os.system('useradd nobody')
os.system('sudo mkdir /usr/share/empty')
os.system('sudo cp vsftpd /usr/local/sbin/vsftpd')
os.system('sudo cp vsftpd.8 /usr/local/man/man8')
os.system('sudo cp vsftpd.conf.5 /usr/local/man/man5')
#os.system('sudo cp vsftpd.conf /etc')
#os.system('sudo /usr/local/sbin/vsftpd &')
# os.system('ftp localhost')
os.system('sudo mkdir /var/ftp/')
os.system('sudo useradd -d /var/ftp ftp')
os.system('sudo chown root:root /var/ftp')
os.system('sudo chmod og-w /var/ftp')
#os.system('sudo rm /etc/vsftpd.conf')
#test
os.system('pwd')
os.chdir('/')
os.system('sudo mv vsftpd.conf /etc/')
os.system('sudo chown root vsftpd.conf')
os.chdir('/var/run/')
os.system('sudo mkdir vsftpd')
os.chdir('vsftpd')
os.system('sudo mkdir empty')
os.chdir('/')
os.system('sudo /usr/local/sbin/vsftpd &')

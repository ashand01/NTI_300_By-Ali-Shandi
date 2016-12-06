import os

def set-up-git():
   print('install git')
   os.system('sudo yum -y install git')
   
   print('instally my reposoitory')
   os.sytem('git clone https://github.com/ashand01/NTI_300_By-Ali-Shandi.git')
   

set-up-git()

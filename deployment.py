#!/usr/bin/python

import boto3
import base64
import pprint

ec2 = boto3.resource('ec2')
client = boto3.client('ec2')

amazon_image = 'ami-6f68cf0f'                                       # This will launch a red hat instance
amazon_instance = 't2.micro'                                        # we've been working with micro's, if you use Amizon Linux, you could launch a nono
amazon_pem_key = 'Redhat300'                    # the name of the key/pem file you would like to use to access this machine
firewall_profiles = ['launch-wizard-6']                             # the security group name(s) you would like to use, remember, this is your firewall, make sure the ports you want open are open

print(amazon_image)
print(amazon_instance)
print(amazon_pem_key)

def launch_test_instance():

   instances = ec2.create_instances(
      ImageId = amazon_image,
      InstanceType = amazon_instance,
      MinCount=1,
      MaxCount=1,
      KeyName = amazon_pem_key,
      SecurityGroupIds = firewall_profiles,
      UserData="""#!/usr/bin/python





# Github.py
import sys, os
def set_up_git():
   print('install git')
   os.system('yum -y install git')
   
   print('clone my reposotory')
   os.system('git clone https://github.com/ashand01/NTI_300_By-Ali-Shandi.git /tmp/NTI_300_By-Ali-Shandi')
set_up_git()

sys.path.append('/tmp/NTI_300_By-Ali-Shandi')
import apache
apache.install_apache()




#Django 

#!/bin/bash

echo "Current version of Python:"

python --version

echo "Installing virtualenv to give Django it's own version of Python..."

rpm -iUvh https://dl.fedoraproject.org/pub/epel/7/x86_64/e/epel-release-7-8.noarch.rpm
yum -y install python-pip

pip install virtualenv
cd /opt

mkdir django
chown -R ec2-user django
sleep 5
cd django
virtualenv django-env

echo "Activating virtualenv..."

source /opt/django/django-env/bin/activate

echo "To switch out of virtualenv, type deactivate."

echo "Now using this version of Python:"

which python
sudo chown -R ec2-user /opt/django

echo "installing django"

sudo pip install Django

echo "Django admin is version:"

django-admin --version
django-admin startproject project1

echo "This is the new django project directory..."

tree project1

echo "Go to https://docs.djangoproject.com/en/1.10/intro/tutorial01/ to begin first Django Project!"

#crontab.py

import os
def mailx():
   print('Installing mailx')
   os.system('yum -y install mailx')

mailx()

import os
def crontab():
   print('Creating crontab entry for Server Alert emails every 30 minutes.')
   os.system('chmod +x /python_deployment/server_alert.sh')
   os.system('(crontab -l 2>/dev/null; echo "0,30 * * * * /python_deployment/server_alert.sh | mail -s \"Server Alert\"ali6302@gmail.com") | crontab - ')
   os.system('crontab -l')

crontab()

def start_django():
  print('Starting the Django Web Server')
  os.system('python /django/project1/manage.py runserver 0.0.0.0:8000&')
start_django()
"""

   )

   pprint.pprint(instances)


launch_test_instance()














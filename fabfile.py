from __future__ import with_statement
import os, sys, time, getpass
from fabric.api import *
from fabric.colors import red, green, blue, cyan, magenta, white, yellow
from fabric.api import put, run, settings, sudo
from fabric.operations import prompt
from fabric.contrib import django


env.VENDOR_PATH = 'vendor'
env.REMOTE_CODEBASE_PATH		= '/home/ubuntu/josephmisiti.com'
env.PIP_REQUIREMENTS_PATH		= 'requirements.txt'
env.GUNICORN_PID_PATH			= os.path.join(
    env.REMOTE_CODEBASE_PATH, 'logs/gunicorn.pid')
env.PROJECT_PATH				= os.path.dirname(os.path.abspath(__file__))
env.FETCHER_PROJECT_PATH		= env.REMOTE_CODEBASE_PATH
env.BRANCH_NAME					= 'master'
env.user						= 'ubuntu'
env.key_filename				= '/Users/%s/.ssh/id_rsa' % getpass.getuser()

env.roledefs = {
	'website'  : ['52.7.89.116'],
}

def install_supervisor():
    sudo("mkdir -p /mnt/logs/supervisor/")
    sudo("chown ubuntu.ubuntu /mnt/logs/supervisor/")
    sudo('apt-get -y install supervisor')
    sudo('/etc/init.d/supervisor stop')
    sudo('sleep 2')
    sudo('/etc/init.d/supervisor start')
    

def setup_installs():
    """ Installs apt-get packages """
    packages = [
        'build-essential',
        'gcc',
        'libreadline-dev',
        'libpcre3-dev',
        'libssl-dev',
        'sysstat',
        'iotop',
        'git',
        'python-dev',
        'python-pip',
        'locate',
        'python-software-properties',
        'software-properties-common',
        'libpcre3-dev',
        'libncurses5-dev',
        'libdbd-pg-perl',
        'libssl-dev',
        'make',
        'libyaml-0-2',
        'python-setuptools',
        'curl',
        'golang',
    ]
    sudo('apt-get -y update')
    sudo('DEBIAN_FRONTEND=noninteractive apt-get -y --force-yes upgrade')
    sudo('DEBIAN_FRONTEND=noninteractive apt-get -y --force-yes install %s' % ' '.join(packages))


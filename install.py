import subprocess
import os
import sys
import platform

def command_exists(cmd):
    try:
        subprocess.check_output(['which', cmd], stderr=subprocess.STDOUT)
        return True
    except:
        return False

system = platform.system()
if system != 'Linux':
    raise OSError("This script only supports Linux for Node.js installation.")

node_installed = command_exists('node')
npm_installed = command_exists('npm')

if not node_installed or not npm_installed:
    subprocess.run("curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo -E bash -", shell=True, check=True)
    subprocess.run("sudo apt-get install -y nodejs", shell=True, check=True)

subprocess.run(['npm', 'install', 'puppeteer-real-browser', 'hpack', 'colors'])
subprocess.run(['npx', '@puppeteer/browsers', 'install', 'chrome@stable'])
chrome_path = subprocess.check_output(['npx', '@puppeteer/browsers', 'path', 'chrome@stable']).decode().strip()
chrome_dir = os.path.dirname(chrome_path)
current_path = os.environ.get('PATH', '')
os.environ['PATH'] = chrome_dir + os.pathsep + current_path
subprocess.run(['node', 'Gravitus.js'])
script_path = os.path.abspath(sys.argv[0])
subprocess.run(['rm', '-rf', script_path])

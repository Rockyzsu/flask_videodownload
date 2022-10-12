import subprocess
from task.config import youget_path,target_folder
def download(link, filename):
    if 'youtube' in link:
        # 下载youtube
        cmd = 'python  {} -o {} -O {} {}'
        command = cmd.format(youget_path,target_folder, filename, link)
    else:
        cmd = 'wget {} -O {}/{}'
        command = cmd.format(link, target_folder,filename)

    try:
        p = subprocess.Popen(command.split(), shell=False, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    except Exception as e:
        return False
    else:
        p.wait()
        return True



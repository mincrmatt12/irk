import subprocess


def run(args):
    proc = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
    all_stdout = ""
    while proc.poll() is None:
        new_content = proc.stdout.read(16)
        all_stdout += new_content
        print(new_content, end="")
    return proc.returncode, all_stdout

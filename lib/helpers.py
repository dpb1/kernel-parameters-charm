import os
import shutil
import subprocess


def write_sysctl(params, path):
    """Write sysctl file from params, unlink first if exists."""
    if os.path.exists(path):
        shutil.rmtree(path)
    with open(path, 'w') as f:
        for param in params.split(";"):
            f.write("%s\n" % param.strip())


def load_sysctl_file(path):
    """Load the given sysctl file."""
    subprocess.check(["sysctl", "-p", path])

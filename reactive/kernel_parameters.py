import os
import shutil
import subprocess
from charms.reactive import when_not, set_state
from charmhelpers.core import hookenv

SYSCTL_FILE = "/etc/sysctl.d/90-kernel-parameters-charm"


@when_not('kernel-parameters.installed')
def install_kernel_parameters():
    params = hookenv.config("kernel-parameters")
    hookenv.log(
        "Writing Kernel Parameters to file: %s \n"
        "  Params: (Will split/strip first): %s" % (SYSCTL_FILE, params))
    write_sysctl(params, SYSCTL_FILE)
    load_sysctl_file(SYSCTL_FILE)
    set_state('kernel-parameters.installed')


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

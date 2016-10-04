from charms.reactive import when_not, set_state
from charmhelpers.core import hookenv

from lib.helpers import write_sysctl, load_sysctl_file

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

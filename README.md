Kernel Parameters Charm
-----------------------

This simple subordinate charm can be useful for setting kernel
parameters through sysctl(8) and having them be maintained across
reboots.

Usage
-----

Sample Bundle:

    services:
      ubuntu:
        series: trusty
      kernel-parameters:
        series: trusty
        options:
          kernel-parameters: kernel.shmmax=2147483648 net.ipv4.ip_forward=1
    relations:
      - ["ubuntu", "kernel-parameters"]

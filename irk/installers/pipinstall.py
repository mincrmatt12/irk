from .common import InstallerState, Installer
from ..util import proc


class PipInstaller(Installer):
    def __init__(self, package_name, version):
        self.executable = "pip" + version
        self.package = package_name

    def install(self, dry_run):
        arg_string = [
            "/usr/bin/env", self.executable, "install", self.package
        ]
        if dry_run:
            print("Would run {}".format(" ".join(arg_string)))
            return InstallerState.OK
        print(f"Running {' '.join(arg_string)}")
        code, stdout = proc.run(arg_string)
        if code == 0:
            return InstallerState.OK
        elif "[Errno 13]" in stdout:
            return InstallerState.NEEDS_SUDO
        elif "No matching distribution" in stdout:
            return InstallerState.INVALID_NAME
        else:
            return InstallerState.FAILED

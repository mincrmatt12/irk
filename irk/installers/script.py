import os
import tempfile

from irk.installers.common import Installer, InstallerState
from irk.util import proc


class ScriptInstaller(Installer):
    def __init__(self, script_contents, package):
        self.script_contents = script_contents
        self.package = package

    def install(self, dry_run):
        if dry_run:
            print("Would run a custom script, unable to show contents.")
            return InstallerState.OK
        with tempfile.NamedTemporaryFile("w") as f:
            f.write(self.script_contents)
            os.chmod(f.name, 0o775)
            code, stdout = proc.run(f.name + " " + self.package)
            if code == 0:
                return InstallerState.OK
            if code == 101:
                return InstallerState.INVALID_NAME
            return InstallerState.FAILED

    def remove(self, dry_run):
        print("NOTIMPL: You can't remove script-based things yet..")

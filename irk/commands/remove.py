from irk.installers.common import InstallerState
from irk.util.proc import elevate
from irk.util.storage import resolv


def remove(package, specific_resolver=None, dry_run=False):
    for resolver in resolv.get_matching_resolvers(package):
        if specific_resolver is None or resolver.get_resolver_name() == specific_resolver:
            print(f"Using resolver {resolver.get_resolver_name()}")
            code = resolver.resolve_to_installer(package).remove(dry_run)
            if code == InstallerState.OK:
                print("Removed {}".format(package))
                return 0
            elif code == InstallerState.INVALID_NAME:
                print("Trying next resolver...")
                continue
            elif code == InstallerState.FAILED:
                return 1
            elif code == InstallerState.NEEDS_SUDO:
                print("ERR: You probably need to run me as sudo!")
                elevate()
                return 1
    print("ERR: Invalid package!")
    return 2
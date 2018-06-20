from irk.installers.common import InstallerState
from irk.util.storage import resolv


def try_to_install(resolver, package, dry_run):
    installer = resolver.resolve_to_installer(package)
    for dep in installer.get_dependencies():
        print("Installing dependency {}".format(dep))
        install(dep, dry_run)
    code = installer.install(dry_run)
    if code == InstallerState.HAS_DEPS:
        print("WARN: Detected dependency errors, attempting to installing dependencies")
        for dep in installer.get_dependencies():
            print("Installing dependency {}".format(dep))
            install(dep, dry_run)
        code = installer.install(dry_run)
    return code


def install(package, specific_resolver=None, dry_run=False):
    for resolver in resolv.get_matching_resolvers(package):
        if specific_resolver is None or resolver.get_resolver_name() == specific_resolver:
            print(f"Using resolver {resolver.get_resolver_name()}")
            code = try_to_install(resolver, package, dry_run)
            if code == InstallerState.OK:
                print("Installed {}".format(package))
                return 0
            elif code == InstallerState.INVALID_NAME:
                print("Trying next resolver...")
                continue
            elif code == InstallerState.FAILED:
                return 1
            elif code == InstallerState.NEEDS_SUDO:
                print("ERR: You probably need to run me as sudo!")
                return 1
    print("ERR: Invalid package!")
    return 2

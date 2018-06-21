import click
from .commands.update import update as update_impl
from .commands.install import install as install_impl
from .commands.remove import remove as remove_impl
from .util.version import VERSION_STRING, COPYRIGHT


@click.group(invoke_without_command=True)
@click.option("-v", "--version", is_flag=True, help="Print version information")
def main(version):
    if version:
        print(f"version {VERSION_STRING}\n{COPYRIGHT}")
        exit(0)


@main.command()
def update():
    update_impl()


@main.command()
@click.option("--dry-run/--no-dry-run", help="Print commands/actions to be ran")
@click.option("-r", "--resolver", default=None, type=str, help="Use this resolver specifically")
@click.argument("name")
def install(dry_run, resolver, name):
    exit(install_impl(name, resolver, dry_run))


@main.command()
@click.option("--dry-run/--no-dry-run", help="Print commands/actions to be ran")
@click.option("-r", "--resolver", default=None, type=str, help="Use this resolver specifically")
@click.argument("name")
def remove(dry_run, resolver, name):
    exit(remove_impl(name, resolver, dry_run))
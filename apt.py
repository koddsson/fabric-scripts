from fabric.colors import red, green
from fabric.api import task, sudo, quiet, env


@task
def apt_install(package_name):
    """Install a package using apt-get package manager"""
    cmd = 'apt-get install {package_name}'.format(package_name=package_name)
    results = sudo(cmd, quiet=True)
    if not results.succeeded:
        print(red(results))
        print(red('[{host}] Installing {package_name} failed'.format(
            host=env.host, package_name=package_name)))
    else:
        print(green('[{host}] Installing {package_name} succeeded'.format(
            host=env.host, package_name=package_name)))


@task
def apt_is_installed(package_name):
    cmd = 'dpkg -s {package_name} | grep "install ok installed"'.format(
        package_name=package_name)
    results = sudo(cmd, quiet=True)
    if results.succeeded:
        print(green('[{host}] {package_name} is installed'.format(
            host=env.host, package_name=package_name)))
    else:
        print(red('[{host}] {package_name} is not installed'.format(
            host=env.host, package_name=package_name)))

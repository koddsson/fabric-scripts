from fabric.colors import red, green
from fabric.api import task, sudo, quiet


@task
def apt_install(package_name):
    """Install a package using apt-get package manager"""
    cmd = 'apt-get install {package_name}'.format(package_name=package_name)
    results = sudo(cmd, quiet=True)
    if not results.succeeded:
        print(red(results))
        print(red('Installing {package_name} failed'.format(
            package_name=package_name)))
    else:
        print(green('Installing {package_name} succeeded'.format(
            package_name=package_name)))

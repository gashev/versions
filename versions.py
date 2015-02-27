from distutils.version import LooseVersion
import json
import requests
import sys

def versions(package_name):
    """Get sorted versions list for the package from the pypi.

    :param package_name: string package name
    :return: list
    """

    url = "https://pypi.python.org/pypi/%s/json" % (package_name)
    data = json.loads(requests.get(url).text)
    versions = data["releases"].keys()
    versions.sort(key = LooseVersion)

    return versions

def main():
    if (len(sys.argv) != 2):
        sys.stderr.write("Usage: %s PACKAGE\n" % (sys.argv[0]))
        return 1

    try:
        print("\n".join(versions(sys.argv[1])))
    except Exception as e:
        sys.stderr.write("Error: %s\n" % (e.message))
        return 1

    return 0

if __name__ == "__main__":
    sys.exit(main())

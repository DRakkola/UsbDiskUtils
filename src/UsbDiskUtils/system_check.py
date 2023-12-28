import platform
import sys

def get_sys_info():
    python_version = sys.version.split('\n')
    dist_info = str(platform.platform())
    system = platform.system()
    machine = platform.machine()
    platform_info = platform.platform()
    uname_info = platform.uname()
    version_info = platform.version()
    mac_version_info = platform.mac_ver()

    return {
        "Python version": python_version,
        "Distribution": dist_info,
        "System": system,
        "Machine": machine,
        "Platform": platform_info,
        "Uname": uname_info,
        "Version": version_info,
        "Mac version": mac_version_info
    }


def print_python_info(info_dict):
    print("Python Information:")
    for key, value in info_dict.items():
        print(f"{key}: {value}")
    print()

if __name__ == "__main__":
    python_info = get_sys_info()
    print_python_info(python_info)

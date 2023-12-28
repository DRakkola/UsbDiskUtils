from system_check import get_sys_info


if get_sys_info()['System'] == 'Darwin':        
    from macOS import UsbDiskUtils


    def test(nbr):
        print('something happened ....', nbr)

    if __name__ == "__main__":
        # Example usage
        usb_disk_utils = UsbDiskUtils(test, name="NIDHAL", path="YourPath", kind="YourKind")
        usb_disk_utils.run_monitoring()
        
else: 
    print(get_sys_info()['System'],'Not yet supported !! ')
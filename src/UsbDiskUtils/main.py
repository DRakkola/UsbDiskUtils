from system_check import get_sys_info


if get_sys_info()['System'] == 'Darwin':        
    from macOS import UsbDiskUtils

    # Example usage:
    def custom_callback(line):
        print(f"Custom Callback: {line}")


    if __name__ == "__main__":
        # Example usage
        usb_disk_utils = UsbDiskUtils()
        print(f"Starting monitoring...")
        worker_id = usb_disk_utils.start_worker(name="NIDHAL", callback=custom_callback)

        # You can stop the worker using its ID
        #usb_disk_utils.stop_worker(worker_id)
        
else: 
    print(get_sys_info()['System'],'Not yet supported !! ')
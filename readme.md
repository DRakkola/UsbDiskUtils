# UsbDiskUtils

UsbDiskUtils is a Python library designed to handle USB disk events, allowing users to execute tasks or run custom code upon the insertion or removal of USB disks. While the initial release focuses on macOS support, future updates are planned to extend compatibility to other operating systems.

## System Compatibility

UsbDiskUtils checks the system information using the `get_sys_info` module. The library includes specific implementations based on the detected operating system.

## Example usage

```python

    from macOS import UsbDiskUtils

    def custom_callback(line):
        print(f"Custom Callback: {line}")


    if __name__ == "__main__":
        # Example usage
        usb_disk_utils = UsbDiskUtils()
        print(f"Starting monitoring...")
        # you can launch more than one worker to handle multiple events/Usb drives at the same time
        worker_id = usb_disk_utils.start_worker(name="NIDHAL", callback=custom_callback)

        # You can stop the worker using its ID
        #usb_disk_utils.stop_worker(worker_id)


```

## Features

- macOS Support: UsbDiskUtils is optimized for macOS, offering a reliable solution for USB disk event handling on Apple's operating system.
- Event-Driven Architecture: Leverage the event-driven design to respond dynamically to USB disk events, enabling flexible and customizable workflows.
- Simplified Integration: The library provides an easy-to-use API for seamless integration into your projects, ensuring swift implementation of USB disk event monitoring.

## Roadmap

- Future releases will expand UsbDiskUtils to support additional operating systems, ensuring a comprehensive solution for USB disk event management across various platforms.


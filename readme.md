# UsbDiskUtils

UsbDiskUtils is a Python library designed to handle USB disk events, allowing users to execute tasks or run custom code upon the insertion or removal of USB disks. While the initial release focuses on macOS support, future updates are planned to extend compatibility to other operating systems.

## System Compatibility

UsbDiskUtils checks the system information using the `get_sys_info` module. The library includes specific implementations based on the detected operating system.

## Example usage

```python

    from macOS import UsbDiskUtils

    #add logic that you want to trigger on usb dick (pluged)
    def test():
        print('Something happened....')

    if __name__ == "__main__":
        # Example usage on macOS
        usb_disk_utils = UsbDiskUtils(test, name="NIDHAL", path="YourPath", kind="YourKind")
        usb_disk_utils.run_monitoring()


```

## Features

- macOS Support: UsbDiskUtils is optimized for macOS, offering a reliable solution for USB disk event handling on Apple's operating system.
- Event-Driven Architecture: Leverage the event-driven design to respond dynamically to USB disk events, enabling flexible and customizable workflows.
- Simplified Integration: The library provides an easy-to-use API for seamless integration into your projects, ensuring swift implementation of USB disk event monitoring.

## Roadmap

- Future releases will expand UsbDiskUtils to support additional operating systems, ensuring a comprehensive solution for USB disk event management across various platforms.


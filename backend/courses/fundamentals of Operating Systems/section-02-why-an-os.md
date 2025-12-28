# Why an OS

## Intro why an OS

- It's easier to deal with hardware and resources using an abstracted layer
- Without OS, we required to deal with so many different vendors, RAMs, so many different CPU architecture and so many different storage
- We deal with many and many devices. We needed a general purpose operating system that works on all of them
- An OS is very important to us to build an application

## Why do we need an Operating System
- Operating system is a Software
- Resources need to be managed
- Your apps talk to the OS
- Most OSs are general purpose
- Scheduling
    - OS manages scheduling processes to the CPU
    - Scheduling is critical
    - General purpose scheduling algorithm is so hard
    - If I know my workload is always going to be long running processes, then I know exactly what to do
    - Fair share of resources to all processes
        - CPU/Memory/IO
    - Bandwidth of the IO of the disk is so critical. You can see it in database tuning as well
    - For example, mySQL has InnoDB I/O capacity
- OS APIs abstracts the hardware. Like POSIX: Portable Operating System Interface
    - Your app works on any hardware
- OS is not a magic
- Understanding OS makes you a better engineer

## System Architecture

- System has resources
- The kernal is OS core component
- The kernal manages the resources
- CPU is where the actual execution happens
    - CPU:
        - Central Processing Unit
        - Consists of cores
        - Each core has a clock speed
        - Executes machine level instructions
- Memory:
    - Random Access Memory
    - Fast but volatile
    - Store process states and data
    - Limited
    - Slower than CPU cache
- Storage:
    - Persisted storage
    - HDD, SSD
    - Kernal has an interface which knows how to read or write SSD/HDD
    - NVME is a certain command set responsible for abstracting disk read and write to the Operating system
- Network:
    - Communicate with other hosts
    - NIC (Network Interface Controller)
    - Protocol Implementation
    - The NIC receives data bits at layer 2, the OS translates those packets to above layer
- Kernal:
    - The core of the OS
    - We focus in this course on the kernal tasks
    - Manages the resources
    - The OS is more than the kernal
        - GUI, command lines, UI and tooling
        - Distros is all about extra tooling
- File System:
    - Storage is mostly blocks of bytes
    - We like to work files
    - File system is an abstraction
    - Logical Block Addressing (LBA)
        - Disks are exposed as a big arrays of LBAs
        - Partitions start from LBA and end in an LBA
        - Provides logical segmentation
        - Each partition can have its own FS
    - How files stored on disk
    - btrfs, ext4, fat32, NTFS, tmpfs
- Program vs Process:
    - Program is the compiled executable
    - Process is an instance of the program
    - Process is a program in motion
    - Program is a process at rest
    - Execution file format: different OS have different executable file header and formats
- Process Management:
    - Kernal manages processes
    - Schedules process for a CPU
    - Switches a process for another
    - Grant access to resources like storage
- User space vs Kernal Space:
    - User space:
        - Browser
        - Postgres
    - Protected kernal space
        - Kernal code
        - Device drivers
        - TCP/IP stack
    - Isolated, (io_uring kind of broke that rule)
- Device drivers
    - Drivers are software in the kernal
    - Manages hardware devices
    - NVME, Keyboard, NIC, etc
    - Interrupt Service Routine
- System Calls:
    - To jump from User to Kernal mode
    - User makes a system call
    - Read() write() malloc()
    - Mode switch
    




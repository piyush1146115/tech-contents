# Section 3: The Anatomy of a Process

## Intro

You really don't need an operating system. But it is very useful for convenience. Writing an application that directly communicates with hardware is extremely difficult.

## Program vs Process

Process is a program in motion. 
Process has also a pointer called program counter. 

### Program:
- Code is compiled and linked for a CPU
- Dynamic Link Library
- Produces executable file program
- Only works on that CPU architecture

### Process
- When a program is run, we get a process
- Process lives in memory
- Uniquely identified with an id
- Instruction pointer/program counter: represents the current instruction to be executed
- Process Control Block (PCB) . PCB lives in memory. It stores metadata about the process. Tells you the file descriptor, tells you the program counter etc
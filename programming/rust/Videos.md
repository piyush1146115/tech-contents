# Videos related to Rust

- [How NOT to learn Rust](https://www.youtube.com/watch?v=2uY5tpcs3Gs)
    - Mistakes while learning Rust:
        - Writing Rust code like other languages
        - Neglecting the most important 20% of Rust
        - Being a productive procastinator
        - Thinking you can vibe code Rust
- [Will Crichton: Rust for Everyone!](https://www.youtube.com/watch?v=R0dP-QR5wQo&list=WL&index=73&t=224s)
    - Rust is a language empowering everyone to build reliable and efficient software
    - Rust combines systems programming and functional programming
    - How can we sysmetically empower more people to learn and use Rust? 
    - Rust uses its type system to ensure memory safety at compile-time
    - Investigate why programmers struggle with ownership
    - Develop a conceptual model and pedalogy of ownership
    - A brief intro to traits
    - As your dependencies get more complex, so your diagnostics
    - Cognitive science will be useful as long as humans have agency
    - Programming language theory helps us build reliable tooling

    - Tools:
        - Ownership visualization: Interactive diagrams showing permissions (read/write/own) that help students understand borrowing better than rule-based explanations
        - Trait debugging: [Argus](https://github.com/cognitive-engineering-lab/argus) A graphical tool for navigating complex trait inference trees when compiler errors become unreadably long
        -  Program slicing: [Flowistry](https://github.com/willcrichton/flowistry) Using Rust's type system to automatically highlight only code relevant to specific variables

- [Why Rust is different, with Alice Ryhl](https://youtu.be/q9xD36NCtZ8?si=qyK086AvCawNRFFP)
    - Memory safety
    - Crate and cargo
    - Crate is package in rust
    - Cargo is a all-rounder tool in rust. It can download packages, run code, generate doc, run tests, etc
    - For backend Rust is really a great fit, it's the strongest side of Rust
    - Rust is least matured in Frontend
    - Editions in Rust
    - Rust has a very good high backward compatability guarantee 
    - Rust is no more experimental in Linux Kernal
    - To learn a new language, you have to implement some project
    - The rust language book is a good resource to learn and work with Rust
    - For intermediate devs, Rust of Rustaceans is a nice book: https://rust-for-rustaceans.com/
    - Rustling exercises are also a good way to learn the language
- [Concurrency in Rust - Creating Threads](https://youtu.be/06WcsNPUNC8?si=D_linV9x58dnVZpT)
    - Green threads don't maintain 1:1 mapping with OS threads
    - Rust only includes OS threads or 1:1 threads in standard library
- [Concurrency in Rust - Message Passing](https://www.youtube.com/watch?v=FE1BkKqYCGU)
    - Using messages for sharing states across different threads
    - In go there is a proverb: "Do not communicate by sharing memory, instead share memory by communicating"
    - Rust has channel in standard libary for message passing bettween threads
    - A channel can contain a sender and a receiver
    - Here mpsc stands for multi producer, single consumer
    - 
```rs
use std::sync::mpsc;

fn main(){
   let (tx: Sender<{unknown}>, rx: Receiver<{unknown}>) mpsc::channel();

   thread::spawn(move || {
    let msg: String = String::from("hi");
    tx.send(msg).unwrap();
   });

   let received: String = rx.recv().unwrap();
   println!("Got: {}", received);
}
```
- [Concurrency in Rust - Sharing state](https://youtu.be/mupwF9jbVZ4?si=alMOc0w5Y4Ju7cuv)

```rs
use std::sync::Mutex;

fn main() {

    let m: Mutex<i32> = Mutex::new(5);

    {
        let mut num: MutexGuard<i32> = m.lock().unwrap();
        *num = 6;
    }

    println!("m = {:?}", m);
}
```
```rs
use std::sync::Mutex;
use std::thread;
use std::rc::Rc;

fn main() {
    let counter: Mutex<i32> = Rc::new(Mutex::new(0));
    let mut handles: Vec<{unknown}> = vec![];

    for _ in 0..10 {
        let counter: Rc<Mutex<i32>> = Rc::clone(self: &counter);
        let handle: JoinHandle<()> = thread::spawn(move || {
            let mut num: MutexGuard<i32> = counter.lock.unwrap();

            *num += 1;
        });

        handles.push(handle);
    }
}
```
- [The most trusted code on Earth is being rewritten in Rust](https://www.youtube.com/watch?v=Sntj4HmuykI&list=WL&index=4)

- [Generic Types in Rust](https://youtu.be/6rcTSxPJ6Bw?si=-9x_SHbRCTptH4r1)
    - Generics are great because they help us to reduce duplication

- [Rust's Module System Explained!](https://youtu.be/5RPXgDQrjio?si=54C5C2jZQmT1bZGo)
    - Rust module system starts with a package
    - A package stores crates
    - A crates can be library crates or binary crates
    - Crate cont
    - Rust has something called workspaces
    - By default, child modules can see what defined in parent module. But, parent module can not access child module contents by default
- [Rust is taking over the web](https://www.youtube.com/watch?v=TdDt7AiN6aw)
    - The web tooling for Javascript is being re-written in Rust
        - Example: Flow rewrite from Meta, Bun rewrite, Pyreflow from Meta
- [Rust is now one of the most popular languages in the world](https://youtu.be/meq4FxGvJCc?si=TGi-5YhrrQuCCiez)
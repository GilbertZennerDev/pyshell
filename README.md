🐚💻 PyShell — A Tiny Shell Written in Python!

Welcome to PyShell, my very own lightweight command-line shell written entirely in Python 🐍✨

It’s simple, powerful, and surprisingly functional — a great mix of Python logic and Unix spirit 💪

⚡ What It Does

PyShell gives you a mini interactive terminal, where you can:

✅ Navigate directories (cd, pwd)
✅ Run executables (./a.out)
✅ Launch Python scripts (.py)
✅ Use environment variables (echo $HOME)
✅ Exit cleanly with exit

Think of it as your tiny personal bash — but written in pure Python 🔥

🧠 Supported Commands
Command	Description
pwd	Prints the current working directory 📂
cd <dir>	Changes directory 📁
echo <text>	Prints text or environment variable 🗣️
python3 file.py	Runs Python scripts 🐍
./a.out	Executes compiled programs ⚙️
exit	Exits the shell 🚪

💡 You can also directly run other system commands — PyShell will pass them to subprocess automatically.

🚀 How to Run

1️⃣ Clone the repo:

git clone https://github.com/yourusername/pyshell.git
cd pyshell


2️⃣ Run it:

python pyshell.py


3️⃣ Try some commands:

pyshell: pwd
pyshell: cd ..
pyshell: echo $HOME
pyshell: ./a.out
pyshell: python3 script.py
pyshell: exit

💡 Example Session
pyshell: pwd
/home/user/projects

pyshell: cd ..
pyshell: pwd
/home/user

pyshell: echo $USER
myusername

pyshell: ./hello
Hello, World!

pyshell: exit

🧩 How It Works

🧱 Uses os for directory management
⚙️ Uses subprocess.run() for command execution
🐍 Interprets .py files directly through Python
💥 Clean error handling with the error() helper

You’re essentially building a shell interface from scratch — a perfect mix of Python and system-level fun 🧠💥

🌈 Why It’s Cool

✨ It’s minimal but extensible — you can add pipes, I/O redirection, or environment export next!
🧰 Great for learning how shells parse and execute commands
💬 A perfect side project for understanding os and subprocess in Python

🛠️ Future Ideas

🚀 Add command history (with readline)
🧩 Add autocomplete for directories and files
🧱 Support for environment variables and export
⚡ Add && and | chaining for advanced users

🤝 Contribute

Got ideas to improve PyShell? PRs welcome! 🙌
Add new commands, optimize parsing, or just make it fancier — this is your sandbox to play in 🎨

📜 License

🆓 MIT License — Free and open source.
Use it, modify it, and hack it however you like 💻💥

👨‍💻 Author

Made with ❤️ and curiosity by [Your Name]
💬 “Sometimes the best way to understand a system… is to build your own.” ⚙️🐍

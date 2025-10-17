# 🧠 MAC Address Changer 🛠️  
> A simple Python tool to change your MAC address directly from the terminal — fast, reliable, and beginner-friendly!

---

## 🌟 Features
✅ Change your MAC address in seconds  
✅ Colorful terminal output (Red ❌ & Green ✅ indicators)  
✅ Input validation for safety  
✅ Beginner-friendly structure and clean code  
✅ Works with Linux systems (`ifconfig` required)

---

## 🐍 Built With
- **Python 3**
- **subprocess**
- **optparse**
- **re (Regular Expressions)**
- **time**

---

## 🚀 Usage Guide

### 1️⃣ Clone or Download the Script
```bash
git clone https://github.com/YOUR-USERNAME/mac-changer.git
cd mac-changer
```
# Make sure you have the right permissions (use sudo if required)
```bash
sudo python3 mac_changer.py -i <interface> -m <new-mac-address>
```
## Example :
```bash
sudo python3 mac_changer.py -i eth0 -m 00:11:22:33:44:55
```
```
        | Option            | Description                    | Example             |
        | :---------------- | :----------------------------- | :------------------ |
        | `-i, --interface` | Specify your network interface | `eth0`, `wlan0`     |
        | `-m, --mac`       | New MAC address to assign      | `00:11:22:33:44:55` |
```

### 🧩 Code Overview

🔹 get_arguments()

    Parses command-line options (interface and mac) and validates inputs.

🔹 mac_changer(interface, mac)

    Uses ifconfig commands to:

        Turn the interface down

        Set a new MAC address

        Bring the interface back up

🔹 check_result(options)

    Checks if the MAC address was successfully changed and prints colored confirmation.

```bash
    [+] changing mac address to interface eth0 as : 00:11:22:33:44:55
    [+] Your MAC address is Changed to 00:11:22:33:44:55
    [+] MAC address changed Successfully ✅
```

### ⚠️ Notes

Works best on Linux 🐧

Run with sudo/root privileges

Ensure ifconfig is installed (sudo apt install net-tools)

# 🧑‍💻 Author

### Surya Prasath

💼 Python Developer | 🛡️ Cybersecurity Learner | Hacktivist

<a href="https://suryaprasath11.github.io/portfoilo-">Protfolio</a>


### 💖 Support

If you find this project helpful, give it a ⭐ on GitHub — it really motivates me! 🌟

---

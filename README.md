# WIFIHacker 🔓📶

An all-in-one WiFi pentesting tool designed to automate and simplify WiFi security auditing and attacks — phishing, SSID spam, DoS, and more. Built with ❤️ by [@karthithehacker](https://github.com/karthi-the-hacker)


![Logo](https://github.com/karthi-the-hacker/WIFIHacker/raw/refs/heads/main/images/Wifi_Haker.webp)


> ⚠️ Educational use only. Use responsibly and with permission.



## 📌 Features

- 📡 **WiFi Phishing** – Create fake access points with phishing login pages  
- 📶 **WiFi Spam** – Broadcast multiple fake SSIDs to confuse or overload nearby users  
- 🚫 **WiFi DoS** – *(Coming Soon)*  
- 📘 **Learn WiFi Hacking** – *(Coming Soon)*  
- 🔐 **View Captured Credentials**  




## ⚠️ Requirements

- A **WiFi card that supports monitor mode** is **mandatory**.
  
  This tool interacts directly with low-level network packets and wireless interfaces. Without monitor mode support, essential features like:
  
  - 📡 WiFi Phishing  
  - 📶 WiFi Spam  
  - 🚫 WiFi DoS  

  will not function properly.


### ✅ Recommended WiFi Adapters (Monitor Mode + Packet Injection Support)

| WiFi Adapter | Chipset | Monitor Mode | Packet Injection | Notes |
|--------------|---------|---------------|-------------------|-------|
| **Alfa AWUS036NHA** | Atheros AR9271 | ✅ | ✅ | One of the most recommended for Kali Linux |
| **Alfa AWUS036NH**  | Ralink RT3070  | ✅ | ✅ | Good range, stable |
| **TP-Link TL-WN722N** (v1 only) | Atheros AR9271 | ✅ | ✅ | Make sure to get **version 1** only |
| **Panda Wireless PAU06** | Ralink RT5372 | ✅ | ✅ | Works well out-of-the-box with Kali |
| **Alfa AWUS036ACH** | Realtek RTL8812AU | ✅ | ✅ | 5GHz support, may need driver install |
| **ASUS USB-AC68** | Realtek RTL8814AU | ✅ | ✅ | Powerful but may require manual driver setup |



> 💡 **Tip:** Before purchasing a WiFi adapter, always check chipset compatibility with **Kali Linux** or your preferred penetration testing OS.




## 📦 Tech Stack

- **Language:** Python 3
- **Libraries Used:**  
  - `scapy`  
  - `rich`  
  - `random`, `time`, `os`, `subprocess`, `argparse`



## 🛠️ Requirements

Install Python dependencies:

```bash
pip install -r requirements.txt
```

### 🧰 External Tools

Make sure these tools are installed:

- `mdk4` – for SSID spamming  
- `airmon-ng` – to enable monitor mode on your wireless interface  

Install them on Debian/Kali Linux:

```bash
sudo apt install mdk4 aircrack-ng
```



## 💻 Installation

Clone the repository:

```bash
git clone https://github.com/karthi-the-hacker/WIFIHacker.git
cd WIFIHacker
```

Install Python requirements:

```bash
pip install -r requirements.txt
```


## 🚀 Usage

Start the tool with sudo:

```bash
sudo python3 Wifihacker.py
```

Example output

```bash
                                                                        v1.0
██╗    ██╗██╗███████╗██╗██╗  ██╗ █████╗  ██████╗██╗  ██╗███████╗██████╗ 
██║    ██║██║██╔════╝██║██║  ██║██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗
██║ █╗ ██║██║█████╗  ██║███████║███████║██║     █████╔╝ █████╗  ██████╔╝
██║███╗██║██║██╔══╝  ██║██╔══██║██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗
╚███╔███╔╝██║██║     ██║██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║
 ╚══╝╚══╝ ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
                                                    Author: @karthithehacker
                                                Website: Karthithehacker.com     
```

From the menu, choose the attack you want:

```
1. 📡 Wifi Phishing
2. 📶 Wifi SPAM
3. 🚫 Wifi DoS (Coming Soon)
4. 📘 Learn Wifi Hacking (Coming Soon)
5. 🔐 View Captured Credentials
6. ❌ Exit
```

## 📝 Notes

- You can keep adding new folder templates in `templates/` with the structure:
  ```
  templates/
  ├── yourtemplatename/
      ├── index.html
      └── index.css
  ```
- The server will load the correct template based on the user input or default config.
- Make sure your Python server is serving files from the selected template directory and captures data from `/login`.




## 🧪 Example Fake Login Template (HTML)

### `index.html`

```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <title>Free Wi-Fi Login</title>
      <link rel="stylesheet" href="index.css">
    </head>
    <body>
      <form action="/login" method="post" class="login-box">
        <h2>Connect to Wi-Fi</h2>
        <input type="text" name="username" placeholder="Username or Email" required>
        <input type="password" name="password" placeholder="Password" required>
        <input type="submit" value="Login">
        <div class="note">Powered by Free Public Wi-Fi</div>
      </form>
    </body>
    </html>
```


## 📡 Captive Portal Endpoint

The `/login` endpoint receives credentials from fake Wi-Fi login pages (templates). When a user submits the login form, the server captures the following parameters:

### 📥 POST `/login`

| Parameter  | Type     | Description            |
|------------|----------|------------------------|
| `username` | `string` | **Required.** Username or email entered by the user |
| `password` | `string` | **Required.** Password entered by the user |



## 👨‍💻 Author

- Website: [karthithehacker.com](https://karthithehacker.com)
- GitHub: [@karthi-the-hacker](https://github.com/karthi-the-hacker)

---

## ⚠️ Disclaimer

This tool is made for **educational and ethical purposes only**.  
Unauthorized access to networks is illegal. The developer is not responsible for any misuse.


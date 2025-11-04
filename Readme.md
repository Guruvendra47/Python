# Windows Python Installation Guide (Step-by-Step)

This guide walks you through installing **Python 3** on **Windows**, verifying your setup, and creating a virtual environment.

> If you're on Windows 10/11, these steps work great. Prefer the official installer from python.org for full control and latest versions.

---

## ✅ Quick Summary
1. Download the latest Python 3 installer for Windows.
2. Run the installer and **check 'Add Python to PATH'**.
3. Verify `python` and `pip` in Command Prompt or PowerShell.
4. (Recommended) Upgrade `pip` and set up a virtual environment.
5. Fix common issues if something doesn’t work.

---

## 1) Download Python for Windows


- Open: **https://www.python.org/downloads/windows/**
- Click **Download Python 3.x** (Windows installer, 64‑bit).
- Save the `.exe` (e.g., `python-3.xx.x-amd64.exe`).

> Tip: Always use **python.org**. Avoid third-party download sites.

---

## 2) Run the Installer (Very Important: PATH)


1. Double‑click the downloaded **.exe**.
2. **Check** the box **“Add Python to PATH”** at the bottom.
3. Click **Install Now** (recommended).
4. Wait for setup to complete, then click **Close**.

> Want more control? Choose **Customize installation** and make sure **pip** and **tcl/tk and IDLE** are selected.

---

## 3) (Optional) Custom Installation Choices


- **Install for all users** (requires Admin) installs to `C:\Program Files\Python3x`.
- **pip**: Python’s package manager — **keep this checked**.
- **tcl/tk and IDLE**: Useful for simple GUIs and the IDLE editor.
- **Add Python to environment variables**: Check this if you missed the PATH checkbox.

---

## 4) Verify the Installation


Open **Command Prompt** or **PowerShell** and run:

```bat
python --version
pip --version
```

You should see something like:

```
Python 3.x.x
pip x.x from C:\Users\<you>\AppData\... (python 3.x)
```

If you have multiple Pythons installed, you can also try:

```bat
py --list
py -3 --version
```

---

## 5) Upgrade pip and Create a Virtual Environment


```bat
python -m pip install --upgrade pip
python -m venv .venv
```
**Activate the venv:**

- **PowerShell**
  ```bat
  .\.venv\Scripts\Activate.ps1
  ```
  If you see an execution policy error, run PowerShell **as Administrator** and then:
  ```bat
  Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
  ```

- **Command Prompt (cmd.exe)**
  ```bat
  .\.venv\Scripts\activate.bat
  ```

**Install packages inside the venv:**
```bat
pip install requests
```

**Deactivate when done:**
```bat
deactivate
```

---

## 6) Use Python from VS Code (Optional but Recommended)

1. Install **Visual Studio Code**.
2. Install the **Python** extension by Microsoft.
3. Open your project folder in VS Code.
4. Press `Ctrl+Shift+P` → **Python: Select Interpreter** → choose the **.venv** interpreter.
5. Create a file `main.py` and run it with the **Run** button.

---

## 7) Troubleshooting (Most Common)


- **`'python' is not recognized`**  
  Re‑run the installer and **check 'Add Python to PATH'**. Or manually add:
  - `C:\Users\<you>\AppData\Local\Programs\Python\Python3x\`
  - `C:\Users\<you>\AppData\Local\Programs\Python\Python3x\Scripts\`

- **Pip not found**  
  Run: `python -m ensurepip --upgrade` or re‑install with **pip** selected.

- **Multiple versions conflict**  
  Use the launcher: `py -3.12`, `py -3.11`, etc.

- **Permission issues**  
  Right‑click the installer → **Run as administrator** or install just for your user.

---

## 8) Uninstall or Repair

- Open **Settings → Apps → Installed apps** → search **Python** → **Uninstall**.
- Or re‑run the original installer to **Modify** or **Repair**.

---

## 9) Verify Everything Works

```bat
python - << "PY"
print('Hello from Python!')
PY
```

Expected output: `Hello from Python!`


---

**You're all set!** 🎉




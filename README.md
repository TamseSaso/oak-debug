# OAK Hand Pose Debug Example

This repository is an **example of debugging an OAK application using OAK Containers**.  
It is based on the official Luxonis **hand pose estimation example** found here:

https://github.com/luxonis/oak-examples/tree/main/neural-networks/pose-estimation/hand-pose

The goal of this repo is **not** to provide a polished demo, but to show how a debugging workflow with OAK Containers can look in practice.

---

## What This Example Is

- A **hand pose estimation** example
- Uses **OAK Containers**
- Demonstrates **remote debugging** using **Web-PDB** (web-based Python debugger)
- Intended purely for **debug / development experimentation**

---

## Getting Started

### 1. Clone the Repository

```bash
git clone <THIS_REPO_URL>
cd debug_app
```

---

### 2. Run the App on the OAK Device

Start the application using `oak-debug`:

```bash
./oak-debug <APP_PATH> <DEVICE_IP>
```

- `<APP_PATH>` – path to the application directory
- `<DEVICE_IP>` – IP address of your OAK device

The script will:
1. Start the app on the OAK device
2. Wait for the Web-PDB server to be ready (port 5555)
3. Automatically open your web browser to the debugger interface

---

### 3. Debug in Your Web Browser

Once the browser opens, you'll see the **Web-PDB interface** at:

```
http://<DEVICE_IP>:5555
```

The Web-PDB interface provides:
- **Current file** view with syntax highlighting
- **Globals** and **Locals** variable inspection
- Full PDB command support in the web console
- Command history (arrow keys UP/DOWN)

You can use standard PDB commands like:
- `n` (next line)
- `s` (step into)
- `c` (continue)
- `p <variable>` (print variable)
- `pp <variable>` (pretty print)
- `l` (list code)
- `w` (where/stack trace)
- `q` (quit)

**Note:** It's recommended to use only one browser session at a time. Multiple browser windows may display incorrect data.

---

## Customizing Breakpoints

The debugger is set to break at the start of the pipeline execution in `main.py`. To add additional breakpoints, add:

```python
import web_pdb; web_pdb.set_trace()
```

at any point in your code where you want to pause execution.

You can also use Python 3.7+ `breakpoint()` function by setting:
```bash
export PYTHONBREAKPOINT="web_pdb.set_trace"
```

---

## Known Issues / Quirks

- The debugger will pause execution when it hits `web_pdb.set_trace()`
- Make sure port 5555 is accessible from your machine to the OAK device
- If the browser doesn't open automatically, manually navigate to `http://<DEVICE_IP>:5555`

---

## Final Notes

This repository is intentionally minimal and experimental.  
If something feels rough around the edges — that's expected 🙂

Happy debugging 🚀

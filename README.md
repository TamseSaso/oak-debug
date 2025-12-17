# OAK Hand Pose Debug Example

This repository is an **example of debugging an OAK application using OAK Containers**.  
It is based on the official Luxonis **hand pose estimation example** found here:

https://github.com/luxonis/oak-examples/tree/main/neural-networks/pose-estimation/hand-pose

The goal of this repo is **not** to provide a polished demo, but to show how a debugging workflow with OAK Containers can look in practice.

---

## What This Example Is

- A **hand pose estimation** example
- Uses **OAK Containers**
- Demonstrates **remote debugging** using **VS Code**
- Intended purely for **debug / development experimentation**

⚠️ **Note:** This setup is a bit wonky by nature. You may need to retry the debugger multiple times before it successfully attaches.

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

After running the command, **wait for the app to fully start** on the device.

---

### 3. Attach the Debugger in VS Code

1. Open the repository in **VS Code**
2. Go to the **Run & Debug** panel
3. Select the launch configuration named:

```
Attach to OAK
```

4. Start debugging

If successful, the debugger will attach and you should eventually see an **error appear in the code**, indicating that debugging is active.

---

## Known Issues / Quirks

- Debugging is **not always reliable**
- You may need to:
  - Stop the debugger
  - Re-run it multiple times
- This is expected behavior for this example

---

## Stopping the Debugging Process

To stop the debugging process and run the example again, you must explicitly stop the running app on the device:

```bash
oakctl app stop 00000000-0000-0000-0000-000000000000
```

After stopping the app:

1. Run the app again using `./oak-debug`
2. Re-attach the debugger from VS Code if needed

---

## Final Notes

This repository is intentionally minimal and experimental.  
If something feels rough around the edges — that’s expected 🙂

Happy debugging 🚀

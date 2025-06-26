# SUMO Simulation 

This package contains all necessary files to run a traffic simulation using [SUMO (Simulation of Urban MObility)](https://www.eclipse.org/sumo/).

---

## Files Included: In the testing folder

- **test.sumocfg** – Main simulation configuration file  
- **test.net.nod.xml** – Network nodes definition  
- **test.net.edg.xml** – Network edges definition  
- **test.net.con.xml** – Connection definitions between edges  
- **test.net.tll.xml** – Traffic light logic file  
- **test.net.netccfg** – Network construction configuration  
- **test.netecfg** – Network editing configuration (optional)  
- **test.rou.xml** – Route/traffic flow definitions  

---

## ✅ Prerequisites

Make sure SUMO is installed. If not, install it using:

```bash
sudo apt update
sudo apt install sumo sumo-tools sumo-doc
```

Alternatively, use the [latest version from source](https://sumo.dlr.de/docs/Installing/index.html) for full features.

---

##  Run the Simulation

1. **Open a terminal and navigate to the folder containing these files:**

    ```bash
    cd /path/to/this/folder
    ```

2. **Run the simulation using SUMO-GUI:**

    ```bash
    sumo-gui -c test.sumocfg
    ```

    Or to run it without the GUI (command-line mode):

    ```bash
    sumo -c test.sumocfg
    ```

---

## 🛠 Notes

- If you edit network XML files (`*.nod.xml`, `*.edg.xml`, etc.), regenerate the network file using:

    ```bash
    netconvert -c test.net.netccfg
    ```

- To view or edit the network visually, use:

    ```bash
    netedit -c test.netecfg
    ```

---

## 📚 Additional Tips

### File Structure Overview

- **Configuration files** (`.sumocfg`, `.netccfg`): Control simulation parameters and network generation  
- **Network definition files** (`.nod.xml`, `.edg.xml`, `.con.xml`): Define the road network structure  
- **Traffic files** (`.rou.xml`, `.tll.xml`): Define vehicle routes and traffic light behavior  

### Common Commands

- **Check simulation validity:**  
    ```bash
    sumo --check-route-files -c test.sumocfg
    ```
- **Generate network from scratch:**  
    ```bash
    netconvert -c test.net.netccfg
    ```
- **Run headless simulation:**  
    ```bash
    sumo -c test.sumocfg --no-step-log
    ```

### Troubleshooting

- Ensure all referenced files exist in the same directory  
- Check XML syntax if encountering parsing errors  
- Verify network connectivity if vehicles aren't moving as expected  

---

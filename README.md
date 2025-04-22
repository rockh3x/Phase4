# Phase4
Shows federated model accuracy hovering around 20–26%
To run the federated learning scripts in Visual Studio Code, follow these steps:

### Step 1: Open Your Project in VS Code
1. Launch VS Code.
2. Open your project directory where you've saved the Python scripts.

### Step 2: Install Extensions
Make sure you have the following extensions installed for the best development experience:
- **Python**: Provides IntelliSense and code support.
- **Pylance** or **Jupyter**: For enhanced linting and code suggestions.

### Step 3: Set Up a Python Environment
1. **Create a Virtual Environment** (optional but recommended):
   Open a terminal in VS Code (using `Ctrl + `) and run the following commands:

   ```bash
   python -m venv venv
   ```

   Activate the virtual environment:
   - For Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - For macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

2. **Install Required Packages**:
   Install the necessary libraries (if not already installed):

   ```bash
   pip install flwr tensorflow matplotlib
   ```

### Step 4: Configure Python Interpreter
1. Press `Ctrl + Shift + P` to open the Command Palette.
2. Type `Python: Select Interpreter` and choose the interpreter from your virtual environment, e.g., `./venv/Scripts/python`.

### Step 5: Create and Fill in Your Python Files
Ensure you've created the necessary Python files (`client.py`, `model.py`, `run_phase4.py`, `server.py`, `utils.py`) and pasted the corresponding code into them.

### Step 6: Run the Server
1. Open a terminal in VS Code.
2. In the terminal, run the server script:

   ```bash
   python server.py
   ```

### Step 7: Run the Clients
Open additional terminal windows in VS Code for the clients:

1. For Client 0:
   ```bash
   python client.py 0
   ```
   
2. For Client 1:
   ```bash
   python client.py 1
   ```
   
3. For Client 2:
   ```bash
   python client.py 2
   ```
   
4. For Client 3:
   ```bash
   python client.py 3
   ```
   
5. For Client 4:
   ```bash
   python client.py 4
   ```

### Step 8: Monitor Output
Monitor the output in the server terminal to see the accuracy logs for each round. After all rounds are complete, the accuracy plot will be saved as `federated_accuracy.png`.

### Summary
- Open your project in VS Code.
- Set up a virtual environment and install required packages.
- Run the server and clients using separate terminals within VS Code.
- Monitor the output for accuracy logs.

If you need further assistance or run into any issues, feel free to ask! 

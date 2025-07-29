# PEDAL POWER

Pedal Power is an interactive, Python-based GUI program that encourages sustainability through biking. Biking is a sustainable and healthy mode of transportation. The application will enable users to input their rides and track how much they contribute to reducing their carbon footprint by using a bike as their mode of transportation. The app encourages users to continue biking through weekly challenges that suggest users ride a longer distance throughout the week and gives them virtual badges.

## 🚀 Features
### ♻️ Community Engagement & Eco-Tracking
- Encourage sustainable habits like recycling, biking, and energy-saving actions.
- Track individual eco-actions with real-time scoring.
### 🧠 Python Data Structures & Optimization
- Efficient tracking and scoring of eco-actions using optimized algorithms.
- Smart challenge generation to maximize community impact.
### 🧱 Object-Oriented Design
- Modular classes for:
  1. User: Profile, actions, and eco-points.
  2. Action: Type, impact score, and timestamp.
  3. Reward: Unlockable incentives based on performance.
  4. Challenge: Community goals and progress tracking.
### 🗃️ SQLite Database
- Persistent storage of user data, actions, and eco-points.
- Lightweight and portable for desktop environments.
### 📊 Data Visualization with Matplotlib
- Visual dashboards showing:
  1. Individual progress over time.
  2. Community-wide impact and leaderboard trends.
### 🖥️ PyQT Desktop App
- User-friendly interface for:
  1. Logging eco-actions.
  2. Viewing personal and community stats.

## Gantt Chart:
[Project_Sked_Group01](https://mymailmapuaedu-my.sharepoint.com/:x:/g/personal/cmaalonzo_mymail_mapua_edu_ph/EYb00BFohFNLunYTpnnjMlEBgQe3GJPqLP4N2inj1Oofnw)

---

## System Requirements and Platform Compatibility

Pedal Power is a cross-platform desktop application designed for seamless operation on both Windows and Ubuntu systems. The project requires Python 3.10 or later, utilizing PyQt5 for its graphical user interface and matplotlib for data visualization. All features are fully supported on Windows (including Windows 10 and 11) and Ubuntu 22.04 LTS and 24.04 LTS.

**Supported Operating Systems:**
- Windows 10 and 11
- Ubuntu 22.04 LTS
- Ubuntu 24.04 LTS

**Required Packages:**
- Python 3.10 or later
- PyQt5 (version 5.15.11)
- matplotlib

**Additional Notes:**
- For Ubuntu, ensure all required system dependencies for PyQt5 and matplotlib are installed.
- The application is best run in a virtual environment for dependency management.

---

# 🏁 Sprint 1: Initial Prototype

**Overview:**  
Sprint 1 establishes the foundational structure of the project, focusing on implementing a basic user login system.

**Key Components:**
- **Login UI (`Login_ui - 1.py`):** A simple command-line interface that prompts users for their username and password, and provides feedback on login success or failure.
- **Business Logic (`loginbl.py`):** Handles the authentication process by verifying user credentials against stored data.
- **Data Access Layer (`login_dal.py`):** Manages reading user credentials from a text file.
- **User Data (`users.txt`):** Contains sample usernames and passwords in a comma-separated format for authentication testing.

**Summary:**  
This sprint delivers a working prototype where users can log in using credentials stored in a file, demonstrating the integration of UI, business logic, and data access.

---

# 🚧 Sprint 2: GUI and Database Integration

**Overview:**  
Sprint 2 builds upon the foundational work completed in Sprint 1, which focused on creating the basic user interface (UI) and initial database setup. In Sprint 1, the login system was implemented using simple text-based input and a mock database (a text file), with most UI elements only printing messages to the terminal rather than being fully functional.

**Improvements and New Features:**
- **Graphical User Interfaces:** Fully developed graphical UIs for the Login, User, and Admin interfaces using PyQt5.
- **Database Integration:** Uses an SQLite database (`pedalpower.db`) for storing user and admin data, as well as biking records, replacing the simple text file approach from Sprint 1.
- **Admin Features:** Admin UI allows for listing users from the database, with buttons for adding, updating, deleting, and viewing users (currently connected to print statements, with full functionality planned for future sprints).
- **User Experience:** Visually improved UIs with fixed window sizes, icons, and better layout.
- **Assets:** Visual assets such as icons for logout and password visibility.
- **Requirements and Setup:** Clear setup instructions and a requirements file for easier environment configuration.

**Links:**  
[Requirements](https://github.com/Wixalot/CPE106L---Project-Pedal-Power/blob/90fe39f9ad6a933e846c96f0551b893add7f7638/Sprint%202/Requirements.txt)  
[Instructions](https://github.com/Wixalot/CPE106L---Project-Pedal-Power/blob/90fe39f9ad6a933e846c96f0551b893add7f7638/Sprint%202/INSTRUCTIONS.txt)  

---

# 🏆 Sprint 3: Complete Application

**Overview:**  
Sprint 3 delivers the complete and fully functional version of the Pedal Power project. This sprint finalizes all planned features, providing a polished, interactive, and data-driven experience for both users and administrators.

**Improvements and New Features:**
- **Centralized Main Program:** A new `main.py` file serves as the entry point, streamlining application startup and navigation.
- **User Data Visualization:** Users can now view their weekly biking progress through a dynamic chart (using matplotlib), and see their emissions saved.
- **User Input and Logging:** Users can input their biking distances, which are logged and reflected in their weekly statistics and emissions calculations.
- **Admin Enhancements:** The Admin UI now supports full CRUD (Create, Read, Update, Delete) operations for user management, with dedicated modules for adding, updating, and removing users. Admins can also view detailed biking records for each user.
- **View Window:** A new window allows admins to inspect individual user biking records.
- **Modular Code Structure:** Features are organized into modules (e.g., `AdminModules`, `UserModules`).
- **Improved UI/UX:** More interactive interfaces with better feedback, error handling, and visual polish.
- **Expanded Requirements:** Now requires both PyQt5 and matplotlib.

**Links:**  
[Requirements](https://github.com/Wixalot/CPE106L---Project-Pedal-Power/blob/90fe39f9ad6a933e846c96f0551b893add7f7638/Sprint%203/Requirements.txt)  
[Instructions](https://github.com/Wixalot/CPE106L---Project-Pedal-Power/blob/90fe39f9ad6a933e846c96f0551b893add7f7638/Sprint%203/INSTRUCTIONS.txt)  

---

# 👥 Team Members and Roles:
1. **ALONZO, Cyan** - Group Leader
2. **BELDIA, Luis** - Programmer
3. **ESTANDIAN, Geoffrey** -

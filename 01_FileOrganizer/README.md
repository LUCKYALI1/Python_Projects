# 🗂️ Python File Organizer

## ✨ Features
- 📂 **Organizes files** into predefined categories.
- 📝 **Logs every action** with a timestamp in `file_organizer_log.txt`.
- 🔒 **Exception handling** for missing folders and permission errors.
- ⚙ **OOP-based** for clean and reusable code.
- 🧪 **Test folder generator** included to create sample files.

## 📂 Folder Structure
```plaintext
FileOrganizer/
├── file_organizer.py        # Main file organizer script
├── create_test_files.py     # Script to generate sample test files
├── README.md                # Project documentation
└── test_files/              # Auto-created when you run create_test_files.py
```

## 📥 Installation & Setup
1. Clone the repository
```
git clone https://github.com/yourusername/FileOrganizer.git
cd FileOrganizer
```
2. Create test files
```
python create_test_files.py
```
This will create a folder named `test_files` with various file types.

3. Run the File Organizer
```
python file_organizer.py
```
Enter the folder path (e.g., `test_files`) when prompted.

## 📂 File Categories
| Category | Extensions |
| --- | --- |
| Images | `.jpg`, `.png`, `.gif`, `.bmp` |
| Videos | `.mp4`, `.avi`, `.mov`, `.mkv` |
| Documents | `.pdf`, `.docx`, `.txt`, `.xlsx` |
| Music | `.mp3`, `.wav`, `.ogg`, `.flac` |
| Archives | `.zip`, `.rar`, `.7z`, `.tar` |
| Executables | `.exe`, `.msi`, `.apk`, `.ipa` |
| Others | Any other file type |

## 🖥 Example Output
```
✅ Files organized successfully.
📄 Log file created: file_organizer_log.txt
```

Log file example:
```
[2025-08-10 14:25:36] Moved 'photo1.jpg' to 'images'
[2025-08-10 14:25:36] Moved 'video1.mp4' to 'videos'
```

## 🛠 Technologies Used
- Python 3
- `os` – File and directory handling
- `time` – Timestamps
- `shutil` – Moving files
- OOP – Class-based structure

## 🧪 Testing
To create a test folder with different file types:
```
python create_test_files.py
```
Then, run the organizer on that folder.

## 📜 License
This project is licensed under the MIT License – see the `LICENSE` file for details.

## 💡 Author
Lucky Ali

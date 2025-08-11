import os
import time as t
import shutil

class FileOrganizer:
    def __init__(self, path):
        self.folderPath = path
        self.logFile = os.path.join(self.folderPath, "file_organizer_log.txt")
        self.categories = {
            "images": ['.jpg', '.png', '.gif', '.bmp'],
            "videos": ['.mp4', '.avi', '.mov', '.mkv'],
            "documents": ['.pdf', '.docx', '.txt', '.xlsx'],
            "Music": ['.mp3', '.wav', '.ogg', '.flac'],
            "archives": ['.zip', '.rar', '.7z', '.tar'],
            "executables": ['.exe', '.msi', '.apk', '.ipa'],
            "others": []
        }

    def create_category_folders(self):
        for category in self.categories.keys():
            path = os.path.join(self.folderPath, category)
            os.makedirs(path, exist_ok=True)  # No error if folder exists

    def get_category(self, fileName):
        _, fileExtension = os.path.splitext(fileName)
        fileExtension = fileExtension.lower()
        for category, extensions in self.categories.items():
            if fileExtension in extensions:
                return category
        return "others"

    def log_action(self, message):
        """Log actions with timestamps."""
        with open(self.logFile, "a") as log:
            log.write(f"[{t.strftime('%Y-%m-%d %H:%M:%S')}] {message}\n")

    def organize_files(self):
        try:
            if not os.path.exists(self.folderPath):
                raise FileNotFoundError("Folder Does Not Exist!")

            self.create_category_folders()

            for fileName in os.listdir(self.folderPath):
                filePath = os.path.join(self.folderPath, fileName)

                # Skip directories and log file itself
                if os.path.isdir(filePath) or fileName == "file_organizer_log.txt":
                    continue

                category = self.get_category(fileName)
                destination = os.path.join(self.folderPath, category, fileName)

                shutil.move(filePath, destination)
                self.log_action(f"Moved '{fileName}' to '{category}'")

            print("✅ Files organized successfully.")

        except FileNotFoundError as e:
            print("❌ Error:", str(e))
        except PermissionError:
            print("❌ Permission denied to access files.")
        except Exception as e:
            print(f"❌ Unexpected error: {e}")


if __name__ == "__main__":
    folderPath = input("Enter The Folder Path To Organize: ").strip()
    try:
        organizer = FileOrganizer(folderPath)
        organizer.organize_files()
        print("Organizing Files...")
        t.sleep(2)
    except:
        print("Invalid Folder Path")

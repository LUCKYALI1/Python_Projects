import os

# Create a test folder
test_folder = "test_files"
os.makedirs(test_folder, exist_ok=True)

# Sample files with different extensions
sample_files = [
    "photo1.jpg",
    "photo2.png",
    "video1.mp4",
    "video2.mkv",
    "doc1.pdf",
    "doc2.txt",
    "music1.mp3",
    "music2.wav",
    "archive1.zip",
    "archive2.rar",
    "program.exe",
    "installer.msi",
    "unknown.xyz"
]

# Create empty files in the folder
for file_name in sample_files:
    file_path = os.path.join(test_folder, file_name)
    with open(file_path, "w") as f:
        f.write(f"This is a dummy file for {file_name}")

print(f"✅ Test folder '{test_folder}' created with {len(sample_files)} files.")

def progress_bar(progress, total):
    percent = 100 * (progress / float(total))
    bar = "█" * int(percent) + "-" * (100 - int(percent))
    print(f"\r|{bar}| {percent:.2f}%", end="\r")


def validate_file(file):
    """Validate the uploaded file"""
    file.file.seek(0, 2)
    file_size = file.file.tell()
    file.file.seek(0)  # Reset file pointer
    if file_size > MAX_FILE_SIZE:
        raise HTTPException(status_code=400, detail="File too large")

    file_extension = os.path.splitext(file.filename)[1].lower()
    if file_extension not in ALLOWED_EXTENSIONS:
        raise HTTPException(status_code=400, detail="Unsupported file type")

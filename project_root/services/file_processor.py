from fastapi import UploadFile, HTTPException
from services.embedding_service import process_text, store_in_chromadb
from services.question_generator import generate_questions
from utils.helpers import validate_file
import os
import asyncio


async def process_file(file: UploadFile):
    try:
        validate_file(file)
        content = await file.read()
        file_extension = os.path.splitext(file.filename)[1].lower()

        # Process the file based on its type
        # (Implementation details here)

        text = "Processed text from the file"  # Replace with actual processed text
        sentences = process_text(text)
        await store_in_chromadb(sentences, file.filename)

        questions = generate_questions(text)

        return {
            "filename": file.filename,
            "message": "File processed and stored successfully",
            "suggested_questions": questions,
        }
    except HTTPException as he:
        raise he
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing file: {str(e)}")


# Add any other necessary functions here

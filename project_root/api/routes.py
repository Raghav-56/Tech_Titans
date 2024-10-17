from fastapi import APIRouter, File, UploadFile, HTTPException
from services.file_processor import process_file
from services.query_service import query_documents
from api.models import Query

router = APIRouter()


@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    try:
        print(f"Receiving file: {file.filename}")
        text = await process_file(file)

        print("File processed. Beginning further processing...")
        sentences = process_text(text)
        await store_in_chromadb(sentences, file.filename)

        print("Generating questions...")
        questions = generate_questions(text)

        print(f"Processing complete.")
        return {
            "filename": file.filename,
            "message": "File processed and stored successfully",
            "suggested_questions": questions,
        }
    except HTTPException as he:
        raise he
    except Exception as e:
        print(f"Error occurred: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")


@router.post("/query")
async def query_endpoint(query: Query):
    try:
        print(f"Received query: {query.text}")
        results = await asyncio.to_thread(
            collection.query, query_texts=[query.text], n_results=5
        )

        formatted_results = [
            {"text": doc, "metadata": meta}
            for doc, meta in zip(results["documents"][0], results["metadatas"][0])
        ]

        context = "\n".join([result["text"] for result in formatted_results])
        ai_prompt = f"Based on the following context, answer the question: '{query.text}'\n\nContext:\n{context}"
        ai_response = ai_model.generate_content(ai_prompt)

        print(f"Query complete. Returning results and AI-generated response.")
        return {"results": formatted_results, "ai_response": ai_response.text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing query: {str(e)}")

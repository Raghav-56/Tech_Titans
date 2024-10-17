from database.chroma_db import collection
from services.question_generator import ai_model


async def query_documents(query: str):
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

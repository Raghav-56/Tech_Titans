import asyncio
from services.file_processor import process_file
from services.query_service import query_documents
from api.models import Query


def cli_interface():
    while True:
        print("\n1. Upload and process a file")
        print("2. Query the database")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            file_path = input("Enter the path to the file: ")
            if os.path.exists(file_path):
                with open(file_path, "rb") as file:
                    file_name = os.path.basename(file_path)
                    file_object = UploadFile(filename=file_name, file=file)
                    result = asyncio.run(upload_file(file_object))
                    print(result)
            else:
                print("File not found. Please check the path and try again.")

        elif choice == "2":
            query_text = input("Enter your query: ")
            result = asyncio.run(query_documents(Query(text=query_text)))
            print("\nQuery results:")
            for i, doc in enumerate(result["results"], 1):
                print(
                    f"{i}. {doc['text'][:100]}... (Source: {doc['metadata']['source']})"
                )
            print("\nAI-generated response:")
            print(result["ai_response"])

        elif choice == "3":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

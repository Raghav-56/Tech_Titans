# services/citation_service.py


class CitationService:
    def __init__(self, chroma_db):
        self.chroma_db = chroma_db

    def generate_citation(self, chunk_id):
        # Retrieve the chunk and its metadata from the database
        chunk_data = self.chroma_db.get_chunk(chunk_id)

        # Extract page number or section information
        page_number = chunk_data.get("page_number")
        section = chunk_data.get("section")

        # Generate a formatted citation
        if page_number:
            return f"(Page {page_number})"
        elif section:
            return f"(Section: {section})"
        else:
            return "(Source: Document)"

    def validate_response(self, response, chunk_ids):
        citations = []
        for chunk_id in chunk_ids:
            citation = self.generate_citation(chunk_id)
            citations.append(citation)

        # Combine the response with citations
        validated_response = f"{response}\n\nSources: {', '.join(citations)}"
        return validated_response

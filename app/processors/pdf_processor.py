import fitz

from app.processors.base_processor import BaseProcessor

class PDFProcessor(BaseProcessor):

    def extract_text(self,file_path: str) -> list[dict]:
        
        document = fitz.open(file_path)

        pages =[]

        for page_number in range(len(document)):

            page = document[page_number]
            text = page.get_text()
            pages.append({
                "page": page_number+1,
                "text": text,
            })

        document.close()

        return pages
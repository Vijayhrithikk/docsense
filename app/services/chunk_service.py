def generate_chunks(pages : list[dict]):

    paragraph_stream = []

    TARGET_SIZE = 1000
    MAX_CHUNK_SIZE = 1200

    for page in pages:

        page_number = page["page"]

        paragraphs = page["text"].split("\n\n")

        for paragraph in paragraphs:

            paragraph = paragraph.strip()

            if not paragraph:
                continue 

            if len(paragraph) > MAX_CHUNK_SIZE:

                for i in range(
                    0,
                    len(paragraph),
                    MAX_CHUNK_SIZE,
                ):

                    paragraph_stream.append({
                        "page": page_number,
                        "paragraph": paragraph[
                            i:i + MAX_CHUNK_SIZE
                        ]
                    })

            else:

                paragraph_stream.append({
                    "page": page_number,
                    "paragraph": paragraph
                })

    chunks = []

    current_chunk=[]
    current_size = 0
    start_page = None 
    end_page =None 



    for item in paragraph_stream:

        paragraph = item["paragraph"]
        page = item["page"]

        if start_page is None:
            start_page=page
        
        paragraph_size = len(paragraph)

        if(current_size+paragraph_size>TARGET_SIZE and current_chunk):
            chunks.append({
                "start_page": start_page,
                "end_page": end_page,
                "content": "\n\n".join(current_chunk)
            })

            current_chunk = []
            current_size=0
            start_page=page 

        current_chunk.append(paragraph)
        current_size += paragraph_size
        end_page = page

    if current_chunk:

        chunks.append({
            "start_page": start_page,
            "end_page": end_page,
            "content": "\n\n".join(current_chunk)
        })

    return chunks


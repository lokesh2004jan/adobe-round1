import os
import fitz  
import json
import re

def extract_outline(pdf_path):
    doc = fitz.open(pdf_path)
    title = os.path.splitext(os.path.basename(pdf_path))[0]
    outline = []

    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        blocks = page.get_text("dict")["blocks"]

        for block in blocks:
            for line in block.get("lines", []):
                spans = line.get("spans", [])
                if not spans:
                    continue

              
                text = " ".join([span.get("text", "") for span in spans]).strip()
                text = " ".join(text.split())  # Normalize spaces

               
                text = re.sub(r'\b([A-Z])\s+([A-Z])', r'\1\2', text)

              
                if not text or text.isdigit():
                    continue
                if "arxiv" in text.lower():
                    continue

               
                font_sizes = [span.get("size", 0) for span in spans]
                avg_font_size = sum(font_sizes) / len(font_sizes) if font_sizes else 0

                
                
                
                if avg_font_size > 15:
                    level = "H1"
                elif avg_font_size > 13:
                    level = "H2"
                elif avg_font_size > 11:
                    level = "H3"
                else:
                    continue

                outline.append({
                    "level": level,
                    "text": text,
                    "page": page_num + 1
                })

    return {
        "title": title,
        "outline": outline
    }

def main():
    input_folder = "input"
    output_folder = "output"

    os.makedirs(input_folder, exist_ok=True)
    os.makedirs(output_folder, exist_ok=True)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(".pdf"):
            pdf_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename.replace(".pdf", ".json"))

            outline_data = extract_outline(pdf_path)

            with open(output_path, "w", encoding="utf-8") as f:
                json.dump(outline_data, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    main()

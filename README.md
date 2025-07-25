# Adobe Round 1 – PDF Outline Extractor

This project extracts structured outlines (titles/headings) from PDFs using offline techniques. It is designed to run fully offline in a Docker container, as required by the Adobe GenAI Hackathon Round 1.

## 📌 Features
- Extracts headings (H1, H2, H3) using font-size heuristics via PyMuPDF.
- Outputs structured JSON files for each PDF.
- Runs offline in a lightweight Docker image.
- AMD64 compatible (as per Adobe requirements).

## 🧠 Methodology
- **PyMuPDF** is used to parse PDF text and font metadata.
- Heading levels are inferred using average font sizes.
- Outputs are saved as `<filename>.json` in the `/app/output` folder.

## 📂 Directory Structure


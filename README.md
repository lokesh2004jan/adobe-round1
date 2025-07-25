# Adobe Round 1 – PDF Outline Extractor

## Overview
A lightweight solution developed for Adobe GenAI Hackathon Round 1A that extracts structured outlines from academic/technical PDF documents using font-based heuristics.
The tool operates completely offline and supports containerized execution via Docker.

## Key Features
 **Offline Operation** - No internet/API dependencies  
 **Hierarchical Extraction** - Identifies H1/H2/H3 headings by font size  
 **Structured JSON Output** - Clean, machine-readable document outlines  
 **Docker-Compatible** - Reproducible builds on linux/amd64  
 **Optimized Performance** - Processes documents in <10 seconds  

## Technical Specifications
| Requirement          | Status      |
|----------------------|------------|
| Offline Operation    | ✔️ Compliant |
| No GPU Dependencies  | ✔️ Compliant |
| AMD64 Architecture   | ✔️ Compliant |
| Model Size <200MB    | ✔️ (No ML model) |
| JSON Output          | ✔️ Compliant |

## Project Structure

##  Project Structure
```text
.
├── app/
│   ├── input/          # PDF input directory (mount point)
│   ├── output/         # JSON results directory
│   └── main.py         # Core extraction engine
├── tests/              # (Optional) Test cases
├── Dockerfile          # Production-grade container setup
├── requirements.txt    # Pinned dependencies
└── README.md           # This documentation

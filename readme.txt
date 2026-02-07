# High-Efficiency Python Web Scraper (No-Dependencies)

A lightweight and optimized Python script designed to extract key web elements (links and headings) and export them into a structured CSV format.

## 🚀 Overview
Unlike many scrapers that rely on heavy external libraries, this tool is built using Python's native `html.parser`. This makes it faster, more secure, and extremely easy to deploy in any environment without worrying about package conflicts.

## ✨ Key Features
- **Zero Dependencies**: Uses only standard Python libraries (`urllib`, `html.parser`, `csv`).
- **Clean Data Extraction**: Specifically targets `<a>`, `<h1>`, `<h2>`, and `<h3>` tags.
- **Automated Export**: Automatically generates a `scraped_content.csv` file with all retrieved data.
- **Error Handling**: Built-in validation for URLs and robust handling of connection timeouts.
- **Optimized Performance**: Uses a class-based approach for efficient HTML parsing.

## 🛠️ Installation & Usage
1. **Clone the repository:**
   ```bash
2. Navigate to the directory:
## cd your-repo-name

3. Run the script:
## python product_scraper.py

4. Input the URL:
When prompted, enter the full website address (e.g., https://example.com).

Sample Output:
The script generates a CSV with the following columns:
   Type: (Link or Heading)
   Tag: (a, h1, h2, etc.)
   Text: The actual content inside the tag
   Href: The destination URL (for links)

💼 Why this approach?
As a software developer, I focus on building tools that are not just functional, but also optimized. This project demonstrates my ability to work with Python's core modules to create reliable automation solutions.

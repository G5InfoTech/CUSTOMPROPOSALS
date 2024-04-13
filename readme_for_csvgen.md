Certainly! Here's a README.md file explaining the provided code:

---

# CSV Generator

This Python script generates a CSV file based on the provided information using an AI assistant called Gemini.

## How it works

1. **Initialization**: The script initializes an instance of the `Generator_csv` class, which internally initializes an instance of the Gemini AI assistant from the `LLM.gemini` module.

2. **generate_csv method**: This method takes two arguments:
   - `data`: Information about a company provided as a string.
   - `output_path`: Path where the generated CSV file will be saved.

3. **Prompt Creation**: The method constructs a prompt for the Gemini AI assistant. The prompt includes a system message, instructions, and the provided information about the company. The prompt instructs the AI to generate CSV data based on the given information.

4. **AI Response**: The script sends the prompt to the Gemini AI assistant using the `get_response` method of the `llm` object (Gemini instance). It receives a response containing CSV data formatted as per the instructions.

5. **CSV Generation**: The response is split into lines, and each line is split into fields using a comma (`,`) delimiter. The script then writes these fields into a CSV file specified by `output_path` using the `csv` module.

6. **Completion Message**: Once the CSV file is successfully generated, the script prints a confirmation message.

## Example Usage

```python
from LLM.gemini import Gemini
from generator_csv import Generator_csv

# Instantiate Generator_csv class
csv_generator = Generator_csv()

# Information about the company
company_info = "Company Name: XYZ Corp, Location: New York, Industry: Technology"

# Specify output path for the CSV file
output_file_path = "output.csv"

# Generate CSV file
csv_generator.generate_csv(company_info, output_file_path)
```

This script can be used to quickly generate CSV files containing contact information based on provided company details.

---

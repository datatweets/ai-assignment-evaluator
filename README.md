# Automated Assignment Scoring System

This system automatically evaluates student assignments using AI (Claude API) and generates structured feedback in JSON format.

## Features

- Reads student assignments from Word documents (.docx)
- Automatically detects incomplete or template submissions
- Evaluates based on 5 criteria (25 points total):
  - Prompt Clarity (0-5)
  - Real-World Relevance (0-5)
  - Reflection Quality (0-5)
  - Responsible Use (0-5)
  - Writing Clarity (0-5)
- Generates structured JSON feedback for each student
- Provides detailed summary feedback and improvement suggestions
- View results in formatted tables with statistics
- Export results to CSV for easy analysis

## Project Structure

```
assignment_workflow/
├── automate_scoring.py          # Main scoring script
├── view_results.py              # Results viewer (table/CSV export)
├── evaluation_prompt.json       # Evaluation criteria and prompts
├── config.json                  # Configuration file
├── requirements.txt             # Python dependencies
├── student-assignments/         # Input: Student assignment files (.docx)
├── evaluation-results/          # Output: JSON evaluation results + CSV
└── assignment-template/         # Assignment template and scoring guide
```

## Setup Instructions

### 1. Install Dependencies

Activate your virtual environment and install required packages:

```bash
source .venv/bin/activate  # On macOS/Linux
# or
.venv\Scripts\activate     # On Windows

pip install -r requirements.txt
```

### 2. Configure API Key

You have two options:

**Option A: Using config.json (Recommended for testing)**

Edit [config.json](config.json) and add your Anthropic API key:

```json
{
  "anthropic_api_key": "sk-ant-your-actual-api-key",
  "model": "claude-3-5-sonnet-20241022",
  "max_tokens": 4096
}
```

**Option B: Using Environment Variables (Recommended for production)**

Create a `.env` file (copy from `.env.example`):

```bash
cp .env.example .env
```

Edit `.env` and add your API key:

```
ANTHROPIC_API_KEY=sk-ant-your-actual-api-key
```

### 3. Get Your Anthropic API Key

1. Go to [https://console.anthropic.com/](https://console.anthropic.com/)
2. Sign in or create an account
3. Navigate to API Keys section
4. Generate a new API key
5. Copy and paste it into your config file

## Usage

### Basic Usage

Place student assignment files (.docx) in the `student-assignments/` folder, then run:

```bash
python automate_scoring.py
```

### Output

The script will:
1. Process all `.docx` files in `student-assignments/`
2. Generate individual evaluation files in `evaluation-results/`
3. Create a summary file: `evaluation-results/all_evaluations_summary.json`

### Viewing Results

After running the scoring script, use the results viewer to see evaluations in a formatted table:

```bash
python view_results.py           # Summary table + statistics (default)
python view_results.py detailed  # Detailed view of each student
python view_results.py stats     # Statistics only
python view_results.py csv       # Export to CSV file
python view_results.py all       # Show everything + export CSV
```

**Example Output:**

```
========================================================================================================================
ASSIGNMENT EVALUATION SUMMARY
========================================================================================================================

Student              Total      Prompt     Real-World   Reflection   Responsible   Writing
------------------------------------------------------------------------------------------------------------------------
stu_no_2949          15 / 25    4/5        4/5          2/5          3/5           2/5
stu_no_3949          10 / 25    2/5        2/5          2/5          2/5           2/5

============================================================
STATISTICS
============================================================

Total Assignments: 2
Average Score: 12.5 / 25
Highest Score: 15 / 25
Lowest Score: 10 / 25

Score Distribution:
  0-10  (Developing):       1 student(s)
  11-17 (Progressing Well): 1 student(s)
  18-22 (Strong):           0 student(s)
  23-25 (Excellent):        0 student(s)
```

### Example Output Structure

Each evaluation JSON file contains:

```json
{
  "total_score": "18 / 25",
  "category_breakdown": {
    "prompt_clarity": "4/5",
    "real_world_relevance": "3/5",
    "reflection_quality": "4/5",
    "responsible_use": "4/5",
    "writing_clarity": "3/5"
  },
  "summary_feedback": "The student demonstrated good understanding...",
  "improvement_suggestion": "Add more specific context about your role...",
  "metadata": {
    "student_file": "stu_no_2949.docx",
    "evaluation_date": "2025-11-05T10:30:00",
    "model_used": "claude-3-5-sonnet-20241022"
  },
  "raw_response": "**Total Score:** 18 / 25..."
}
```

## Evaluation Criteria

The system evaluates assignments based on criteria defined in [evaluation_prompt.json](evaluation_prompt.json):

### 1. Prompt Clarity (0-5)
- Evaluates strong and improved prompts in Section 2
- Checks understanding of Role + Context + Instruction + Format
- Reviews explanation of why weak prompts are weak

### 2. Real-World Relevance (0-5)
- Assesses connection to actual work tasks
- Evaluates practical examples and applications

### 3. Reflection Quality (0-5)
- Reviews depth of reflection on AI responses
- Checks learning outcomes and insights

### 4. Responsible Use (0-5)
- Evaluates awareness of privacy and ethical considerations
- Checks understanding of accuracy verification

### 5. Writing Clarity (0-5)
- Assesses overall clarity and organization
- Evaluates completeness of responses

## Customization

### Modify Evaluation Criteria

Edit [evaluation_prompt.json](evaluation_prompt.json) to:
- Change scoring rubrics
- Add new criteria
- Modify point allocations
- Update assignment structure

### Change AI Model

Edit [config.json](config.json):

```json
{
  "model": "claude-3-opus-20240229",  // For more detailed analysis
  "max_tokens": 8192                  // For longer responses
}
```

## Troubleshooting

### Issue: "No .docx files found"
- Ensure your student files are in the `student-assignments/` folder
- Check that files have `.docx` extension (not `.doc`)

### Issue: "Authentication error"
- Verify your API key is correct
- Check that the API key has proper permissions
- Ensure you have credits in your Anthropic account

### Issue: "Module not found"
- Activate your virtual environment: `source .venv/bin/activate`
- Install dependencies: `pip install -r requirements.txt`

### Issue: "Rate limit exceeded"
- The script processes files sequentially to avoid rate limits
- If you have many files, consider adding delays between requests

## Cost Estimation

Using Claude 3.5 Sonnet:
- Input: ~$3 per million tokens
- Output: ~$15 per million tokens
- Approximate cost per evaluation: $0.10 - $0.30 (depending on assignment length)

## Advanced Usage

### Process Specific Files

Modify the script to process specific files:

```python
scorer = AssignmentScorer()
evaluation = scorer.score_assignment("student-assignments/specific_student.docx")
print(json.dumps(evaluation, indent=2))
```

### Batch Processing with Custom Output

```python
scorer = AssignmentScorer()
results = scorer.score_all_assignments(
    input_dir="custom-input-folder",
    output_dir="custom-output-folder"
)
```

## Support

For issues or questions:
1. Check the troubleshooting section above
2. Review the [evaluation_prompt.json](evaluation_prompt.json) configuration
3. Verify your API key and credits at [console.anthropic.com](https://console.anthropic.com/)

## License

This is an educational tool for automated assignment grading.

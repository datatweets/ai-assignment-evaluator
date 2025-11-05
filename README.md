# AI Assignment Evaluator

Automated assignment evaluation system using Claude API to provide structured, constructive feedback on student submissions.

## Overview

This system evaluates Generative AI training assignments by analyzing student responses across five key criteria, generating detailed JSON feedback, and providing actionable improvement suggestions. The evaluation is rigorous yet supportive, helping students learn and grow.

## Features

- **Automated Evaluation**: Processes Word documents (.docx) and generates structured JSON feedback
- **Smart Detection**: Automatically identifies incomplete or template-only submissions
- **Multi-Criteria Scoring**: Evaluates across 5 dimensions (25 points total)
  - Prompt Clarity (0-5)
  - Real-World Relevance (0-5)
  - Reflection Quality (0-5)
  - Responsible Use (0-5)
  - Writing Clarity (0-5)
- **Constructive Feedback**: Generates kind, encouraging feedback with specific improvement suggestions
- **Results Visualization**: View results in formatted tables with statistics
- **Data Export**: Export evaluations to CSV for analysis in Excel or Google Sheets
- **Customizable**: Modify evaluation criteria and scoring rubrics via JSON configuration

## Project Structure

```
ai-assignment-evaluator/
├── automate_scoring.py          # Main scoring script
├── view_results.py              # Results viewer (tables/CSV export)
├── evaluation_prompt.json       # Evaluation criteria and rubrics
├── config.json                  # Configuration (API key, model settings)
├── requirements.txt             # Python dependencies
├── FORMAT_GUIDE.md              # Output format documentation
├── student-assignments/         # Input: Student .docx files
├── evaluation-results/          # Output: JSON evaluations + CSV
└── assignment-template/         # Assignment templates and scoring guide
```

## Quick Start

1. **Install dependencies:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # macOS/Linux
   pip install -r requirements.txt
   ```

2. **Configure API key:**
   ```bash
   cp .env.example .env
   # Edit .env and add your Anthropic API key
   ```

3. **Run evaluation:**
   ```bash
   python automate_scoring.py
   ```

4. **View results:**
   ```bash
   python view_results.py
   ```

## Setup Instructions

### 1. Install Dependencies

Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate  # On macOS/Linux
# or
.venv\Scripts\activate     # On Windows

pip install -r requirements.txt
```

### 2. Configure API Key

**Important:** The `config.json` file is excluded from version control for security. You need to create it locally.

Create `config.json` with your Anthropic API key:

```json
{
  "anthropic_api_key": "sk-ant-your-actual-api-key",
  "model": "claude-3-haiku-20240307",
  "max_tokens": 4096,
  "input_directory": "student-assignments",
  "output_directory": "evaluation-results"
}
```

**Alternative: Use environment variables**

Create a `.env` file:

```bash
cp .env.example .env
```

Add your API key to `.env`:

```
ANTHROPIC_API_KEY=sk-ant-your-actual-api-key
```

### 3. Get Your Anthropic API Key

1. Visit [https://console.anthropic.com/](https://console.anthropic.com/)
2. Sign in or create an account
3. Navigate to API Keys section
4. Generate a new API key
5. Copy the key to your `config.json` or `.env` file

## Usage

### Running Evaluations

Place student assignment files (.docx) in the `student-assignments/` folder:

```bash
python automate_scoring.py
```

The script will:
1. Process all `.docx` files in `student-assignments/`
2. Detect and flag incomplete/template submissions
3. Generate individual evaluation JSON files in `evaluation-results/`
4. Create a summary file: `evaluation-results/all_evaluations_summary.json`

### Viewing Results

Display results in formatted tables:

```bash
python view_results.py           # Summary table + statistics
python view_results.py detailed  # Full feedback for each student
python view_results.py stats     # Statistics only
python view_results.py csv       # Export to CSV
python view_results.py all       # All views + CSV export
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
stu_no_4949          20 / 25    4/5        4/5          4/5          4/5           4/5

============================================================
STATISTICS
============================================================

Total Assignments: 3
Average Score: 15.0 / 25
Highest Score: 20 / 25
Lowest Score: 10 / 25

Score Distribution:
  0-10  (Developing):       1 student(s)
  11-17 (Progressing Well): 1 student(s)
  18-22 (Strong):           1 student(s)
  23-25 (Excellent):        0 student(s)
```

### Output Format

Each evaluation generates a JSON file with:

```json
{
  "total_score": "15 / 25",
  "category_breakdown": {
    "prompt_clarity": "4/5",
    "real_world_relevance": "4/5",
    "reflection_quality": "2/5",
    "responsible_use": "3/5",
    "writing_clarity": "2/5"
  },
  "summary_feedback": "Great work on this assignment! You demonstrate...",
  "improvement_suggestion": "For your next assignment, aim to produce...",
  "metadata": {
    "student_file": "stu_no_2949.docx",
    "evaluation_date": "2025-11-05T11:18:13.642013"
  },
  "raw_response": "**Total Score:** 15 / 25\n..."
}
```

See [FORMAT_GUIDE.md](FORMAT_GUIDE.md) for detailed format specifications.

## Evaluation Criteria

The system uses five criteria defined in [evaluation_prompt.json](evaluation_prompt.json):

### 1. Prompt Clarity (0-5)
Evaluates the quality of prompts created in Section 2:
- Strong prompt (Step 2) using Role + Context + Instruction + Format
- Improved prompt (Step 5) based on reflection
- Understanding of why weak prompts are ineffective

### 2. Real-World Relevance (0-5)
Assesses practical application:
- Connection to actual job responsibilities
- Specific, realistic examples from daily work
- Thoughtful adaptation to their role

### 3. Reflection Quality (0-5)
Measures depth of learning:
- Critical analysis of AI responses
- Clear reasoning about what worked/didn't work
- Specific plans for applying insights

### 4. Responsible Use (0-5)
Evaluates ethical awareness:
- Understanding of data privacy and security
- Accuracy verification practices
- Ethical considerations in AI use

### 5. Writing Clarity (0-5)
Assesses communication:
- Overall clarity and organization
- Complete, well-structured responses
- Effective idea communication

## Customization

### Modify Evaluation Criteria

Edit [evaluation_prompt.json](evaluation_prompt.json) to:
- Adjust scoring rubrics
- Add or remove criteria
- Change point allocations
- Update assignment structure
- Modify feedback tone and style

### Change AI Model

Edit `config.json` to use a different model:

```json
{
  "model": "claude-3-haiku-20240307",    # Fast, cost-effective
  "model": "claude-3-5-sonnet-20241022", # More detailed (if available)
  "max_tokens": 4096
}
```

**Note:** Model availability depends on your API access tier.

### Adjust Incomplete Submission Detection

Modify `check_if_submission_is_complete()` in `automate_scoring.py` to change detection logic for incomplete or template submissions.

## Troubleshooting

### "No .docx files found"
- Verify files are in `student-assignments/` folder
- Ensure files have `.docx` extension (not `.doc`)
- Check file permissions

### "Authentication error"
- Verify API key is correct in `config.json` or `.env`
- Check API key has proper permissions
- Ensure you have credits in your Anthropic account
- Visit [console.anthropic.com](https://console.anthropic.com/) to check status

### "Module not found"
- Activate virtual environment: `source .venv/bin/activate`
- Install dependencies: `pip install -r requirements.txt`
- Verify Python version (3.8 or higher recommended)

### "Model not found" (404 error)
- Check your API access tier
- Update model name in `config.json` to an available model
- Default fallback: `claude-3-haiku-20240307`

### "Rate limit exceeded"
- Script processes files sequentially to minimize rate limits
- For large batches, add delays between requests
- Consider upgrading API tier for higher limits

### Missing total score in results
- Parser automatically calculates from category breakdown if missing
- Check [FORMAT_GUIDE.md](FORMAT_GUIDE.md) for format specifications
- Review `raw_response` field in JSON for actual AI output

## Cost Estimation

Using Claude 3 Haiku (default):
- Input: ~$0.25 per million tokens
- Output: ~$1.25 per million tokens
- Approximate cost per evaluation: $0.01 - $0.05

Using Claude 3.5 Sonnet (if available):
- Input: ~$3 per million tokens
- Output: ~$15 per million tokens
- Approximate cost per evaluation: $0.10 - $0.30

Actual costs depend on assignment length and complexity.

## Advanced Usage

### Process Specific Files

```python
from automate_scoring import AssignmentScorer

scorer = AssignmentScorer()
evaluation = scorer.score_assignment("student-assignments/student_001.docx")
print(json.dumps(evaluation, indent=2))
```

### Custom Input/Output Directories

```python
scorer = AssignmentScorer()
results = scorer.score_all_assignments(
    input_dir="custom-submissions",
    output_dir="custom-results"
)
```

### Programmatic Access to Results

```python
import json
from pathlib import Path

# Load all evaluations
results_dir = Path("evaluation-results")
evaluations = []

for json_file in results_dir.glob("*_evaluation.json"):
    with open(json_file) as f:
        evaluations.append(json.load(f))

# Calculate average score
scores = [int(e["total_score"].split("/")[0]) for e in evaluations]
average = sum(scores) / len(scores)
print(f"Class average: {average:.1f} / 25")
```

## Security & Privacy

- **API Keys**: Never commit `config.json` or `.env` files
- **Student Data**: Student assignments and evaluations are excluded from git
- **Data Protection**: All processing happens locally; only prompts are sent to Claude API
- **Audit Trail**: All evaluations include metadata with timestamps

## File Management

Protected files (in `.gitignore`):
- `config.json` - Contains API key
- `evaluation-results/` - Student evaluation data
- `student-assignments/*.docx` - Student submissions
- `.venv/` - Python virtual environment
- `.env` - Environment variables

## Contributing

To contribute:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test with sample assignments
5. Submit a pull request

## License

This is an educational tool for automated assignment grading. See repository for license details.

## Documentation

- [FORMAT_GUIDE.md](FORMAT_GUIDE.md) - Output format specifications
- [evaluation_prompt.json](evaluation_prompt.json) - Evaluation criteria
- [requirements.txt](requirements.txt) - Python dependencies

## Support

For issues or questions:
1. Check the troubleshooting section above
2. Review [FORMAT_GUIDE.md](FORMAT_GUIDE.md) for format issues
3. Verify configuration in `evaluation_prompt.json`
4. Check API status at [console.anthropic.com](https://console.anthropic.com/)

---

**Repository**: https://github.com/datatweets/ai-assignment-evaluator

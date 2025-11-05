#!/usr/bin/env python3
"""
View Assignment Evaluation Results in Table Format
This script displays evaluation results from JSON files in a formatted table.
"""

import json
import os
from pathlib import Path
from typing import List, Dict, Any


def load_evaluation_results(results_dir: str = "evaluation-results") -> List[Dict[str, Any]]:
    """Load all evaluation JSON files from the results directory."""
    results_path = Path(results_dir)

    if not results_path.exists():
        print(f"Error: Directory '{results_dir}' not found.")
        return []

    # Find all individual evaluation files (not the summary)
    json_files = [f for f in results_path.glob("*_evaluation.json")]

    if not json_files:
        print(f"No evaluation files found in '{results_dir}'")
        return []

    evaluations = []
    for json_file in sorted(json_files):
        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                data['file_name'] = json_file.stem.replace('_evaluation', '')
                evaluations.append(data)
        except Exception as e:
            print(f"Error loading {json_file}: {e}")

    return evaluations


def display_summary_table(evaluations: List[Dict[str, Any]]):
    """Display a summary table of all evaluations."""
    if not evaluations:
        print("No evaluations to display.")
        return

    print("\n" + "=" * 120)
    print("ASSIGNMENT EVALUATION SUMMARY")
    print("=" * 120)
    print()

    # Header
    header = f"{'Student':<20} {'Total':<10} {'Prompt':<10} {'Real-World':<12} {'Reflection':<12} {'Responsible':<13} {'Writing':<10}"
    print(header)
    print("-" * 120)

    # Rows
    for eval_data in evaluations:
        student = eval_data.get('file_name', 'Unknown')
        total = eval_data.get('total_score', 'N/A')
        breakdown = eval_data.get('category_breakdown', {})

        prompt_clarity = breakdown.get('prompt_clarity', 'N/A')
        real_world = breakdown.get('real_world_relevance', 'N/A')
        reflection = breakdown.get('reflection_quality', 'N/A')
        responsible = breakdown.get('responsible_use', 'N/A')
        writing = breakdown.get('writing_clarity', 'N/A')

        row = f"{student:<20} {total:<10} {prompt_clarity:<10} {real_world:<12} {reflection:<12} {responsible:<13} {writing:<10}"
        print(row)

    print("=" * 120)
    print()


def display_detailed_view(evaluations: List[Dict[str, Any]]):
    """Display detailed view of each evaluation."""
    for i, eval_data in enumerate(evaluations, 1):
        student = eval_data.get('file_name', 'Unknown')
        metadata = eval_data.get('metadata', {})

        print("\n" + "=" * 100)
        print(f"STUDENT {i}: {metadata.get('student_file', student)}")
        print("=" * 100)

        # Score
        print(f"\nTotal Score: {eval_data.get('total_score', 'N/A')}")

        # Category Breakdown
        print("\nCategory Breakdown:")
        breakdown = eval_data.get('category_breakdown', {})
        for category, score in breakdown.items():
            formatted_category = category.replace('_', ' ').title()
            print(f"  - {formatted_category:<25}: {score}")

        # Summary Feedback
        print("\nSummary Feedback:")
        feedback = eval_data.get('summary_feedback', 'No feedback available')
        # Word wrap the feedback
        words = feedback.split()
        line = ""
        for word in words:
            if len(line) + len(word) + 1 <= 95:
                line += word + " "
            else:
                print(f"  {line.strip()}")
                line = word + " "
        if line:
            print(f"  {line.strip()}")

        # Improvement Suggestion
        print("\nImprovement Suggestion:")
        suggestion = eval_data.get('improvement_suggestion', 'No suggestion available')
        # Word wrap the suggestion
        words = suggestion.split()
        line = ""
        for word in words:
            if len(line) + len(word) + 1 <= 95:
                line += word + " "
            else:
                print(f"  {line.strip()}")
                line = word + " "
        if line:
            print(f"  {line.strip()}")

        # Metadata
        print(f"\nEvaluation Date: {metadata.get('evaluation_date', 'Unknown')}")
        print()


def display_statistics(evaluations: List[Dict[str, Any]]):
    """Display statistics about the evaluations."""
    if not evaluations:
        return

    print("\n" + "=" * 60)
    print("STATISTICS")
    print("=" * 60)
    print()

    # Extract total scores
    scores = []
    for eval_data in evaluations:
        total_str = eval_data.get('total_score', '0 / 25')
        try:
            score_num = int(total_str.split('/')[0].strip())
            scores.append(score_num)
        except:
            continue

    if scores:
        avg_score = sum(scores) / len(scores)
        max_score = max(scores)
        min_score = min(scores)

        print(f"Total Assignments: {len(evaluations)}")
        print(f"Average Score: {avg_score:.1f} / 25")
        print(f"Highest Score: {max_score} / 25")
        print(f"Lowest Score: {min_score} / 25")
        print()

        # Score distribution
        print("Score Distribution:")
        developing = sum(1 for s in scores if s <= 10)
        progressing = sum(1 for s in scores if 11 <= s <= 17)
        strong = sum(1 for s in scores if 18 <= s <= 22)
        excellent = sum(1 for s in scores if s >= 23)

        print(f"  0-10  (Developing):       {developing} student(s)")
        print(f"  11-17 (Progressing Well): {progressing} student(s)")
        print(f"  18-22 (Strong):           {strong} student(s)")
        print(f"  23-25 (Excellent):        {excellent} student(s)")
        print()


def export_to_csv(evaluations: List[Dict[str, Any]], output_file: str = "evaluation-results/summary.csv"):
    """Export results to CSV file."""
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            # Header
            f.write("Student,Total Score,Prompt Clarity,Real-World Relevance,Reflection Quality,Responsible Use,Writing Clarity,Evaluation Date\n")

            # Rows
            for eval_data in evaluations:
                student = eval_data.get('metadata', {}).get('student_file', eval_data.get('file_name', 'Unknown'))
                total = eval_data.get('total_score', 'N/A')
                breakdown = eval_data.get('category_breakdown', {})
                date = eval_data.get('metadata', {}).get('evaluation_date', 'Unknown')

                row = f"{student},{total},{breakdown.get('prompt_clarity', 'N/A')},{breakdown.get('real_world_relevance', 'N/A')},{breakdown.get('reflection_quality', 'N/A')},{breakdown.get('responsible_use', 'N/A')},{breakdown.get('writing_clarity', 'N/A')},{date}\n"
                f.write(row)

        print(f"✓ Results exported to: {output_file}")
    except Exception as e:
        print(f"Error exporting to CSV: {e}")


def main():
    """Main function to display evaluation results."""
    import sys

    print("\n" + "🎓" * 30)
    print("ASSIGNMENT EVALUATION RESULTS VIEWER")
    print("🎓" * 30)

    # Load evaluations
    evaluations = load_evaluation_results()

    if not evaluations:
        print("\nNo evaluation results found. Run automate_scoring.py first.")
        return

    # Check for command line arguments
    view_mode = "summary"
    if len(sys.argv) > 1:
        view_mode = sys.argv[1].lower()

    if view_mode == "detailed" or view_mode == "-d":
        display_detailed_view(evaluations)
    elif view_mode == "stats" or view_mode == "-s":
        display_statistics(evaluations)
    elif view_mode == "csv" or view_mode == "-c":
        display_summary_table(evaluations)
        export_to_csv(evaluations)
    elif view_mode == "all" or view_mode == "-a":
        display_summary_table(evaluations)
        display_statistics(evaluations)
        display_detailed_view(evaluations)
        export_to_csv(evaluations)
    else:
        # Default: summary table + statistics
        display_summary_table(evaluations)
        display_statistics(evaluations)



if __name__ == "__main__":
    main()

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
import catalog_runner
import argparse
import sys

def generate_statistical_report(results, agent_type, filename="statistical_results.pdf"):
    doc = SimpleDocTemplate(filename, pagesize=letter)
    styles = getSampleStyleSheet()
    elements = []
    
    # Title
    elements.append(Paragraph(f"Catalog Scheduling Statistical Results - {agent_type.capitalize()} Agent", styles['Title']))
    elements.append(Paragraph("\n", styles['Normal']))
    
    # Create table data
    data = [
        ['Max Credits', 'Avg Semesters', 'Min Semesters', 'Max Semesters', 'Total Students']
    ]
    
    for credits, stats in results.items():
        data.append([
            credits.split('_')[-1],
            f"{stats['average_semesters']:.2f}",
            str(stats['min_semesters']),
            str(stats['max_semesters']),
            str(stats['total_runs'])
        ])
    
    # Create and style the table
    table = Table(data)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 14),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 12),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))
    
    elements.append(table)
    
    # Add analysis based on agent type
    elements.append(Paragraph("\nAnalysis:", styles['Heading2']))
    
    if agent_type == "random":
        analysis_text = """
        The random agent selects courses randomly from available options each semester.
        Since I am doing policy search, the agent takes a catalog and measures how good it is by simulating students taking classes.
        The random agent's performance was tested with different maximum credit loads per semester. 
        This helps us understand how the credit limit affects graduation time. Key observations:
        
        1. Higher credit limits generally lead to faster graduation times
        2. The random agent shows significant variation in performance
        3. The minimum number of semesters represents the best-case scenario
        """
    else:  # requirements agent
        analysis_text = """
        The requirements agent makes informed decisions based on graduation requirements.
        It prioritizes courses that fulfill unfulfilled requirements, leading to more efficient degree completion.
        Testing with different credit loads reveals:
        
        1. More strategic course selection compared to random agent
        2. Better consistency in graduation times
        3. More efficient fulfillment of degree requirements
        """
    
    elements.append(Paragraph(analysis_text, styles['Normal']))
    
    doc.build(elements)

def main(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument('--episodes', type=int, default=100)
    parser.add_argument('--output', type=str, default='statistical_results.pdf')
    parser.add_argument('--agent', type=str, choices=['random', 'requirements'], default='random',
                      help='Type of agent to analyze')
    args = parser.parse_args(argv[1:])
    
    # Run simulations
    runner_args = type('Args', (), {
        'render_mode': None,
        'max_semesters': 50,
        'episode_count': args.episodes,
        'catalog_file': 'fullcatalog.json',
        'agent': args.agent
    })()
    
    results = catalog_runner.do_catalog_statistical_measure(runner_args)
    
    # Generate PDF report
    generate_statistical_report(results, args.agent, args.output)

if __name__ == "__main__":
    main(sys.argv) 
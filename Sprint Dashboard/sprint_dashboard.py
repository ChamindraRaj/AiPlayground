"""
Sprint Metrics Dashboard Generator
Reads Excel data and generates an HTML dashboard matching the design specifications.
"""

import pandas as pd
from typing import Dict, List
import unittest
from io import StringIO


class DashboardGenerator:
    """Generates HTML dashboard from Excel data."""
    
    # Design constants matching the image
    COLORS = {
        'primary_blue': '#003d5c',
        'secondary_blue': '#4a6c7d',
        'orange': '#ff6633',
        'light_gray': '#e8e8e8',
        'white': '#ffffff'
    }
    
    FONTS = {
        'primary': 'Arial, sans-serif',
        'weight_bold': '700',
        'weight_normal': '400'
    }
    
    def __init__(self, excel_path: str):
        """Initialize with path to Excel file."""
        self.excel_path = excel_path
        self.data = self._load_data()
    
    def _load_data(self) -> Dict:
        """Load and parse Excel data into structured format."""
        df = pd.read_excel(self.excel_path)
        
        # Parse the data structure
        data = {
            'sprint': df.iloc[0]['Value'],
            'increment': df.iloc[1]['Value'],
            'categories': []
        }
        
        # Parse categories starting from row with 'DIGITAL'
        current_category = None
        for idx, row in df.iloc[2:].iterrows():
            if pd.notna(row['Category']):
                if current_category:
                    data['categories'].append(current_category)
                current_category = {
                    'name': row['Category'],
                    'items': [],
                    'delivered': 0,
                    'total': 0,
                    'health': 0.0
                }
            elif pd.notna(row['Item']) and current_category:
                current_category['items'].append(row['Item'])
            elif pd.notna(row['Metric']) and current_category:
                if row['Metric'] == 'Delivered':
                    current_category['delivered'] = int(row['Value'])
                elif row['Metric'] == 'Total':
                    current_category['total'] = int(row['Value'])
                elif row['Metric'] == 'Health':
                    current_category['health'] = float(row['Value'])
        
        if current_category:
            data['categories'].append(current_category)
        
        return data
    
    def _generate_progress_bar(self) -> str:
        """Generate the sprint progress bar HTML."""
        sprints = ['17.1', '17.2', '17.3', '17.4', '17.5', '17.6']
        current = '17.1'
        
        html = '<div class="progress-container">'
        for sprint in sprints:
            active = 'active' if sprint == current else ''
            html += f'<div class="progress-item {active}">{sprint}</div>'
        html += '</div>'
        return html
    
    def _generate_category_card(self, category: Dict, index: int) -> str:
        """Generate HTML for a single category card."""
        name = category['name']
        items = category['items']
        delivered = category['delivered']
        total = category['total']
        health = category['health']
        
        # Determine header style based on position
        header_class = 'card-header-primary' if index == 0 else 'card-header-secondary'
        
        items_html = ''.join([f'<div class="item">✓ {item}</div>' for item in items])
        
        return f'''
        <div class="card">
            <div class="card-header {header_class}">
                <h2>{name}</h2>
                {items_html}
            </div>
            <div class="card-body">
                <div class="metric-large">{delivered}</div>
                <div class="metric-divider"></div>
                <div class="metric-large">{total}</div>
                <div class="metric-label">FEATURES DELIVERED</div>
            </div>
            <div class="card-footer">
                <div class="health-score">{health:.2f}</div>
                <div class="health-divider"></div>
                <div class="health-max">4.00</div>
                <div class="health-label">HEALTH METRICS</div>
            </div>
        </div>
        '''
    
    def generate_html(self) -> str:
        """Generate complete HTML dashboard."""
        cards_html = ''.join([
            self._generate_category_card(cat, idx) 
            for idx, cat in enumerate(self.data['categories'])
        ])
        
        html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Digital Technology - Increment {self.data['increment']}</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: {self.FONTS['primary']};
            background-color: {self.COLORS['light_gray']};
            padding: 20px;
        }}
        
        .container {{
            max-width: 1400px;
            margin: 0 auto;
            background: white;
            padding: 30px;
            border-radius: 10px;
        }}
        
        .header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 20px;
        }}
        
        .title {{
            font-size: 36px;
            font-weight: {self.FONTS['weight_bold']};
            color: {self.COLORS['primary_blue']};
        }}
        
        .title .increment {{
            color: {self.COLORS['orange']};
        }}
        
        .subtitle {{
            font-size: 18px;
            color: {self.COLORS['orange']};
            margin-bottom: 5px;
        }}

        .subtitle .sprintrange {{
            font-weight: {self.FONTS['weight_bold']};;
            color: {self.COLORS['primary_blue']};
        }}
        
        .logo {{
            font-size: 32px;
            font-weight: {self.FONTS['weight_bold']};
            color: {self.COLORS['primary_blue']};
        }}
        
        .logo .industrial {{
            font-size: 14px;
            display: block;
            text-align: right;
            margin-top: -5px;
        }}
        
        .progress-container {{
            display: flex;
            background: {self.COLORS['light_gray']};
            border-radius: 25px;
            padding: 8px;
            margin-bottom: 30px;
            position: relative;
        }}
        
        .progress-item {{
            flex: 1;
            text-align: center;
            padding: 8px;
            color: #999;
            font-weight: {self.FONTS['weight_bold']};
            position: relative;
            z-index: 1;
        }}
        
        .progress-item.active {{
            background: {self.COLORS['orange']};
            color: white;
            border-radius: 20px;
            position: relative;
        }}
        
        .progress-item.active::after {{
            content: '';
            position: absolute;
            right: -15px;
            top: 50%;
            transform: translateY(-50%);
            width: 18px;
            height: 18px;
            background: {self.COLORS['primary_blue']};
            border-radius: 50%;
            border: 3px solid white;
        }}
        
        .cards-container {{
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 20px;
        }}
        
        .card {{
            border: 3px solid {self.COLORS['primary_blue']};
            border-radius: 15px;
            overflow: hidden;
            background: white;
        }}
        
        .card-header {{
            padding: 20px;
            color: white;
            min-height: 180px;
        }}
        
        .card-header-primary {{
            background: {self.COLORS['primary_blue']};
        }}
        
        .card-header-secondary {{
            background: linear-gradient(135deg, {self.COLORS['secondary_blue']} 0%, {self.COLORS['primary_blue']} 100%);
        }}
        
        .card-header h2 {{
            font-size: 24px;
            font-weight: {self.FONTS['weight_bold']};
            margin-bottom: 15px;
            line-height: 1.2;
        }}
        
        .item {{
            font-size: 13px;
            margin-bottom: 5px;
        }}
        
        .card-body {{
            padding: 30px 20px;
            text-align: center;
            background: white;
        }}
        
        .metric-large {{
            font-size: 120px;
            font-weight: {self.FONTS['weight_bold']};
            color: {self.COLORS['primary_blue']};
            line-height: 1;
            display: inline;
        }}
        
        .metric-divider {{
            height: 4px;
            background: {self.COLORS['orange']};
            margin: 10px 40px;
        }}
        
        .metric-label {{
            font-size: 16px;
            font-weight: {self.FONTS['weight_bold']};
            color: {self.COLORS['primary_blue']};
            margin-top: 15px;
        }}
        
        .card-footer {{
            background: {self.COLORS['orange']};
            padding: 20px;
            text-align: center;
            color: white;
        }}
        
        .health-score {{
            font-size: 48px;
            font-weight: {self.FONTS['weight_bold']};
            display: inline;
        }}
        
        .health-divider {{
            height: 3px;
            background: {self.COLORS['primary_blue']};
            margin: 8px 40px;
        }}
        
        .health-max {{
            font-size: 36px;
            font-weight: {self.FONTS['weight_bold']};
        }}
        
        .health-label {{
            font-size: 14px;
            font-weight: {self.FONTS['weight_bold']};
            margin-top: 8px;
            letter-spacing: 1px;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <div>                
                <div class="title">DIGITAL TECHNOLOGY – <span class="increment">INCREMENT {self.data['increment']}</span></div>
                <div class="subtitle">Delivery metrics for Sprint {self.data['sprint']}</div>
            </div>
            <div class="logo">
                SIME
                <span class="industrial">INDUSTRIAL</span>
            </div>
        </div>
        
        {self._generate_progress_bar()}
        
        <div class="cards-container">
            {cards_html}
        </div>
    </div>
</body>
</html>'''
        return html
    
    def save_html(self, output_path: str) -> None:
        """Generate and save HTML to file."""
        html = self.generate_html()
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html)


def create_sample_excel(output_path: str) -> None:
    """Create a sample Excel file with the expected structure."""
    data = {
        'Category': ['Sprint', 'Increment', 'DIGITAL TECHNOLOGY', None, None, None, 
                     'DIGITAL', None, None, None, None,
                     'ENTERPRISE APPLICATIONS', None, None, None, None,
                     'TECHNOLOGY OPERATIONS', None, None, None, None, None, None],
        'Item': [None, None, 'DIGITAL', 'ENTERPRISE APPLICATIONS', 'TECHNOLOGY OPERATIONS', None,
                 'AVATARS', 'DESTINO', 'SDI WEBSITE', 'XENO', None,
                 'AX GUARDIANS', 'DELTA 365', 'ENTERPRISE AUTOMATION', 'WARETEC', None,
                 'CSI', 'CYBER DEFENCE', 'CYBER OPERATIONS', 'ENTERPRISE ARCHITECTURE', 'GRC', 'JSOC', 'MATRIX'],
        'Metric': [None, None, None, None, None, None,
                   None, None, None, None, 'Delivered',
                   None, None, None, None, 'Delivered',
                   None, None, None, None, None, None, 'Delivered'],
        'Value': ['17.1 - 17.1', '17', None, None, None, None,
                  None, None, None, None, 3,
                  None, None, None, None, 0,
                  None, None, None, None, None, None, 2]
    }
    
    # Add Total and Health rows
    additional_rows = [
        {'Category': None, 'Item': None, 'Metric': 'Total', 'Value': 39},
        {'Category': None, 'Item': None, 'Metric': 'Health', 'Value': 3.63},
        {'Category': None, 'Item': None, 'Metric': 'Total', 'Value': 43},
        {'Category': None, 'Item': None, 'Metric': 'Health', 'Value': 3.58},
        {'Category': None, 'Item': None, 'Metric': 'Total', 'Value': 71},
        {'Category': None, 'Item': None, 'Metric': 'Health', 'Value': 3.21},
    ]
    
    df = pd.DataFrame(data)
    for row in additional_rows:
        df = pd.concat([df, pd.DataFrame([row])], ignore_index=True)
    
    df.to_excel(output_path, index=False)


# Unit Tests
class TestDashboardGenerator(unittest.TestCase):
    """Unit tests for DashboardGenerator class."""
    
    @classmethod
    def setUpClass(cls):
        """Create test Excel file before running tests."""
        cls.test_excel = 'test_dashboard_data.xlsx'
        create_sample_excel(cls.test_excel)
    
    def test_load_data_structure(self):
        """Test that data loads with correct structure."""
        generator = DashboardGenerator(self.test_excel)
        self.assertIn('sprint', generator.data)
        self.assertIn('increment', generator.data)
        self.assertIn('categories', generator.data)
        self.assertIsInstance(generator.data['categories'], list)
    
    def test_category_count(self):
        """Test correct number of categories are loaded."""
        generator = DashboardGenerator(self.test_excel)
        self.assertEqual(len(generator.data['categories']), 4)
    
    def test_category_structure(self):
        """Test that each category has required fields."""
        generator = DashboardGenerator(self.test_excel)
        for category in generator.data['categories']:
            self.assertIn('name', category)
            self.assertIn('items', category)
            self.assertIn('delivered', category)
            self.assertIn('total', category)
            self.assertIn('health', category)
    
    def test_html_generation(self):
        """Test that HTML is generated without errors."""
        generator = DashboardGenerator(self.test_excel)
        html = generator.generate_html()
        self.assertIsInstance(html, str)
        self.assertGreater(len(html), 1000)
        self.assertIn('<!DOCTYPE html>', html)
    
    def test_html_contains_data(self):
        """Test that generated HTML contains actual data."""
        generator = DashboardGenerator(self.test_excel)
        html = generator.generate_html()
        self.assertIn('INCREMENT 17', html)
        self.assertIn('DIGITAL TECHNOLOGY', html)
        self.assertIn('FEATURES DELIVERED', html)
        self.assertIn('HEALTH METRICS', html)
    
    def test_color_constants(self):
        """Test that color constants are properly defined."""
        self.assertEqual(DashboardGenerator.COLORS['primary_blue'], '#003d5c')
        self.assertEqual(DashboardGenerator.COLORS['orange'], '#ff6633')
    
    def test_progress_bar_generation(self):
        """Test progress bar HTML generation."""
        generator = DashboardGenerator(self.test_excel)
        progress_html = generator._generate_progress_bar()
        self.assertIn('17.1', progress_html)
        self.assertIn('17.6', progress_html)
        self.assertIn('active', progress_html)


def main():
    """Main execution function."""
    # Create sample Excel file
    excel_file = 'dashboard_data.xlsx'
    create_sample_excel(excel_file)
    print(f"Sample Excel file created: {excel_file}")
    
    # Generate dashboard
    generator = DashboardGenerator(excel_file)
    output_file = 'sprint_dashboard.html'
    generator.save_html(output_file)
    print(f"Dashboard generated: {output_file}")


if __name__ == '__main__':
    # Run main program
    main()
    
    # Run unit tests
    print("\nRunning unit tests...")
    unittest.main(argv=[''], exit=False, verbosity=2)

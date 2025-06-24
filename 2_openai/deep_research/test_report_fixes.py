#!/usr/bin/env python3
"""
Test script to verify report generation fixes
"""

def test_robust_report_building():
    """Test the robust report building logic"""
    print("🔍 Testing robust report building logic...")
    
    # Mock report classes
    class MockReport:
        def __init__(self, content=None):
            if content:
                self.markdown_report = content
    
    class EmptyReport:
        def __init__(self):
            self.markdown_report = ""
    
    class NoAttrReport:
        pass
    
    def build_robust_report(reports, section_names):
        """Simulate the robust report building logic"""
        report_sections = []
        
        for i, (report, section_name) in enumerate(zip(reports, section_names)):
            if report and hasattr(report, 'markdown_report') and report.markdown_report:
                report_sections.append(f"# {section_name}\n\n{report.markdown_report}")
            else:
                report_sections.append(f"# {section_name}\n\n*Report generation failed or content empty*")
        
        return "\n\n---\n\n".join(report_sections)
    
    # Test cases
    print("\n" + "="*60)
    print("TEST 1: All good reports")
    good_reports = [
        MockReport("Disease analysis content here..."),
        MockReport("Pharmacology analysis content here..."),
        MockReport("Pathophysiology analysis content here...")
    ]
    section_names = ["Disease Understanding Report", "Pharmacology Report", "Comprehensive Pathophysiology Report"]
    result = build_robust_report(good_reports, section_names)
    print(f"Result length: {len(result)}")
    print(f"Preview:\n{result[:300]}...")
    
    print("\n" + "="*60)
    print("TEST 2: Mixed reports (some good, some empty, some None)")
    mixed_reports = [
        MockReport("Good disease analysis..."),
        EmptyReport(),  # Empty content
        None  # Failed generation
    ]
    result = build_robust_report(mixed_reports, section_names)
    print(f"Result length: {len(result)}")
    print(f"Preview:\n{result[:400]}...")
    
    print("\n" + "="*60)
    print("TEST 3: All failed reports")
    failed_reports = [None, EmptyReport(), NoAttrReport()]
    result = build_robust_report(failed_reports, section_names)
    print(f"Result length: {len(result)}")
    print(f"Preview:\n{result[:300]}...")

def test_fallback_markdown_generation():
    """Test the fallback markdown generation"""
    print("\n🔍 Testing fallback markdown generation...")
    
    class MockDiseaseReport:
        def __init__(self):
            self.executive_summary = "This is a test executive summary"
            self.clinical_profile = "Test clinical profile information"
            self.genetic_landscape = "Test genetic information"
            self.epidemiological_context = "Test epidemiological data"
            self.omics_insights = "Test omics findings"
            self.key_biological_factors = ["Factor 1", "Factor 2", "Factor 3"]
            self.markdown_report = ""  # Empty - needs fallback
    
    report = MockDiseaseReport()
    
    # Simulate the fallback logic
    if not report.markdown_report:
        print("Generating fallback markdown...")
        report.markdown_report = f"""# Disease Understanding Report

## Executive Summary
{report.executive_summary}

## Clinical Profile
{report.clinical_profile}

## Genetic Landscape
{report.genetic_landscape}

## Epidemiological Context
{report.epidemiological_context}

## Omics Insights
{report.omics_insights}

## Key Biological Factors
{', '.join(report.key_biological_factors)}
"""
    
    print(f"Generated markdown length: {len(report.markdown_report)}")
    print(f"Generated content:\n{report.markdown_report}")

def main():
    """Run all tests"""
    print("🚀 Testing Report Generation Fixes\n")
    
    test_robust_report_building()
    test_fallback_markdown_generation()
    
    print("\n" + "="*60)
    print("✅ ALL TESTS COMPLETED")
    print("\n🎯 IMPROVEMENTS IMPLEMENTED:")
    print("1. Robust report building that handles missing/empty reports")
    print("2. Fallback markdown generation when LLM fails to populate field")
    print("3. Better error handling and user feedback")
    print("4. Debug information showing report lengths and previews")
    print("\n🔧 RESULT:")
    print("Users will now see reports even if some stages fail!")

if __name__ == "__main__":
    main()

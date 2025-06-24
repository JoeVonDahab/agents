#!/usr/bin/env python3
"""
Debug script to test report generation without full LLM calls
"""

def test_report_generation_flow():
    """Test the report generation flow to identify issues"""
    print("🔍 Testing report generation flow...")
    
    # Simulate a report object
    class MockReport:
        def __init__(self, content=""):
            self.markdown_report = content
    
    def test_validation(report, report_name):
        """Test the validation logic"""
        print(f"\nTesting {report_name}:")
        print(f"  Report exists: {report is not None}")
        
        if report:
            print(f"  Has markdown_report attr: {hasattr(report, 'markdown_report')}")
            if hasattr(report, 'markdown_report'):
                print(f"  markdown_report length: {len(report.markdown_report) if report.markdown_report else 0}")
                print(f"  markdown_report content preview: {repr(report.markdown_report[:100])}")
                
                # Test the validation condition
                validation_result = not report or not hasattr(report, 'markdown_report') or not report.markdown_report
                print(f"  Validation fails: {validation_result}")
                
                return not validation_result
        return False
    
    # Test cases
    print("="*60)
    print("TEST CASE 1: Empty report")
    empty_report = MockReport("")
    test_validation(empty_report, "Empty Report")
    
    print("\n" + "="*60)
    print("TEST CASE 2: Report with content")
    good_report = MockReport("# Disease Analysis\n\nThis is a comprehensive report...")
    test_validation(good_report, "Good Report")
    
    print("\n" + "="*60)
    print("TEST CASE 3: None report")
    test_validation(None, "None Report")
    
    print("\n" + "="*60)
    print("TEST CASE 4: Report without markdown_report attribute")
    class BadReport:
        pass
    bad_report = BadReport()
    test_validation(bad_report, "Bad Report (no attr)")
    
def test_stage_completion_logic():
    """Test the stage completion detection logic"""
    print("\n🔍 Testing stage completion logic...")
    
    # Simulate chunks that would come from the research manager
    test_chunks = [
        "Starting Stage 2...",
        "Phase A: Disease Understanding...",
        "✅ Disease report generated successfully (1234 characters)",
        "Phase B: Pharmacology...",
        "Some analysis content here...",
        "Phase C: Comprehensive Pathophysiology...",
        "Stage 2 complete. Comprehensive analysis ready.",
        "# Disease Understanding Report\n\nThis is the actual report content...",
        "Additional report content continues here..."
    ]
    
    stage2_complete = False
    accumulated_content = ""
    
    for chunk in test_chunks:
        print(f"Processing chunk: {chunk[:50]}...")
        accumulated_content += chunk + "\n"
        if "Stage 2 complete" in chunk:
            stage2_complete = True
            print("  ✅ Stage 2 completion detected!")
    
    print(f"\nStage 2 completed: {stage2_complete}")
    print(f"Total content length: {len(accumulated_content)}")
    print(f"Content preview:\n{accumulated_content[:200]}...")

def test_gradio_yielding():
    """Test how the Gradio yielding works"""
    print("\n🔍 Testing Gradio yielding pattern...")
    
    def mock_research_manager_stage():
        """Mock a research manager stage that yields content"""
        yield "Starting analysis..."
        yield "Intermediate results..."
        yield "Stage complete. Final report ready."
        yield "# Final Report\n\nDetailed analysis content here..."
    
    print("Simulating Gradio async iteration:")
    for i, chunk in enumerate(mock_research_manager_stage()):
        print(f"  Yield {i+1}: {chunk}")

def main():
    """Run all debug tests"""
    print("🚀 Debug Report Generation Issues\n")
    
    test_report_generation_flow()
    test_stage_completion_logic()
    test_gradio_yielding()
    
    print("\n" + "="*60)
    print("🎯 POTENTIAL ISSUES IDENTIFIED:")
    print("1. LLM may not be populating markdown_report field")
    print("2. Report content may be empty even if field exists")
    print("3. Stage completion detection may interfere with content yielding")
    print("4. Validation may be too strict")
    
    print("\n🔧 RECOMMENDED FIXES:")
    print("1. Add explicit markdown_report instructions to all agents")
    print("2. Add debug output to show actual report content")
    print("3. Ensure all report content is yielded to user")
    print("4. Add fallback report generation if LLM fails")

if __name__ == "__main__":
    main()

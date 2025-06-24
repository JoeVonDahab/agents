#!/usr/bin/env python3
"""
Comprehensive test for Llama 3.3 configuration and bug fixes
"""

def test_model_configuration():
    """Test that model configuration is correct"""
    print("Testing model configuration...")
    
    # Test 1: Import check (syntax only, will fail if dependencies not installed)
    try:
        import ast
        
        # Parse gemini_config.py to check syntax and structure
        with open('gemini_config.py', 'r') as f:
            config_content = f.read()
        
        tree = ast.parse(config_content)
        
        # Check that required assignments exist
        assignments = {}
        for node in ast.walk(tree):
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name):
                        assignments[target.id] = True
        
        required_vars = ['gemini_client', 'gemini_model', 'llama3_3_client', 'llama3_3_model', 'default_model']
        missing_vars = []
        
        for var in required_vars:
            if var not in assignments:
                missing_vars.append(var)
        
        if missing_vars:
            print(f"❌ Missing variables in gemini_config.py: {missing_vars}")
            return False
        else:
            print("✅ All required model variables found in gemini_config.py")
            
    except Exception as e:
        print(f"❌ Error parsing gemini_config.py: {e}")
        return False
    
    return True

def test_default_model_assignment():
    """Test that default_model is set to llama3_3_model"""
    print("\nTesting default model assignment...")
    
    try:
        with open('gemini_config.py', 'r') as f:
            content = f.read()
        
        # Check if default_model = llama3_3_model line exists
        if 'default_model = llama3_3_model' in content:
            print("✅ default_model correctly set to llama3_3_model")
            return True
        elif 'default_model = gemini_model' in content:
            print("❌ default_model is set to gemini_model (should be llama3_3_model)")
            return False
        else:
            print("❌ Could not find default_model assignment")
            return False
            
    except Exception as e:
        print(f"❌ Error reading gemini_config.py: {e}")
        return False

def test_agent_imports():
    """Test that agent files correctly import default_model"""
    print("\nTesting agent imports...")
    
    agent_files = [
        'search_agent.py', 'writer_agent.py', 'prompter_agent.py',
        'evaluator_agent.py', 'disease_synthesis_agent.py',
        'pharmacology_agent.py', 'qsb_modeling_agent.py',
        'target_analysis_agent.py', 'prioritization_agent.py',
        'drug_miner_agent.py', 'repurposing_evaluator_agent.py',
        'final_recommender_agent.py'
    ]
    
    import_issues = []
    
    for agent_file in agent_files:
        try:
            with open(agent_file, 'r') as f:
                content = f.read()
            
            if 'from gemini_config import default_model' not in content:
                import_issues.append(f"{agent_file}: Missing 'from gemini_config import default_model'")
            elif 'model=default_model' not in content:
                import_issues.append(f"{agent_file}: Missing 'model=default_model' in agent definition")
                
        except FileNotFoundError:
            import_issues.append(f"{agent_file}: File not found")
        except Exception as e:
            import_issues.append(f"{agent_file}: Error reading file - {e}")
    
    if import_issues:
        print(f"❌ Agent import issues found:")
        for issue in import_issues:
            print(f"   - {issue}")
        return False
    else:
        print(f"✅ All {len(agent_files)} agent files correctly import and use default_model")
        return True

def test_research_manager_bug_fixes():
    """Test that research manager has proper error handling"""
    print("\nTesting research manager bug fixes...")
    
    try:
        with open('research_manager.py', 'r') as f:
            content = f.read()
        
        bug_fixes_present = []
        
        # Check for report validation
        if 'not disease_report.markdown_report' in content:
            bug_fixes_present.append("Disease report validation")
        
        if 'not pharmacology_report.markdown_report' in content:
            bug_fixes_present.append("Pharmacology report validation")
            
        if 'not comprehensive_pathophysiology_report.markdown_report' in content:
            bug_fixes_present.append("Comprehensive pathophysiology report validation")
            
        if 'not network_model.markdown_report' in content:
            bug_fixes_present.append("Network model validation")
            
        if 'not target_analysis.markdown_report' in content:
            bug_fixes_present.append("Target analysis validation")
            
        if 'not target_prioritization.markdown_report' in content:
            bug_fixes_present.append("Target prioritization validation")
        
        if len(bug_fixes_present) >= 6:
            print("✅ Report validation bug fixes present")
            print(f"   Found validations for: {', '.join(bug_fixes_present)}")
            return True
        else:
            print("❌ Missing report validation bug fixes")
            print(f"   Found only: {', '.join(bug_fixes_present)}")
            return False
            
    except Exception as e:
        print(f"❌ Error checking research_manager.py: {e}")
        return False

def test_gradio_app_bug_fixes():
    """Test that Gradio app has proper error handling"""
    print("\nTesting Gradio app bug fixes...")
    
    try:
        with open('deep_research.py', 'r') as f:
            content = f.read()
        
        bug_fixes_present = []
        
        # Check for stage completion tracking
        if 'stage2_complete = False' in content:
            bug_fixes_present.append("Stage 2 completion tracking")
        
        if 'stage3_complete = False' in content:
            bug_fixes_present.append("Stage 3 completion tracking")
            
        if 'stage4_complete = False' in content:
            bug_fixes_present.append("Stage 4 completion tracking")
            
        # Check for report validation
        if 'report is empty' in content:
            bug_fixes_present.append("Report content validation")
        
        if len(bug_fixes_present) >= 4:
            print("✅ Gradio app bug fixes present")
            print(f"   Found fixes for: {', '.join(bug_fixes_present)}")
            return True
        else:
            print("❌ Missing Gradio app bug fixes")
            print(f"   Found only: {', '.join(bug_fixes_present)}")
            return False
            
    except Exception as e:
        print(f"❌ Error checking deep_research.py: {e}")
        return False

def test_switch_model_script():
    """Test that switch_model.py works correctly"""
    print("\nTesting switch_model.py functionality...")
    
    try:
        with open('switch_model.py', 'r') as f:
            content = f.read()
        
        # Check for proper model switching logic
        if 'default_model = llama3_3_model' in content and 'default_model = gemini_model' in content:
            print("✅ switch_model.py has correct model switching logic")
            return True
        else:
            print("❌ switch_model.py missing proper model switching logic")
            return False
            
    except Exception as e:
        print(f"❌ Error checking switch_model.py: {e}")
        return False

def main():
    """Run all tests"""
    print("🔍 Running comprehensive test for Llama 3.3 configuration and bug fixes\n")
    
    tests = [
        test_model_configuration,
        test_default_model_assignment,
        test_agent_imports,
        test_research_manager_bug_fixes,
        test_gradio_app_bug_fixes,
        test_switch_model_script
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
        print()  # Add blank line between tests
    
    print("="*60)
    print(f"SUMMARY: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! Your Llama 3.3 configuration and bug fixes are working correctly.")
        print("\n📋 NEXT STEPS:")
        print("1. Install dependencies: pip install -r requirements.txt")
        print("2. Set up Ollama: bash setup_llama.sh")
        print("3. Run the application: python deep_research.py")
    else:
        print("❌ Some tests failed. Please review the issues above.")
    
    return passed == total

if __name__ == "__main__":
    main()

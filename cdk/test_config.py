#!/usr/bin/env python3
"""
Simple test script to validate CDK configuration
"""

import sys
import os

def test_imports():
    """Test that all required imports work"""
    try:
        import aws_cdk as cdk
        from aws_cdk import (
            Stack,
            aws_s3_deployment as s3deploy,
            aws_cloudfront as cloudfront,
            aws_s3 as s3,
            RemovalPolicy,
            Duration,
            CfnOutput
        )
        from constructs import Construct
        from aws_solutions_constructs.aws_cloudfront_s3 import CloudFrontToS3
        print("✅ All imports successful")
        return True
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False

def test_stack_creation():
    """Test that the stack can be created without errors"""
    try:
        from personal_website_stack import PersonalWebsiteStack
        import aws_cdk as cdk
        
        app = cdk.App()
        
        # Test stack creation
        stack = PersonalWebsiteStack(
            app, 
            "TestStack"
        )
        
        print("✅ Stack creation successful")
        return True
    except Exception as e:
        print(f"❌ Stack creation error: {e}")
        return False

def main():
    """Run all tests"""
    print("🧪 Testing CDK Configuration...")
    print()
    
    tests = [
        ("Import Test", test_imports),
        ("Stack Creation Test", test_stack_creation)
    ]
    
    results = []
    for test_name, test_func in tests:
        print(f"Running {test_name}...")
        result = test_func()
        results.append(result)
        print()
    
    # Summary
    passed = sum(results)
    total = len(results)
    
    print("=" * 50)
    print(f"Test Results: {passed}/{total} passed")
    
    if passed == total:
        print("🎉 All tests passed! CDK configuration is valid.")
        sys.exit(0)
    else:
        print("❌ Some tests failed. Please check the configuration.")
        sys.exit(1)

if __name__ == "__main__":
    main()

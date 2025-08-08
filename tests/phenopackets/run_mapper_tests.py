import unittest
import sys
from pathlib import Path
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("phenopackets_test_run.log")
    ]
)

logger = logging.getLogger(__name__)

# Define the list of available mappers for easy reference
AVAILABLE_MAPPERS = [
    "base",
    "disease",
    "individual",
    "vital_status",
    "variation_descriptor",
    "interpretation",
    "phenotypic_feature",
    "measurement",
    "metadata",
    "medical_action"
]

def run_all_mapper_tests():
    """
    Discovers and runs all mapper tests in the mappings directory.
    """
    # Get the current directory (where this script is located)
    current_dir = Path(__file__).parent
    
    # Add the project root to the Python path if needed
    project_root = current_dir.parent.parent
    if str(project_root) not in sys.path:
        sys.path.insert(0, str(project_root))
    
    # Find and run tests
    test_loader = unittest.TestLoader()
    
    # Get all tests from the mappings directory
    mapper_test_dir = current_dir / "mappings"
    logger.info(f"Looking for tests in {mapper_test_dir}")
    
    # Check if directory exists
    if not mapper_test_dir.exists():
        logger.error(f"Test directory {mapper_test_dir} does not exist")
        return 1
    
    # Discover tests
    mapper_test_suite = test_loader.discover(
        start_dir=str(mapper_test_dir),
        pattern="test_*.py"
    )
    
    # Count tests
    test_count = mapper_test_suite.countTestCases()
    logger.info(f"Found {test_count} tests to run")
    
    if test_count == 0:
        logger.warning("No tests found. Make sure test files follow the naming pattern 'test_*.py'")
        return 1
    
    # Run the tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(mapper_test_suite)
    
    # Log results
    logger.info(f"Tests run: {result.testsRun}")
    logger.info(f"Errors: {len(result.errors)}")
    logger.info(f"Failures: {len(result.failures)}")
    
    # Return exit code based on test result
    return 0 if result.wasSuccessful() else 1

def run_specific_mapper_test(mapper_name):
    """
    Runs a specific mapper test module.
    
    Args:
        mapper_name (str): Name of the mapper (e.g., 'disease', 'individual', 'vital_status')
    
    Returns:
        int: Exit code (0 for success, 1 for failure)
    """
    # Get the current directory (where this script is located)
    current_dir = Path(__file__).parent
    
    # Add the project root to the Python path if needed
    project_root = current_dir.parent.parent
    if str(project_root) not in sys.path:
        sys.path.insert(0, str(project_root))
    
    # Validate mapper name
    if mapper_name not in AVAILABLE_MAPPERS:
        logger.error(f"Unknown mapper: {mapper_name}")
        logger.info(f"Available mappers: {', '.join(AVAILABLE_MAPPERS)}")
        return 1
    
    # Find and run tests
    logger.info(f"Running tests for mapper: {mapper_name}")
    
    try:
        # Import the specific test module
        module_name = f"tests.phenopackets.mappings.test_{mapper_name}_mapper"
        
        # Try to import it
        try:
            test_module = __import__(module_name, fromlist=['*'])
        except ImportError:
            logger.error(f"Could not import test module {module_name}")
            return 1
        
        # Create test suite from the module
        test_loader = unittest.TestLoader()
        test_suite = test_loader.loadTestsFromModule(test_module)
        
        # Run the tests
        runner = unittest.TextTestRunner(verbosity=2)
        result = runner.run(test_suite)
        
        # Log results
        logger.info(f"Tests run: {result.testsRun}")
        logger.info(f"Errors: {len(result.errors)}")
        logger.info(f"Failures: {len(result.failures)}")
        
        # Return exit code based on test result
        return 0 if result.wasSuccessful() else 1
        
    except Exception as e:
        logger.error(f"Error running tests for {mapper_name}: {e}")
        return 1

if __name__ == "__main__":
    if len(sys.argv) > 1:
        # Run specific mapper test
        mapper_name = sys.argv[1]
        
        if mapper_name == "--list":
            # List available mappers
            print("Available mappers:")
            for mapper in AVAILABLE_MAPPERS:
                status = "✅" if mapper in ["base", "disease", "individual", "vital_status", "variation_descriptor", "interpretation", "phenotypicfeature"] else "⬜"
                print(f"  {status} {mapper}")
            sys.exit(0)
        elif mapper_name == "--help":
            # Show help
            print("Usage: python run_mapper_tests.py [OPTION]")
            print()
            print("Options:")
            print("  <mapper_name>    Run tests for a specific mapper")
            print("  --list           List all available mappers")
            print("  --help           Show this help message")
            print("  (no arguments)   Run all mapper tests")
            print()
            print("Available mappers:")
            for mapper in AVAILABLE_MAPPERS:
                print(f"  - {mapper}")
            sys.exit(0)
            
        logger.info(f"Running tests for mapper: {mapper_name}")
        sys.exit(run_specific_mapper_test(mapper_name))
    else:
        # Run all tests
        logger.info("Running all mapper tests")
        sys.exit(run_all_mapper_tests())
        

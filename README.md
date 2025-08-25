# Manual Testing Project

A comprehensive automated testing project for the [Bellatrix Demos website](https://demos.bellatrix.solutions/) using Playwright with Python and pytest.

## 🚀 Project Overview

This project provides automated testing for e-commerce functionality including:
- **Shop Operations**: Product browsing, cart management, search functionality
- **Contact Forms**: Form validation, accessibility, user interactions
- **Promotions**: Category navigation, product displays, special offers
- **Accessibility**: ARIA compliance, keyboard navigation, screen reader support

## 📁 Project Structure

```
Manual Testing/
├── tests/                          # Test files
│   ├── test_shop.py              # Shop functionality tests
│   ├── test_contact_form.py      # Contact form tests
│   ├── test_promotions.py        # Promotions tests
│   └── README.md                 # Test documentation
├── chatmodes/                     # AI assistant modes
│   ├── test-generator.chatmode.md    # Test generation mode
│   ├── test-explorer.chatmode.md     # Website exploration mode
│   └── playwright-tester.chatmode.md # Playwright testing mode
├── instructions/                   # Testing guidelines
│   └── playwright.instructions.md # Playwright best practices
├── prompts/                        # AI prompt templates
│   └── improve-documentation.prompt.md # Documentation improvement
├── conftest.py                    # Pytest configuration and fixtures
├── pytest.ini                     # Pytest settings
├── requirements.txt               # Python dependencies
└── README.md                      # This file
```

## 🛠️ Prerequisites

- **Python** 3.8 or higher
- **pip** package manager
- **Git** for version control

## 📦 Installation

1. **Clone the repository**:
    ```bash
    git clone <repository-url>
    cd "Manual Testing"
    ```

2. **Install Python dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Install Playwright browsers**:
    ```bash
    playwright install
    ```

## 🏃‍♂️ Running Tests

### **Basic Test Execution**
```bash
# Run all tests
pytest tests/

# Run specific test file
pytest tests/test_shop.py

# Run with verbose output
pytest tests/ -v
```

### **Browser Modes**
```bash
# Run with headed browser (visible)
pytest tests/ --headed

# Run with headless browser (hidden) - default
pytest tests/ --headless
```

### **Advanced Options**
```bash
# Run tests in parallel
pytest tests/ -n auto

# Run with retry on failure
pytest tests/ --reruns 3

# Run specific browser
pytest tests/ --browser=firefox

# Run with coverage
pytest tests/ --cov=tests --cov-report=html
```

## 🔧 Configuration

### **pytest.ini**
Basic pytest configuration including test paths and default options.

### **conftest.py**
Custom fixtures and configuration including:
- Browser launch arguments
- Headless mode configuration
- Custom test fixtures

### **requirements.txt**
Python package dependencies:
- `pytest` - Testing framework
- `pytest-playwright` - Playwright integration
- `playwright` - Browser automation
- `pytest-xdist` - Parallel execution
- `pytest-rerunfailures` - Retry failed tests

## 🎯 Test Organization

### **Test Classes**
Tests are organized in descriptive classes:
- `TestBellatrixDemosShop` - Shop functionality
- `TestBellatrixDemosContactForm` - Contact form testing
- `TestBellatrixDemosPromotions` - Promotions and categories

### **Test Methods**
Each test method follows the pattern:
```python
def test_display_shop_homepage_with_all_products(self, page: Page) -> None:
    """Test that the shop homepage displays all products correctly."""
    # Test implementation
```

### **Fixtures**
Common setup using pytest fixtures:
```python
@pytest.fixture(autouse=True)
def setup(self, page: Page) -> None:
    """Setup for each test."""
    page.goto('https://demos.bellatrix.solutions/')
```

## ♿ Accessibility Testing

The test suite includes comprehensive accessibility verification:
- **ARIA landmarks**: Banner, main, navigation, contentinfo
- **Form labels**: Proper labeling for all inputs
- **Keyboard navigation**: Tab order and focus management
- **Semantic HTML**: Proper heading hierarchy and roles

## 🔍 AI Assistant Modes

### **Test Generator Mode**
- Generates comprehensive Playwright tests in Python
- Uses systematic website exploration
- Follows accessibility-first locator strategies
- Creates maintainable test structures

### **Test Explorer Mode**
- Systematically explores websites using Playwright
- Identifies user flows and interaction patterns
- Documents page structure and functionality
- Provides test planning recommendations

### **Playwright Tester Mode**
- Creates and maintains Python-based Playwright tests
- Provides testing best practices and guidance
- Helps with debugging and troubleshooting
- Integrates with existing test suite

## 📚 Documentation

- **`tests/README.md`**: Comprehensive test documentation
- **`instructions/playwright.instructions.md`**: Playwright best practices
- **`chatmodes/*.chatmode.md`**: AI assistant mode definitions

## 🐛 Troubleshooting

### **Common Issues**

1. **Browser not installed**:
    ```bash
    playwright install
    ```

2. **Tests timing out**:
    - Check internet connection
    - Verify website accessibility
    - Increase timeout if needed

3. **Python path issues**:
    - Ensure you're in the project root directory
    - Check that `tests/` directory exists
    - Verify pytest is installed: `pip show pytest`

### **Debug Mode**
```bash
pytest tests/ --pdb
```

## 📈 Continuous Integration

Tests are designed for CI/CD environments:
- **Parallel execution** with pytest-xdist
- **Retry logic** with pytest-rerunfailures
- **Artifact capture** (screenshots, videos, traces)
- **Proper exit codes** for CI integration

### **CI Example**
```yaml
# GitHub Actions example
- name: Run Tests
  run: |
    pip install -r requirements.txt
    playwright install
    pytest tests/ --headless
```

## 🤝 Contributing

When contributing to the test suite:

1. **Follow existing patterns** and structure
2. **Test locally** before submitting
3. **Maintain accessibility focus**
4. **Update documentation** as needed
5. **Ensure all tests pass** consistently

### **Development Workflow**
```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Install browsers
playwright install

# 3. Run tests locally
pytest tests/ -v

# 4. Run specific test during development
pytest tests/test_shop.py -v -s

# 5. Run with headed mode for debugging
pytest tests/test_shop.py --headed
```

## 📚 Resources

- [Playwright Python Documentation](https://playwright.dev/python/)
- [Pytest Documentation](https://docs.pytest.org/)
- [Pytest-Playwright Documentation](https://pytest-playwright.readthedocs.io/)
- [Accessibility Testing Guide](https://playwright.dev/docs/accessibility-testing)
- [Best Practices](https://playwright.dev/docs/best-practices)
- [Python Testing with Pytest](https://pytest.org/en/stable/)

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

**Note**: These tests are designed for the Bellatrix Demos website and may need updates if the website structure changes significantly. Always test locally before running in CI/CD environments.

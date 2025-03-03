# Playwright E2E Testing for Magento Store

## Project Overview
This project is a practice exercise for creating End-to-End (E2E) automation tests using [Playwright](https://playwright.dev/python/) on the [Magento Store](https://magento.softwaretestingboard.com/). It helps in understanding test automation concepts and improving skills in writing Playwright test scripts.

## Prerequisites
Before running the tests, ensure you have the following installed:
- [Python](https://www.python.org/) (Recommended version: 3.8+)
- [Playwright](https://playwright.dev/python/)
- [pytest](https://docs.pytest.org/en/latest/)

## Installation
1. Clone the repository:
   ```sh
   git clone <repository-url>
   cd <repository-folder>
   ```
2. Install dependencies:
   ```sh
   pip install playwright pytest
   ```
3. Install Playwright browsers:
   ```sh
   playwright install
   ```

## Test Structure
The test suite consists of the following modules:

- **Pages**: Handles interactions with different sections of the website:
  - `home_page.py`: Navigates to login and men’s clothing section.
  - `login_page.py`: Handles user authentication.
  - `men_top_page.py`: Selects a product.
  - `product_page.py`: Chooses size, color, and quantity.
  - `shipping_page.py`: Fills shipping details.
  - `payment_page.py`: Validates price and completes checkout.
  - `after_checkout_page.py`: Confirms purchase and logs out.

- **Configuration**:
  - `config.py`: Stores test data (user credentials, product quantity, shipping info).

- **Test Execution**:
  - `test_user.py`: Runs the full E2E test.

## Running Tests
To execute the tests, use the following command:
```sh
pytest test_user.py
```

For **headless mode**, modify `test_user.py`:
```python
browser = await p.chromium.launch(headless=True)
```

## Reporting
Playwright provides built-in test reports. You can enable video recording by modifying `conftest.py`:
```python
context = await browser.new_context(record_video_dir="videos/")
```

## Conclusion
This project is designed to practice automation testing using Magento, providing hands-on experience with Playwright. Contributions and improvements are welcome!


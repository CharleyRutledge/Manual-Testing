# Pytest configuration to mirror Playwright JS settings
# This file sets sensible defaults for pytest-playwright options.
# You can override any of these via CLI flags when running pytest.

from __future__ import annotations
from typing import Any
import pytest


def pytest_addoption(parser: pytest.Parser) -> None:
    """Add custom command line options."""
    parser.addoption(
        "--headless",
        action="store_true",
        default=False,
        help="Run browser in headless mode (default: headed mode)"
    )


def pytest_configure(config: pytest.Config) -> None:
    """Configure pytest with Playwright defaults."""
    # Default to Chromium (equivalent to the JS project targeting Desktop Chrome)
    if not getattr(config.option, "browser", None):
        config.option.browser = "chromium"

    # Artifact policies similar to JS config
    if not getattr(config.option, "screenshot", None):
        config.option.screenshot = "only-on-failure"

    if not getattr(config.option, "video", None):
        config.option.video = "retain-on-failure"

    # Python plugin supports: off | on | retain-on-failure
    if not getattr(config.option, "tracing", None):
        config.option.tracing = "retain-on-failure"


@pytest.fixture(scope="session")
def browser_name(request: pytest.FixtureRequest) -> str:
    """Get the browser name from command line options or default."""
    return getattr(request.config.option, "browser", "chromium")


@pytest.fixture(scope="session")
def headless(request: pytest.FixtureRequest) -> bool:
    """Get the headless flag from command line options."""
    return getattr(request.config.option, "headless", False)


@pytest.fixture(scope="session")
def browser_launch_args(browser_launch_args: dict, headless: bool) -> dict:
    """Configure browser launch arguments including headless mode."""
    # Set headless mode based on the flag
    if headless:
        browser_launch_args["headless"] = True
    else:
        browser_launch_args["headless"] = False
    
    return browser_launch_args

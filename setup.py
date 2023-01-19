from setuptools import find_packages, setup

setup(
    name="screenshotter",
    version="0.1.0",
    license="MIT",
    description="Automatically take full-screen screenshots at a fixed rate",
    author="Chase Vaughan",
    author_email="contact@cvaugh.dev",
    packages=find_packages(),
    url="https://github.com/cvaugh/screenshotter",
    install_requires=[
        "screeninfo==0.8.1",
        "pillow==9.3.0",
        "pyautogui==0.9.53",
    ],
    entry_points={
        "console_scripts": [
            "screenshotter = screenshotter:main",
        ],
    },
    keywords=["screenshot", "automation"],
)

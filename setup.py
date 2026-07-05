"""
Setup configuration for Jarvis Assistant
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="jarvis-assistant",
    version="1.0.0",
    author="anuphulageri0143-maker",
    description="A Python-based AI voice assistant with task automation capabilities",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/anuphulageri0143-maker/jarvis1",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.8",
    install_requires=[
        "SpeechRecognition==3.10.0",
        "pyttsx3==2.90",
        "PyAudio==0.2.13",
        "requests==2.31.0",
        "python-dotenv==1.0.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0",
            "pytest-cov>=4.0",
            "black>=22.0",
            "flake8>=4.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "jarvis=jarvis.assistant:main",
        ],
    },
)

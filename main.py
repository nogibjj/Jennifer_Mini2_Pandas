"""
Main cli or app entry point
"""

from mylib.calculator import load_dataset
import click


def g_describe():
    g = load_dataset()
    return g_describe()


def save_to_md():
    with open("test.md", "a") as file:
        file.write("test")


if __name__ == "__main__":
    save_to_md()

from setuptools import setup, find_packages


setup(
    name="uf2",
    version="0.1.0",
    url="https://github.com/microsoft/uf2",
    description="Packing and unpacking UF2 files",

    packages=find_packages(),

    package_data={
        "uf2": [
            "uf2families.json"
            ]
        },

    entry_points = {
        "console_scripts": [
            "uf2conv = uf2.uf2conv:main"
            ]
        }

)

if __name__ == "__main__":
    setup()

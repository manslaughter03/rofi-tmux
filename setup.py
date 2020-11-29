from setuptools import setup, find_packages


setup(
    name="rofitmux",
    version="0.0.1",
    description="Tmux window selection from rofi windows",
    url="",
    author="b4nks@protonmail.com",
    license="MIT",
    entry_points={
        'console_scripts': [
            'rofitmux = rofitmux.__main__:main'
        ]
    },
    classifiers=[
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Twitter Tools',
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    python_requires='>=3.5',
    packages=find_packages(),
    install_requires=[
        "python-rofi==1.0.1",
        "libtmux==0.8.5"
    ]
)

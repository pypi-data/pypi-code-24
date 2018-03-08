import setuptools

setuptools.setup(
    name="mautrix-appservice",
    version="0.1.0",
    url="https://github.com/tulir/mautrix-appservice",

    author="Tulir Asokan",
    author_email="tulir@maunium.net",

    description="A Python 3 asyncio-based Matrix application service framework.",
    long_description=open("README.md").read(),

    packages=setuptools.find_packages(),

    install_requires=[
        "aiohttp>=3.0.1,<4",
        "future-fstrings>=0.4.2",
    ],
    extras_require={
        "detect_mimetype": ["python-magic>=0.4.15,<0.5"],
    },
    python_requires="~=3.5",

    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Topic :: Communications :: Chat",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
    ]
)


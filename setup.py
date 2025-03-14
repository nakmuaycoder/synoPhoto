from setuptools import setup

setup(
    name='synoPhoto',
    maintainer="นักมวยโคเดอร์",
    version='0.1',
    install_requires=[
        'importlib-metadata; python_version<"3.10"',
        'freeMobileSMS @ git+https://github.com/nakmuaycoder/freeMobileSMS.git'
    ],   package_dir = {
            "synoPhoto": "synoPhoto",
        },
    entry_points={
        'console_scripts': [
            'synoPhoto= synoPhoto.__main__:main',
        ]
    }
)
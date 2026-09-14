"""Setup script for YmerFlow plugin-building process types."""

from setuptools import setup, find_packages

setup(
    name="ymerflow-plugin-processes",
    version="0.1.0",
    description="Image/artifact-building YmerFlow process types that depend on the plugin SDK "
                "(build_frontend_plugin).",
    packages=find_packages(include=["ymerflow_plugin_processes", "ymerflow_plugin_processes.*"]),
    python_requires=">=3.9",
    install_requires=[
        "fsspec",
        "s3fs",
        "gcsfs",
        "ymerflow-plugin-build @ git+https://github.com/YmerFlow/Ymerflow-plugin-sdk.git",
    ],
    entry_points={
        "ymerflow.process_types": [
            "build_frontend_plugin=ymerflow_plugin_processes.build_frontend_plugin:build_frontend_plugin",
        ],
    },
)

# windows: Remove-Item -Recurse -Force .\dist, .\build, .\.egg-info; poetry build; python -m twine upload dist/*
# linux: rm -rf dist/ build/ .egg-info; poetry build; python3 -m twine upload dist/
# https://packaging.python.org/en/latest/tutorials/packaging-projects/#uploading-your-project-to-pypi
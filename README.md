# Django Package Template

## Usage

After create the Django project by Coding depot, please edit:

- `pyproject.toml`: `name`, `description`, `license`, `homepage`, `repository` and other metadata.
- `django_package`: directory name to your project name.
  - `app.py`: change `DjangoPackageConfig` and `name = 'django_package'` to your project name.
- `tests`:
  - `test_apps.py`: change the unittest according to the previous renaming.

## License

This Template uses [Apache 2.0 License](LICENSE). If you need to customize the license file to Apache 2.0 or other license, please feel free to change the LICENSE file and license option in `pyproject.toml`.

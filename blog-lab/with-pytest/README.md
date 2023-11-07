https://earthly.dev/blog/bazel-and-automated-tests/

```bash
source venv/bin/activate
pip install pytest


pytest lib/test_prime.py
pytest

bazel test //lib:test_prime
bazel test //...
```
https://earthly.dev/blog/bazel-and-automated-tests/

```bash
source venv/bin/activate
pip install pytest


pytest lib/test_prime.py
pytest

bazel test //lib:test_prime
bazel test //...


### dependency graph
bazel query --noimplicit_deps --notool_deps --output graph 'deps(//...)'
# http://www.webgraphviz.com/

```


```bash
cd yt_bazel_tutorial


### py_calculator
bazel build //projects/project2/calculator:calculator
bazel test //projects/project2/calculator:calculator_test


### py_web
bazel build projects/project2/my-python-app:main
bazel run projects/project2/my-python-app:main
```
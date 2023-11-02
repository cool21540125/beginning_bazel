

```bash
cd yt_bazel_tutorial


### python_calculator
bazel build //projects/project2/python_calculator:calculator
bazel test //projects/project2/python_calculator:calculator_test


### my-python-app
bazel build projects/project2/my-python-app:main
bazel run projects/project2/my-python-app:main
```
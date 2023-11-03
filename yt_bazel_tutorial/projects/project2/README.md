

```bash
cd yt_bazel_tutorial


### build
bazel build //projects/project2/python_calculator:calculator
bazel build //projects/project2/python_web:main
bazel build //projects/project2/...


### test
bazel test //projects/project2/python_calculator:calculator_test
bazel test //projects/project2/...


### run web
bazel run projects/project2/python_web:main
```
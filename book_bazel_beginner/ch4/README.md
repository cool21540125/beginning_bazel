
```bash
cd book_bazel_beginner


bazel build //ch4/golang:hello_world_go
bazel build //ch4/python:hello_world_python
bazel build //ch4/...

bazel test //ch4/python:calculator_test
bazel test //ch4/...

bazel run //ch4/python:hello_world_python
bazel run //ch4/golang:hello_world_go
```

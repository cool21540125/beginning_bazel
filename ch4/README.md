
```bash
### go
bazel build //ch4/src:hello_world_go

bazel run ch4/src:hello_world_go


### python
bazel build //ch4/ex_simple_python:hello_world_python

bazel run //ch4/ex_simple_python:hello_world_python

bazel test //ch4/ex_lib_python:calculator_test
```

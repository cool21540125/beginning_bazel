# Golang & Gazelle

```bash
### (首次使用)
cd projects/project4
go mod init github.com/cool21540125/demo_bzel_golang
go work init .
go mod tidy

go test
go build

cd ../..
```


```bash
cd yt_bazel_tutorial

### 自寫 library & test
bazel test //projects/project4/go_calculator:go_calculator_test
bazel test //projects/project4/...
bazel test //projects/...

### build
bazel build //projects/project4/go_calculator
bazel build //projects/project4/go_web:go_web
bazel build //projects/project4/...
bazel build //projects/...


### query / analyze
bazel query @com_github_gorilla_mux//...


### run web
bazel run //projects/project4/go_web
```
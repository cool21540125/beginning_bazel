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
bazel test //projects/project4/go_hello_world:go_hello_world_test
bazel build //projects/project4/go_hello_world


### query / analyze
bazel query @com_github_gorilla_mux//...


### mux
bazel build //projects/project4/go_web:go_web
bazel run //projects/project4/go_web
```
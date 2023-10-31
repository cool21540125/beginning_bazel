# [Building Golang With Bazel and Gazelle](https://earthly.dev/blog/build-golang-bazel-gazelle/)

- [Github bazel-demo-app](https://github.com/Shulammite-Aso/bazel-demo-app/tree/before-bazel)


# Note

- Bazel 原生支援 Golang
    - 需要自行 load rules_go


```bash
### 使用 gazelle 生成 WORKSPACE 裡頭 package 的 BUILD.bazel
gazelle -go_prefix github.com/Shulammite-Aso/bazel-demo-app
# -go_prefix xxx 替換為 go.mod 的 module 路徑
```
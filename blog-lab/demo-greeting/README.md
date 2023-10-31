# [Building Golang With Bazel and Gazelle](https://earthly.dev/blog/build-golang-bazel-gazelle/)

- [Github bazel-demo-app](https://github.com/Shulammite-Aso/bazel-demo-app/tree/before-bazel)


# Note

- Bazel 原生支援 Golang
    - 會偵測 go.mod, 自動生成專案內的 BUILD.bazel (免自行撰寫, 超強 der)
    - 不過需要自行處理 external dependencies. 參考 `gazelle update-repos`

```bash
cd blog-lab/demo-greeting

### 使用 gazelle 生成 WORKSPACE 裡頭 package 的 BUILD.bazel
gazelle -go_prefix github.com/Shulammite-Aso/bazel-demo-app
# -go_prefix xxx 替換為 go.mod 的 module 路徑
# 會幫忙生出專案內的 BUILD


### 讓 gazel 由 go.mod 找出 external deps
gazelle update-repos -from_file=go.mod -to_macro=deps.bzl%go_dependencies -prune
# 生成 //deps.bzl && 同時也會修改 WORKSPACE.bazel


touch BUILD.bazel
# 需要確保 //deps.bzl 所在位置有 BUILD.bazel

bazel build //...
bazel test //...
bazel run //cmd
# 之後便可正常執行
```


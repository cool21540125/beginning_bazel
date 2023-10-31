
- https://www.youtube.com/watch?v=BZYj6yfA6Bs&list=PLdk2EmelRVLovmSToc_DK7F1DV_ZEljbx&index=1

```bash
### 先進入 workspace
cd yt_bazel_tutorial


### ====== build all ======
bazel build //...
# bazel build //:all


### ====== projectA ======
bazel build //projects/projectA/...
bazel build //projects/projectA:foo


### ====== projectB ======
bazel build //projects/projectB/calculator:calc

bazel test //projects/projectB/calculator:calc_test


### ====== projectC ======
bazel build //projects/projectC/my-python-app:app


# 查看 targets in the package
bazel query "//projects/projectC/my-python-app:*"


# 
```

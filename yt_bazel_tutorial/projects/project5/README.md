- [Bazel & NodeJS Tutorial: library, test & nodejs_binary (internal & external deps)](https://www.youtube.com/watch?v=lmWjRhFhvSc&list=PLdk2EmelRVLovmSToc_DK7F1DV_ZEljbx&index=5)
- 從頭到尾都看得不是很懂=.=

```bash
cd yt_bazel_tutorial

### 依照 package.json 做 yarn install 並生成 yarn.lock
bazel run @yarn//:yarn


### query
bazel query @npm//... | grep jasmine
bazel query @npm//... | grep express


### build
bazel build //projects/project5/node_web:node_web
bazel build //projects/project5/node_web
bazel build //projects/project5/node_calculator
bazel build //projects/project5/...
bazel build //projects/...


### test
bazel test //projects/project5/node_calculator/...
bazel test //projects/...


### run web
bazel run //projects/project5/node_web
```
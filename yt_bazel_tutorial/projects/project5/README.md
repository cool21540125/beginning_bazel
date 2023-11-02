- [Bazel & NodeJS Tutorial: library, test & nodejs_binary (internal & external deps)](https://www.youtube.com/watch?v=lmWjRhFhvSc&list=PLdk2EmelRVLovmSToc_DK7F1DV_ZEljbx&index=5)
- 從頭到尾都看得不是很懂=.=

```bash
cd yt_bazel_tutorial

### 依照 package.json 做 yarn install 並生成 yarn.lock
bazel run @yarn//:yarn


### 
bazel query @npm//... | grep jasmine
bazel query @npm//... | grep express


### 
bazel test //projects/project5/node_calculator/...
bazel test //projects/...


bazel build //projects/project5/node_web
bazel run //projects/project5/node_web
```
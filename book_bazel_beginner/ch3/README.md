

```bash
cd book_bazel_beginner

bazel build //ch3/src:LibraryExample
bazel build //ch3/...

bazel test //ch3/src:LibraryExampleTest
bazel test //ch3/...

bazel run //ch3/src:HelloWorld
```
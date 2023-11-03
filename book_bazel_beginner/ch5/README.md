
```bash
cd book_bazel_beginner


### Server
bazel build //ch5/src:echo_server
bazel run //ch5/src:echo_server


### Client - java
bazel build //ch5/src:echo_client
bazel run //ch5/src:echo_client


### Client - python
bazel build //ch5/src:echo_client_py
bazel run //ch5/src:echo_client
```
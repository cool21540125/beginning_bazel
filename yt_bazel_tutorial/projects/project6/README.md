
# Bazel - Docker

- IMPORTANT: rules_docker 已經不再維護. 改以 rules_oci 替代

```bash
cd yt_bazel_tutorial


### (repeated only for sure everything works fine)
bazel build //projects/project6/...
bazel test //projects/project6/...
bazel run //projects/project6/python_web:python_web


### run python_web
bazel run //projects/project6/python_web:python_web_image
# YT 教學說上面會有問題, 要用下面這個, 但我上面那個可以成功 (無腦先猜可能是 bazel 版本問題)
bazel run //projects/project6/python_web:python_web_image --@io_bazel_rules_docker//transitions:enable=no
# 但因為這樣太麻煩了, 因此可把這東西放到 .bazelrc

# 只做 build image (不運行)
bazel run //projects/project6/python_web:python_web_image -- --norun
docker run bazel/projects/project6/python_web:python_web_image


### push image
bazel run //projects/project6/python_web:push

```

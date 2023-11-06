
- https://www.youtube.com/watch?v=HPTzVHOcins&list=PLdk2EmelRVLovmSToc_DK7F1DV_ZEljbx&index=10

```bash
cd yt_bazel_tutorial


### query maven (這邊關於 maven 與 pin 我都不曉得在幹嘛)
# 此時還不能有 maven_install ( maven_install_json = "//:maven_install.json", )
bazel query @maven//...

# get initial 'maven_install.json'
bazel run @maven//:pin
# 會要我們加上 maven_install_json = "@//:maven_install.json",
# 加上以後再查詢, 會發現 extensions 都被納進來可以 query 到了
bazel query @maven//...

# 先把 maven_install( artifacts = [ "com.github.javafaker:javafaker:1.0.1" 修改為 1.0.2
bazel run @unpinned_maven//:pin
# 會替我們修改 maven_install.json 裡頭的版本



###
bazel build //projects/project10/src/main/java/com/cool21540125/javagreeter/greeter/...
bazel build //projects/project10/src/main/java/com/cool21540125/javagreeter/greeter:greeter

### 
bazel run //projects/project10/src/main/java/com/cool21540125/javagreeter/main:main
bazel run //projects/project10/src/main/java/com/cool21540125/javagreeter/main
```
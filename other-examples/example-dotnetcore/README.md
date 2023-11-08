
- 因為我根本不懂他媽 dotnet core 的一大堆專業術語, 所以要再找時間惡補
    - https://blog.miniasp.com/post/2021/10/25/ASP-NET-Core-6-Project-Template-and-CSharp-10-New-Features

```bash
cd other-examples/example-dotnetcore

### build
bazel build //aspnetcore:aspnetcore


### Server
bazel run //aspnetcore:aspnetcore


### Client
curl https://localhost:5001/weatherforecast
```

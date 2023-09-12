### 使用fastapi部署腾讯cos

#### 运行

##### 1.设置环境变量,，也可以直接修改cos.py文件

```text
COS_BUCKET=桶ID
COS_SECRET_ID=SECRET_ID
COS_SECRET_KEY=SECRET_KEY
```

##### 2.执行命令

```shell

pip install --upgrade pip cos-python-sdk-v5 fastapi python-multipart uvicorn -i https://mirrors.aliyun.com/pypi/simple/
uvicorn main:app --reload --host 0.0.0.0
```

#### 接口

- 上传文件：/upload
    - 请求方式：POST
    - 参数：
  ```
  Image: 图片字节
  ```
    - 返回：
  ```json
  {
	"code": 0,
	"msg": "文件上传成功，后端默认不保存图片信息，请自行保存图片路径",
	"data": {
		"filename": "LEO Pharma.jpg",
		"url": "https://kaixin-1319395195.cos.ap-beijing.myqcloud.com/3fa7b94f-80a6-4737-a9d0-b51f7bda740b.jpg",
		"raw": {
			"Content-Length": "0",
			"Connection": "keep-alive",
			"Date": "Tue, 12 Sep 2023 06:42:56 GMT",
			"ETag": "\"c6f6e2196ba6e014a4244ff1be49cf2b\"",
			"Server": "tencent-cos",
			"x-cos-hash-crc64ecma": "143385821157885427",
			"x-cos-request-id": "NjUwMDA4NzBfZDhiNTE0MGJfOWRiZl8zMzdmMDU4",
			"x-cos-storage-class": "STANDARD"
		}

}
}

- 检测：/ping
    - 请求方式：GET
    - 参数：
    - 返回:
  ```text
  pong
  ```
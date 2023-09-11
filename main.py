import logging
import uuid
from pathlib import Path

from fastapi import FastAPI, File, UploadFile

from cos import client, bucket

logger = logging.getLogger("cos-api")

app = FastAPI()

# 文件最大尺寸
MAX_SIZE = 1024 * 1024 * 5


@app.get("/ping")
async def root():
    return "pong"


@app.post('/upload', summary="上传图片", description="上传图片", tags=["upload"])
async def upload_file(image: UploadFile = File(alias="Image")):
    """
    上传图片
    :param image:
    :return:
    """

    # 限定尺寸
    if MAX_SIZE < image.size:
        return {"code": -1, "msg": "文件大小不能超过5M"}
    fileinfo = Path(image.filename)

    # 上传 图片
    key = f"{uuid.uuid4()}{fileinfo.suffix}"
    response = client.put_object(
        Bucket=bucket,
        Body=image.file.read(),
        Key=key

    )

    logger.info(response)

    # 获取图片链接

    url = client.get_object_url(
        Bucket=bucket,
        Key=key
    )
    return {
        "code": 0,
        "msg": "文件上传成功，后端默认不保存图片信息，请自行保存图片路径",
        "data": {
            "filename": image.filename,
            "url": url,
            "raw": response
        }
    }

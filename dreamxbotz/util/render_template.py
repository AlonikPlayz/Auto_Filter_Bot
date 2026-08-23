#Thanks @dreamxbotz for helping in this journey 

import jinja2
from info import BIN_CHANNEL, URL
from dreamxbotz.Bot import dreamxbotz
from dreamxbotz.util.human_readable import humanbytes
from dreamxbotz.util.file_properties import get_file_ids
from dreamxbotz.server.exceptions import FIleNotFound, InvalidHash
import urllib.parse
import logging
import aiohttp
import mimetypes


mimetypes.add_type("video/mp4", ".mp4")
mimetypes.add_type("video/x-matroska", ".mkv")
mimetypes.add_type("video/webm", ".webm")
mimetypes.add_type("video/x-msvideo", ".avi")
mimetypes.add_type("video/quicktime", ".mov")


def guess_mime_type(file_name: str, mime_type: str) -> str:
    guessed_type = mimetypes.guess_type(file_name or "")[0]
    if not mime_type or mime_type == "application/octet-stream":
        return guessed_type or "application/octet-stream"
    return mime_type


async def render_page(id, secure_hash, src=None):
    await dreamxbotz.get_messages(int(BIN_CHANNEL), int(id))
    file_data = await get_file_ids(dreamxbotz, int(BIN_CHANNEL), int(id))
    if not file_data:
        raise FIleNotFound
    if file_data.unique_id[:6] != secure_hash:
        logging.debug(f"link hash: {secure_hash} - {file_data.unique_id[:6]}")
        logging.debug(f"Invalid hash for message with - ID {id}")
        raise InvalidHash

    src = urllib.parse.urljoin(
        URL,
        f"{id}/{urllib.parse.quote_plus(file_data.file_name or 'file')}?hash={secure_hash}",
    )

    mime_type = guess_mime_type(file_data.file_name, file_data.mime_type)
    tag = mime_type.split("/")[0].strip()
    file_size = humanbytes(file_data.file_size)
    if tag in ["video", "audio"]:
        template_file = "dreamxbotz/template/req.html"
    else:
        template_file = "dreamxbotz/template/dl.html"
        async with aiohttp.ClientSession() as s:
            async with s.get(src) as u:
                content_length = u.headers.get("Content-Length")
                if content_length:
                    file_size = humanbytes(int(content_length))

    with open(template_file) as f:
        template = jinja2.Template(f.read())

    file_name = (file_data.file_name or "file").replace("_", " ")

    return template.render(
        file_name=file_name,
        file_url=src,
        download_url=f"{src}&download=1",
        file_size=file_size,
        file_unique_id=file_data.unique_id,
        mime_type=mime_type,
    )

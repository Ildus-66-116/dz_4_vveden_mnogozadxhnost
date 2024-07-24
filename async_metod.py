import aiohttp
import asyncio
from urllib.parse import urlparse
import os
import sys
import time

urls = ['https://klike.net/uploads/posts/2023-02/1675842942_3-315.jpg',
        'https://get.wallhere.com/photo/3840x2160-px-mountain-1327909.jpg',
        'https://s1.1zoom.me/big3/937/Bridges_USA_Golden_Gate_Bridge_California_San_601713_3872x2592.jpg',
        'https://get.wallhere.com/photo/2700x1800-px-building-castle-forest-Hohenzollern-landscape-1077207.jpg',
        'https://wallpaper.forfun.com/fetch/03/03f8cd3f6796daaacc1fe43ffb7704b7.jpeg',
        'https://get.wallhere.com/photo/lake-mountain-tree-water-landscape-1076231.jpg',
        'https://s1.1zoom.ru/big3/212/Thailand_Tropics_Parks_Waterfalls_Stones_Crag_Moss_564248_3200x1800.jpg',
        ]
start_time = time.time()


async def download_image(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            filename = os.path.basename(urlparse(url).path)
            filename = 'asyncio/' + filename
            with open(filename, 'wb') as f:
                f.write(await resp.read())
            print(f"Скачано изображение: {filename} in {time.time() - start_time:.2f} seconds")


async def download_images(urls):
    tasks = []
    for url in urls:
        task = asyncio.create_task(download_image(url))
        tasks.append(task)
    await asyncio.gather(*tasks)


def main(urls):
    global_start_time = time.time()
    asyncio.run(download_images(urls))
    end_time = time.time()
    print(f"\nОбщее время выполнения: {end_time - global_start_time:.2f} секунд")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        urls = sys.argv[1:]
    else:
        urls = urls
    if not urls:
        print("Пожалуйста, укажите хотя бы один URL для скачивания изображений.")

main(urls)

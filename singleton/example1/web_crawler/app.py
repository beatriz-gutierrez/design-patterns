from image_downloader import ImageDonwloaderThread
from singleton_images import Singleton
from transverse_site import traverse_site


if __name__ == "__main__":

    url_root = (
        "https://blog.kartones.net/post/js-rle-algorithm-v3-bit-level-rle/"
    )

    singleton_crawler = Singleton()
    singleton_crawler.queue_to_parse=[url_root]

    traverse_site()

    # 2 parallel threads
    for n_thread in range(0, 2):
        thread = ImageDonwloaderThread(n_thread+1, f"Thread-{n_thread+1}", n_thread+1)
        thread.start()

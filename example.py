"""YouTube Video Downloader with the Scrapely Python SDK (scrapely-client-python).

Install: pip install scrapely-client-python
Run:     SCRAPELY_TOKEN=your_token python example.py
"""
import json
import os

from scrapely_client import ScrapelyClient


def main() -> None:
    client = ScrapelyClient(os.environ['SCRAPELY_TOKEN'])

    run_input = {
        "videos": [
            {
                "url": "https://www.youtube.com/watch?v=jNQXAC9IVRw"
            }
        ],
        "maxVideos": 10,
        "preferredQuality": "720p",
        "preferredFormat": "mp4",
        "storeInKVStore": True,
        "filenameTemplateParts": [
            "title"
        ],
        "transcriptionAndSubtitle": "NONE",
        "proxyConfiguration": {
            "useScrapelyProxy": True,
            "scrapelyProxyGroups": [
                "RESIDENTIAL"
            ]
        }
    }

    # Start the scraper on Scrapely and wait for it to finish.
    run = client.actor('echofield/youtube-video-downloader').call(run_input=run_input)
    if run is None:
        raise RuntimeError('Run was not found')

    # Read the scraped results from the run's dataset.
    items = list(client.dataset(run.default_dataset_id).iterate_items())
    print(f'Scraped {len(items)} results')
    print(json.dumps(items, indent=2, ensure_ascii=False))


if __name__ == '__main__':
    main()

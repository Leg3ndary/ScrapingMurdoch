# pylint:skip-file

import re

import httpx

nums = []

for i in range(6):
    print(f"Scraping Page {i}")
    transcript = httpx.request(
        "GET",
        f"https://transcripts.foreverdreaming.org/viewforum.php?f=13&start={100 + i * 25}",
    )
    matches = re.findall(
        r"""(?<=viewtopic.php\?f=13&amp;t=).*?(?=" class=)""", transcript.text
    )
    for match in matches:
        nums.append(match[0:5])
    print("Scraping Complete")

print(nums)

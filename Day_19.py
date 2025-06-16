import threading
import requests

def download_file(url, filename):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        with open(filename, 'wb') as f:
            f.write(response.content)
        print(f"✅ Downloaded: {filename}")
    except Exception as e:
        print(f"❌ Failed to download {filename}: {e}")

files = [
    ('https://media.geeksforgeeks.org/wp-content/uploads/20240226121023/GFG.pdf', 'research_paper1.pdf'),
    ('https://drodrik.scholar.harvard.edu/sites/scholar.harvard.edu/files/what_the_mercantilists_got_right.pdf', 'research_paper2.pdf'),
    ('https://drodrik.scholar.harvard.edu/sites/scholar.harvard.edu/files/africas_manufacturing_puzzle_050125.pdf', 'research_paper3.pdf'),
    ('https://drodrik.scholar.harvard.edu/sites/scholar.harvard.edu/files/servicing_development.pdf', 'research_paper4.pdf'),
    ('https://drodrik.scholar.harvard.edu/sites/scholar.harvard.edu/files/global_distribution_of_authorship_in_economics_-_january_2025.pdf', 'research_paper5.pdf')
]

threads = []

for url, filename in files:
    t = threading.Thread(target=download_file, args=(url, filename))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("\n🎉 All files downloaded successfully using requests!")

import requests
import xml.etree.ElementTree as ET
import trafilatura
from src.services.qdrant_service import qdrant_service

SITEMAP_URL = "https://physical-ai-humanoid-robotics-cours-eight.vercel.app/sitemap.xml"


def get_all_urls(sitemap_url):
    xml = requests.get(sitemap_url).text
    root = ET.fromstring(xml)

    urls = []
    for child in root:
        loc_tag = child.find("{http://www.sitemaps.org/schemas/sitemap/0.9}loc")
        if loc_tag is not None:
            urls.append(loc_tag.text)
    return urls


def extract_text_from_url(url):
    try:
        html = requests.get(url, timeout=10).text
        text = trafilatura.extract(html)
        if not text:
            print(f"[WARNING] No text extracted from: {url}")
        return text
    except Exception as e:
        print(f"[ERROR] Failed to fetch {url}: {e}")
        return None


# ✅ HARD-SAFE CHUNKER (NO INFINITE LOOP)
def chunk_text(text, max_chars=1200):
    chunks = []

    while len(text) > max_chars:
        split_pos = text.rfind(". ", 0, max_chars)

        # fallback — FORCE progress
        if split_pos == -1 or split_pos < max_chars * 0.3:
            split_pos = max_chars

        chunk = text[:split_pos].strip()
        if chunk:
            chunks.append(chunk)

        # 🔥 GUARANTEED SHRINK
        text = text[split_pos + 1:].strip()

    if text.strip():
        chunks.append(text.strip())

    return chunks


def ingest_book():
    urls = get_all_urls(SITEMAP_URL)
    print(f"Found {len(urls)} URLs in sitemap.")

    qdrant_service.create_collection()
    print("📂 Qdrant collection created/recreated.")

    global_id = 1

    for url in urls:
        try:
            print(f"\nProcessing: {url}")
            text = extract_text_from_url(url)
            if not text:
                continue

            chunks = chunk_text(text)

            for ch in chunks:
                qdrant_service.upsert_chunk(ch, global_id, url)
                print(f"Saved chunk {global_id}")
                global_id += 1

        except Exception as e:
            print(f"[ERROR] URL failed: {url}")
            print(e)

    print("\n✔️ Ingestion completed!")
    print(f"Total chunks stored: {global_id - 1}")


if __name__ == "__main__":
    ingest_book()

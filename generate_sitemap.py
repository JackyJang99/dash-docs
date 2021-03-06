from dash_docs import chapter_index


def create_sitemap():
    sitemap = ''
    for url in sorted(chapter_index.URL_TO_CONTENT_MAP.keys()):
        if url.startswith('/'):
            sitemap += (
                '<url>\n' +
                '    <loc>https://dash.plotly.com{}</loc>\n'.format(url) +
                '</url>\n'
            )
    return (
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.sitemaps.org/schemas/sitemap/0.9 http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd">\n' +
        '<!-- autogenerated by generate-sitemap.py - do not modify manually -->' +
        sitemap +
        '</urlset>\n'
    )

def generate_sitemap():
    sitemap = create_sitemap()
    # Use the same newlines as is currently used
    with open('dash_docs/assets/sitemap.xml', 'rb') as f:
        old_sitemap = f.read().decode()
    if "\r" in old_sitemap:
        sitemap = sitemap.replace("\n", "\r\n")
    with open('dash_docs/assets/sitemap.xml', 'wb') as f:
        f.write(sitemap.encode())


if __name__ == '__main__':
    generate_sitemap()

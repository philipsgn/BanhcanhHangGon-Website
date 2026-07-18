# Banh Canh Ga Hang Gon

Static website for Banh Canh Ga - Xoi Ga Hang Gon.

## Project Structure

```text
.
+-- banhcanhga.html
+-- images/
    +-- behind-scenes/
    +-- menu/
```

## Run Locally

This is a static HTML project. Open `banhcanhga.html` directly in a browser.

For a local server, run one of these commands from the project folder:

```powershell
python -m http.server 8080
```

Then open:

```text
http://localhost:8080/banhcanhga.html
```

## Main Sections

- Home
- Gioi thieu
- Menu
- Hau truong
- Danh gia khach hang
- Vi tri

## Assets

All active image assets are stored under `images/`. Menu item detail banners are loaded through `data-detail` attributes in `banhcanhga.html`.

## Notes

- The site uses Google Fonts.
- The location map points to the real Google Maps place for Banh Canh Ga - Xoi Ga Hang Gon.
- Keep image paths relative so the site works when opened locally or hosted as a static page.

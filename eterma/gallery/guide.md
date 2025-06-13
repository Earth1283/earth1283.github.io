# Intended purpose
This folder `/eterma/gallery`, we store images in .png format. They we sync changes to lines 294 and beyond.
```html
<script>
        // Gallery functionality
        const galleryData = {
            "1": {
                "author": "腐竹",
                "description": "暂无",
                "filename": "background1.png"
            },
            "2": {
                "author": "腐竹",
                "description": "暂无",
                "filename": "background2.png"
            }
        };
```
New gallery functinoalities are expected to be added with the following format:
```json
"number": {
    "author": "insert author name",
    "description": "insert description",
    "filename": "filename to the image"
}
```
The presence of `descriptions.json` is merely for reference and nothing else. Removal is scheduled soon.
# pymbbooth

Raspberry pie photobooth app built with pywebview and svelte.
App is hardcoded for my purpose, if you want to use it you will
have to adapt it for your printer and camera module. 
You will need to edit `pymbbooth/config.py`

If you want to use google photos api you will need to generate credentials.json
file and save it to project root. 
You can generate that file here: https://developers.google.com/photos/library/guides/get-started

## Development

### Instalation

```bash
pip install -r requirements/requirements.txt'
# or if you want develop with livereload
# pip install -r requirements/develop.txt'
pip install -e .
yarn
```
### Run

```bash
photobooth
```


### Autoreload
Run app in development mode with autoreload

```bash
python3 develop.py
```

### Code formating
```
yarn format
black .
```
# pymbbooth

Raspberry pie photobooth app built with pywebview and svelte.
App is hardcoded for my purpose, if you want to use it you will
have to adapt it for your printer and camera module. 
You will probably also have to rewrite buttons since there is no localization 
and everything is in slovak language.

## Development

### Instalation

```bash
pip install -e '.[dev, pi]'
yarn
```
Optional dependencies:
- dev: You can ommit this if you dont need to run with autoreload.
- pi: Ommit if you are installing without raspberry pi (UI will show but capture and printing will be mocked).

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
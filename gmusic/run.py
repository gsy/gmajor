# -*- coding: utf-8 -*-

from gmusic import create_app
from gmusic.config import config

app = create_app(config)


if __name__ == '__main__':
    app.run(debug=True)

#!/usr/bin/env python
# coding=utf-8

import webbrowser

class Movie():
    """
    This ls the Movie class with title, storyline, poster_image_url,
    and trailer_url properties defined.
    Also we could get and set those properties with defined handlers.
    """
    def __init__(self, title, storyline, poster_image_url, trailer_url):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        self.trailer_url = trailer_url

    def get_title(self):
        """get movie title."""
        return self.title

    def set_title(self, title):
        """save new title."""
        self.title = title

    def get_storyline(self):
        """get movie storyline."""
        return self.storyline

    def set_storyline(self, storyline):
        """save new storyline."""
        self.storyline = storyline

    def get_poster_image_url(self):
        """get movie poster image url."""
        return self.poster_image_url

    def set_poster_image_url(self, poster_image_url):
        """save new poster image url."""
        self.poster_image_url = poster_image_url

    def get_trailer_url(self):
        """get movie trailer url."""
        return self.trailer_url

    def set_trailer_url(self, trailer_url):
        """save new trailer url."""
        self.trailer_url = trailer_url

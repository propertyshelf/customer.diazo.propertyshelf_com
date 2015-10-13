# -*- coding: utf-8 -*-
"""Propertyshelf Diazo Theme fot propertyshelf.com."""

# python imports
import logging

# zope imports
from zope.i18nmessageid import MessageFactory

# local imports
from customer.diazo.propertyshelf_com import config

logger = logging.getLogger(config.PROJECT_NAME)
_ = MessageFactory('customer.diazo.propertyshelf_com')


def initialize(context):
    """Initializer called when used as a Zope 2 product."""

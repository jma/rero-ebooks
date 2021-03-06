# -*- coding: utf-8 -*-
#
# Copyright (C) 2018 RERO.
#
# RERO Ebooks is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Signals connections for RERO ebooks."""

from dojson.contrib.marc21.utils import create_record

from rero_ebooks.tasks import create_records

from .dojson.marc21 import marc21


def publish_harvested_records(sender=None, records=[], *args, **kwargs):
    """Create, index the harvested records."""
    # name = kwargs['name']
    converted_records = []
    for record in records:
        rec = create_record(record.xml)
        rec = marc21.do(rec)
        converted_records.append(rec)
    verbose = kwargs.get('verbose', False)
    create_records(converted_records, verbose=verbose)

# vim: set fileencoding=utf-8 :
"""
~~~~~~~
Classes
~~~~~~~

Contains :class:`DictableModel` that can be used as a base class for
:meth:`sqlalchemy.ext.declarative_base`.

"""

from __future__ import absolute_import, division

from zmdictalchemy import utils


class DictableModel(object):
    """Can be used as a base class for :meth:`sqlalchemy.ext.declarative`

    Contains the methods :meth:`DictableModel.__iter__`,
    :meth:`DictableModel.asdict` and :meth:`DictableModel.fromdict`.

    :ivar zmdictalchemy_exclude: List of properties that should always be \
            excluded.
    :ivar zmdictalchemy_exclude_underscore: If True properties starting with an \
            underscore will always be excluded.
    :ivar zmdictalchemy_fromdict_allow_pk: If True the primary key can be \
            updated by :meth:`DictableModel.fromdict`.
    :ivar zmdictalchemy_asdict_include: List of properties that should always \
            be included when calling :meth:`DictableModel.asdict`
    :ivar zmdictalchemy_fromdict_include: List of properties that should always \
            be included when calling :meth:`DictableModel.fromdict`

    """

    asdict = utils.asdict

    fromdict = utils.fromdict

    __iter__ = utils.iter

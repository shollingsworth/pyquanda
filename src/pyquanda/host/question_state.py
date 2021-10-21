#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Abstract method for other modules."""
from typing import Any

from filelock import FileLock
from sqlitedict import SqliteDict

from pyquanda.environment import INTERVIEW_STATE_REMOTE_FILE, LOCK_FILE


class StateData:
    """StateData."""

    lockfile = FileLock(lock_file=str(LOCK_FILE))

    @staticmethod
    def _get_sqlfile() -> SqliteDict:
        return SqliteDict(
            filename=str(INTERVIEW_STATE_REMOTE_FILE),
            tablename="StateData",
        )

    @property
    def _db(self) -> SqliteDict:
        """db

        Args:
            self:

        Returns:
            SqliteDict: sql dictionary
        """
        if not INTERVIEW_STATE_REMOTE_FILE.exists():
            with self._get_sqlfile() as sql:
                sql["init"] = True
                sql.commit()
            INTERVIEW_STATE_REMOTE_FILE.chmod(0o0666)
            LOCK_FILE.chmod(0o0666)
        return self._get_sqlfile()

    def set(self, key: str, value: Any):
        """[TODO:summary]

        [TODO:description]

        Args:
            key: [TODO:description]
            value: [TODO:description]
        """
        with self.lockfile:
            with self._db as db:
                db[key] = value
                db.commit()

    def get(self, key: str, required: bool = True) -> Any:
        """get key value

        Args:
            key: value key
            required: defaults to true

        Returns:
            Any: result

        Raises:
            KeyError:  value does not exist if required is not set to false
        """
        with self.lockfile:
            with self._db as db:
                try:
                    return db[key]
                except KeyError:
                    if not required:
                        return None
                    raise

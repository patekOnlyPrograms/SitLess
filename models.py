from datetime import datetime, timezone

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, Boolean, DateTime, String
from __main__ import db

class TimerLog(db.Model):
    __tablename__ = "Timer"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    start_time: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now(timezone.utc))
    end_time: Mapped[DateTime] = mapped_column(DateTime, nullable=True)
    completed: Mapped[bool] = mapped_column(Boolean, default=False)  # Ran full course
    ended_early: Mapped[bool] = mapped_column(Boolean, default=False)  # User ended early

    def __repr__(self):
        return (
            f"<TimerLog(id={self.id}, interval={self.interval_minutes}, "
            f"completed={self.completed}, ended_early={self.ended_early})>"
        )